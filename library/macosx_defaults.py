#!/usr/bin/python
# coding: utf-8
# Copyright © 2016 fclaerhout.fr, released under the MIT license.
# WANT_JSON

DOCUMENTATION = """
---
module: macosx_defaults
description:
- Manage OSX domain defaults
options:
  domain:
    description:
    - Domain name.
    required: no
    default: -g
  state:
    description:
    - Either C(present) or C(absent).
    - If key is defined, write/delete the key.
    - If key is undefined, import/delete the domain.
    required: yes
  path:
    description:
    - Required if state=present and key is undefined.
    - Path to a plist file.
    required: no
  key:
    description:
    - Key associated to the domain.
    required: no
  value:
    description:
    - Required if state=present and key is defined.
    - The actual value type is the same than the YAML type.
    required: no
"""

EXAMPLES = """
---
- macosx_defaults:
    domain: com.apple.Dock
    state: present
    key: tilesize
    value: 45
- macosx_defaults:
    domain: com.apple.Xcode
    state: present
    path: /tmp/com.apple.Xcode.plist
"""

import subprocess, tempfile, filecmp, shutil, json, sys, os

def Path(*args):
	return os.path.expanduser(os.path.join(*args))

class Defaults(object):

	def __call__(self, *args):
		return subprocess.check_output(args)

	def __init__(self, domain):
		self.domain = domain

	def exists(self):
		return self.domain in self("defaults", "domains").strip().split(", ")

	def create(self, path):
		"import defaults from path if differing and return True, return False otherwise"
		if os.path.dirname(path) == Path("~", "Library", "Preferences"):
			return False
		with tempfile.NamedTemporaryFile() as fp:
			self("defaults", "export", self.domain, fp.name)
			if filecmp.cmp(path, fp.name):
				return False
		self("defaults", "import", self.domain, path)
		return True

	def purge(self):
		"delete defaults if any and return True, return False otherwise"
		if self.exists():
			filename = "{}.plist".format(self.domain)
			paths = (
				Path("~", "Library", "Preferences", filename),
				Path("~", "Library", "Containers", self.domain, "Data", "Library", "Preferences", filename))
			paths = filter(os.path.exists, paths)
			for path in paths:
				os.remove(path)
			assert not self.exists(), "oops, defaults still exist after purge"
			return True
		else:
			return False

	def write(self, key, value):
		"write key if differing and return True, return False otherwise"
		if key in self("defaults", "read", self.domain):
			current_value = self("defaults", "read", self.domain, key).strip()
			_, current_type = self("defaults", "read-type", self.domain, key).strip().split(" is ")
			if current_type == "boolean":
				current_value = False if current_value == "0" else True
			elif current_type == "string":
				current_value = current_value.decode("utf-8")
			elif current_type == "integer":
				current_value = int(current_value)
			elif current_type == "float":
				current_value = float(current_value)
			else:
				raise Exception("{}: unsupported type on reading".format(current_type))
			if current_value == value:
				return False
			#else: # uncomment to debug
			#	raise Exception("{} != {}".format(current_value, value))
		args = ["defaults", "write", self.domain, key]
		if isinstance(value, bool):
			args += ["-bool", "true" if value else "false"]
		elif isinstance(value, unicode):
			args += ["-string", value.encode("utf-8")]
		elif isinstance(value, int):
			args += ["-int", "{}".format(value)]
		elif isinstance(value, float):
			args += ["-float", "{}".format(value)]
		else:
			raise Exception("{}: unsupported type on writing".format(type(value).__name__))
		self(*args)
		return True

	def delete(self, key):
		raise NotImplementedError

def succeed(changed, **kwargs):
	kwargs.update({"changed": changed})
	print json.dumps(kwargs)
	raise SystemExit

def fail(msg):
	print json.dumps({
		"failed": True,
		"msg": msg,
	})
	raise SystemExit(1)

def main():
	if len(sys.argv) < 2:
		raise SystemExit("usage: {} <path>".format(sys.argv[0]))
	with open(sys.argv[1], "r") as fp:
		args = json.load(fp)
	domain = args.get("domain", "-g")
	state = args["state"]
	key = args.get("key", None)
	try:
		if key:
			if state == "present":
				changed = Defaults(domain).write(key, args["value"])
			elif state == "absent":
				changed = Defaults(domain).delete(key)
			else:
				raise Exception("{}: invalid state".format(state))
			succeed(
				changed = changed,
				domain = domain,
				state = state,
				key = key)
		else:
			if state == "present":
				path = Path(args["path"])
				changed = Defaults(domain).create(path)
			elif state == "absent":
				changed = Defaults(domain).purge()
			else:
				raise Exception("{}: invalid state".format(state))
			succeed(
				changed = changed,
				domain = domain,
				state = state)
	except Exception as exc:
		fail("{}: {}".format(type(exc).__name__, exc))

if __name__ == "__main__": main()

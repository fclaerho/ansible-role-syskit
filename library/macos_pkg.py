#!/usr/bin/python
# coding: utf-8
# Copyright © 2016 fclaerhout.fr — released under the MIT license.
# WANT_JSON

DOCUMENTATION = """
---
module: macosx_pkg
description:
- Manage OSX Installer packages
options:
  name:
    description:
    - Package id.
    default: no
  state:
    description:
    - Either C(present) or C(absent).
    default: no
"""

EXAMPLES = """
---
- macosx_pkg:
    name: com.example.Foo
    state: absent
"""

import subprocess, json, sys, os

class Pkgutil(object):

	def __call__(self, *args):
		return subprocess.check_output(args)

	def list(self):
		return sorted(self("pkgutil", "--packages").splitlines())

	def is_installed(self, name):
		return name in self.list()

	def install(self, name):
		if self.is_installed(name):
			return False
		else:
			raise NotImplementedError

	def uninstall(self, name, interactive = True):
		if self.is_installed(name):
			# fetch package installation directory:
			info = {}
			for line in self("pkgutil", "--pkg-info", name).splitlines():
				key, value = line.split(":")
				info[key.strip()] = value.strip()
			dirname = os.path.join(info["volume"], info["location"])
			# fetch file list:
			stdout = self("pkgutil", "--files", name)
			paths = tuple(os.path.join(dirname, line) for line in stdout.splitlines())
			# ask user for confirmation:
			if interactive:
				print "\n".join(paths)
				if raw_input("Proceed (y/n)? ") != "y": return
			# delete files first...
			for path in filter(os.path.isfile, paths):
				if os.path.exists(path):
					os.remove(path)
			# ...then delete *empty* directories
			for path in sorted(filter(os.path.isdir, paths), reverse = True):
				if os.path.exists(path):
					if not os.listdir(path):
						os.rmdir(path)
					else:
						sys.stderr.write("{}: skipping non-empty directory\n".format(path))
			self("pkgutil", "--forget", name)
			assert not self.is_installed(name), "failed to uninstall package -- you might miss credentials"
			return True
		else:
			return False

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
	name = args["name"]
	state = args["state"]
	pkgutil = Pkgutil()
	try:
		if args["state"] == "present":
			changed = Pkgutil().install(name)
		elif args["state"] == "absent":
			changed = Pkgutil().uninstall(
				name = name,
				interactive = False)
		else:
			raise Exception("{}: invalid state".format(state))
		succeed(
			changed = changed,
			state = state,
			name = name)
	except Exception as exc:
		fail("{}: {}".format(type(exc).__name__, exc))

if __name__ == "__main__": main()

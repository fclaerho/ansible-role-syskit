#!/usr/bin/python
# coding: utf-8
# Copyright © 2016 fclaerhout.fr, released under the MIT license.
# WANT_JSON

DOCUMENTATION = """
---
module: macosx_app
description:
- Manage OSX applications
options:
  name:
    description:
    - Application name.
    required: yes
  state:
    description:
    - Either C(present) or C(absent).
    required: yes
"""

EXAMPLES = """
---
- macosx_app:
    name: Sublime Text 2
    state: absent
"""

import subprocess, shutil, json, sys, os

class Dir(object):

	def __init__(self, *args):
		self.path = os.path.expanduser(os.path.join(*args))

	def exists(self):
		return os.path.exists(self.path)

	def create_if_not_exists(self):
		if not self.exists():
			os.mkdir(self.path)

	def delete_if_empty(self):
		if not os.listdir(self.path):
			os.rmdir(self.path)

class App(object):

	def __init__(self, name):
		self.name = name
		self.localdir = Dir("~", "Applications")

	def __call__(self, *args):
		return subprocess.check_output(args)

	def get_path(self):
		"return .app path or None"
		args = ["find", "/Applications"]
		if self.localdir.exists():
			args.append(self.localdir.path)
		args += ["-mindepth", "1", "-maxdepth", "2", "-type", "d", "-name", "{}.app".format(self.name)]
		stdout = self(*args)
		if not stdout:
			return None
		else:
			try:
				path, = stdout.splitlines()
				return path
			except:
				raise Exception("multiple matching apps found -- please report this")

	def uninstall(self):
		path = self.get_path()
		if path:
			shutil.rmtree(path)
			self.localdir.delete_if_empty()
			return True
		else:
			return False

	def install(self):
		path = self.get_path()
		if path:
			return False
		else:
			self.localdir.create_if_not_exists()
			# TODO: download from the appstore or from a given .dmg URL
			# https://github.com/fclaerho/localhost/issues/3
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
	state = args["state"]
	name = args["name"]
	try:
		if state == "present":
			changed = App(name).install()
		elif state == "absent":
			changed = App(name).uninstall()
		else:
			raise Exception("{}: invalid state".format(state))
		succeed(
			changed = changed,
			state = state,
			name = name)
	except Exception as exc:
		fail("{}: {}".format(type(exc).__name__, exc))

if __name__ == "__main__": main()

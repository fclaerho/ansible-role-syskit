#!/usr/bin/python
# coding: utf-8
# Copyright © 2016 fclaerhout.fr — released under the MIT license.
# WANT_JSON

DOCUMENTATION = """
---
module: macosx_flags
description:
- Manage OSX file flags
options:
  path:
    description:
    - File path.
    required: yes
  archived:
    description:
    - Boolean.
    - Archived flag (super-user only.)
    required: no
  opaque:
    description:
    - Boolean.
    - Opaque flag (owner or super-user only.)
    - Directory is opaque when viewed through a union mount.
    required: no
  dump:
    description:
    - Boolean.
    required: no
  sappend:
    description:
    - Boolean.
    - Set the system append-only flag (super-user only.)
    - May only be unset when the system is in single-user mode.
    required: no
  schange:
    description:
    - Boolean.
    - Set the system immutable flag (super-user only.)
    - May only be unset when the system is in single-user mode.
    required: no
  uappend:
    description:
    - Boolean.
    - Set the user append-only flag (owner or super-user only.)
    required: no
  uchange:
    description:
    - Boolean.
    - Set the user immutable flag (owner or super-user only)
    required: no
  hidden:
    description:
    - Boolean.
    - Hide item from GUI.
    required: no
"""

EXAMPLES = """
---
- macosx_flags:
    path: ~/Public
    uchange: yes
"""

import subprocess, json, sys, os

def get_flags(path):
	# man chflags:
	# You can use "ls -lO" to see the flags of existing files.
	stdout = subprocess.check_output(("ls", "-dlO", path))
	_, _, _, _, value, _, _, _, _, _ = stdout.splitlines()[0].split()
	return value.split(",") if value != "-" else ()

def set_flags(path, flags):
	subprocess.check_call(("chflags", "-LR", ",".join(flags), path))

ALIASES = {
	"archived": ("arch",),
	"opaque": (),
	"dump": (),
	"sappend": ("sappnd",),
	"schange": ("schg", "simmutable"), # system immutable
	"uappend": ("uappnd",),
	"uchange": ("uchg", "uimmutable"), # user immutable
	"hidden": (),
}

# from manpage:
# Putting/removing the letters "no" before/from a keyword causes the flag to be cleared.
def normalized(flags):
	"normalize a list of flags"
	result = []
	for item in flags:
		if item.startswith("no"):
			negated = True
			item = item[2:]
		else:
			negated = False
		if item in ALIASES: # is it a basename?
			flag = item
		else:
			for key in ALIASES:
				if item in ALIASES[key]: # is it an alias?
					flag = key
					break
			else:
				raise KeyError("{}: no such flag".format(item))
		result.append("no{}".format(flag) if negated else flag)
	return result

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
	path = os.path.expanduser(args["path"])
	flags = []
	for key in ALIASES:
		if key in args:
			flags.append(key if args[key] else "no{}".format(key))
	try:
		if set(normalized(get_flags(path))) == set(flags):
			changed = False
		else:
			changed = True
			set_flags(
				path = path,
				flags = flags)
		succeed(
			changed = changed,
			flags = flags,
			path = path)
	except Exception as exc:
		fail("{}: {}".format(type(exc).__name__, exc))

if __name__ == "__main__": main()

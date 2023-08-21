# -*- coding: utf-8 -*-


import gdb
import sys


class MyCommand(gdb.Command):
	def __init__(self):
		if int(sys.version[0]) >= 3:
			super().__init__("my_command", gdb.COMMAND_SUPPORT)
		else:
			super(MyCommand, self).__init__("my_command", gdb.COMMAND_SUPPORT)
	def invoke(self, arg, from_tty):
		print("length is : {}".format(len(arg)))
		for i in range(len(arg)):
			print("element is {}".format(arg[i]))
		cv_arg = gdb.string_to_argv(arg)
		print(cv_arg)

class PointerCommand(gdb.Command):
	'''print pointer arg
Usage: print_pointer arg [arg_type]
Output:
  	arg : arg type value
	'''
	def __init__(self):
		if int(sys.version[0]) >= 3:
			super().__init__('print_pointer', gdb.COMMAND_USER)
		else:
			super(PointerCommand, self).__init__('print_pointer', gdb.COMMAND_USER)
	def invoke(self, argv, from_tty):
		args = gdb.string_to_argv(argv)
		pointer_v = args[0]
		pointer = gdb.parse_and_eval(pointer_v)
		pointer_type = gdb.lookup_type(args[1]).pointer() if len(args) >= 2 else pointer.type
		print("{} : {}".format(pointer, pointer.cast(pointer_type).dereference()))

class PrintTypeCommand(gdb.Command):
	'''	print elements types
Usage: print_type arg1 arg2 arg3 ...
Output:
 	[arg1] type is [type]
 	[arg2] type is [type]
 	[arg3] type is [type]
	'''
	def __init__(self):
		if int(sys.version[0]) >= 3:
			super().__init__("print_type", gdb.COMMAND_USER)
		else:
			super(PrintTypeCommand, self).__init__("print_type", gdb.COMMAND_USER)

	def invoke(self, argv, from_tty):
		vals = gdb.string_to_argv(argv)
		for val in vals:
			gdb_val = gdb.parse_and_eval(val)
			print("[{}] type is [{}]".format(val, gdb_val.type))
PrintTypeCommand()
MyCommand()
PointerCommand()



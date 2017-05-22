"""Command line Check Hash

Usage: 
  arguments_example.py [-h] [FILE]

Arguments:
  FILE        optional input file

Options:
  -h --help
"""
from docopt import docopt
import hashlib
import sys
import os


if __name__ == '__main__':
	arguments = docopt(__doc__)
	if arguments['FILE'] is not None:
		file_path = arguments['FILE']
		if os.path.isfile(file_path):
			with open("docopt.py", "rb") as f:
				print("method || value")
				print("-"*48)
				print("md5    || %s" % hashlib.md5(f.read()).hexdigest())
				print("sha1   || %s" % hashlib.sha1(f.read()).hexdigest())
				print("sha256 || %s" % hashlib.sha256(f.read()).hexdigest())
				print("sha512 || %s" % hashlib.sha512(f.read()).hexdigest())
		else:
			print("%s is not a invalid file path" % file_path)
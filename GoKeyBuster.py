import subprocess
import argparse

parser = argparse.ArgumentParser(description='Arguments for GoKeyBruter')
parser.add_argument('-g', help='The GoKey Binary Location')
parser.add_argument('-r', help='The GoKey arguments.r')
parser.add_argument('-p', help='The GoKey Plaintext Password')
parser.add_argument('-v', help='Set Verbosity On/Off')
parser.add_argument('-w', help='Custom wordlist')
arguments = parser.parse_args()

with open(arguments.w) as words:
	for line in words: 
		if(arguments.v):
			print "[*] Trying Password - " + line
		output = subprocess.check_output([arguments.g, "-r", arguments.r, "-p", line])
		if(output.strip() == arguments.p.strip()):
			print "[+] Found the master password! - " + line
			break


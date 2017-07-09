import subprocess
import argparse

parser = argparse.ArgumentParser(description='Arguments for GoKeyBruter')
parser.add_argument('-g', required=True, help='The GoKey Binary Location')
parser.add_argument('-r', help='The GoKey "Realm"')
parser.add_argument('-p', help='The GoKey Plaintext Password')
parser.add_argument('-v', help='Set Verbosity On/Off')
parser.add_argument('-w', required=True, help='Custom wordlist (Currently Required)')

parser.add_argument('--brute-realm', help='Attempt to Brute Force the Realm')
parser.add_argument('--realm-list', help='Attempt to Brute Force the Realm')
parser.add_argument('--master-password', help='If the --brute-realm flag is set you can use this flag to just brute the realm if you already know the Master Password but need the Realm')

arguments = parser.parse_args()
master_password = ''
realm = arguments.r
with open(arguments.w) as words:
	for line in words: 
		if(arguments.v):
			print "[*] Trying Password - " + line
			
		if(arguments.brute_realm):
			with open(arguments.realm_list) as realm_list:
				for r in realm_list:
					r = r.strip()
					if(arguments.v):
						print "[*] Trying Realm - "  + r						
					output = subprocess.check_output([arguments.g, "-r", r, "-p", line])
					
					master_password = output.strip()
					if(master_password == arguments.p.strip()):
						print "[+] Found the master password! [" + master_password + ":" + realm + "]" 
						break
		else:
			output = subprocess.check_output([arguments.g, "-r", arguments.r, "-p", line])
			master_password = output.strip()
			print "comparing " + master_password + " with " + arguments.p.strip()
			if(master_password == arguments.p.strip()):
				print "[+] Found the master password! [" + master_password + ":" + realm + "]" 
				break
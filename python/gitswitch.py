#!/usr/bin/python3

# gitswitch.py - Switches between git accounts globally

import os, sys

name = sys.argv[1]

class Account:
    def __init__(self, name, email, ssh_command):
        self.name = name
        self.email = email
        self.ssh_command = ssh_command



# Account addition:

# first_account_handle = Account("<account-username>", "<account-email>", "ssh -i </path/to/ssh/key>")
# secont_account_handle = Account("<account-username>", "<account-email>", "ssh -i </path/to/ssh/key>")
# accounts = [first_account_handle, second_account_handle]



account_index = 0

for i, x in enumerate(accounts):
    if x.name == name:
        account_index = i
        break


os.system("/bin/bash -c 'git config --global user.name \"" + accounts[account_index].name + "\"'")
os.system("/bin/bash -c 'git config --global user.email \"" + accounts[account_index].email + "\"'")
os.system("/bin/bash -c 'git config --global core.sshCommand \"" + accounts[account_index].ssh_command + "\"'")

print("Switched to account "+accounts[account_index].name+".")


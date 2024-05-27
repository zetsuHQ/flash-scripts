<h1>Wordlist encoder</h1>
<p>A simple python script for solving PortSwigger's Web Security Academy's "Brute-forcing a stay-logged-in cookie" lab.</p>

<p>The lab consists in an application that assigns a low-entropy stay-logged-in cookie to the user, which has the format of 'base64(username+':'+md5HashOfPassword)', alowing attackers to brute force that cookie and gain unauthorized access to other user's accounts. The victim for this lab is the account under the username "carlos".</p>

<p>This script works by hashing all the lines from "data/wordlist.txt" using MD5, writing everything on "data/hashed.txt", then concatenating "carlos:" to the beginning of each hash and encoding them to base64. The final product is "data/encoded.txt".</p>

<p>The list of candidate passwords contained in this repository is meant to be used on Web Security Academy's Authentication labs and is likely to be useless in other contexts.</p>

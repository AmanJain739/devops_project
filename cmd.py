#!/usr/bin/python3

import time
import cgi
import subprocess
import os

print("Content-Type: text/html") 
print("") 

print("<h1>Hello World..</h1>")

data="""
<html>
    <h1>  Hye Docker  </h1>
    <form>

    <input placeholder="Enter Username"> <br>
    <input placeholder="Enter Password"> <br>
    <input type="submit">
    </form>
</html>
"""
print(data)
ox=subprocess.getoutput('date')
print("<h2>",ox,"</h2>")

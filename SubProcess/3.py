#!/bin/python3

import subprocess

cmd='java -version'
sp=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

rc=sp.wait()
o,e=sp.communicate()

if rc==0:
    if bool(o) ==False  and bool(e):
        print(e.splitlines()[0].split('"')[1])

else:
    print(e)


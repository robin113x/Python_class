#!/bin/python3
import subprocess

cmd='bash --version'.split()

sp=subprocess.Popen(cmd,shell=False,stdout=subprocess.PIPE,stderr=subprocess.PIPE,universal_newlines=True)

rc=sp.wait()
out,err=sp.communicate()

l1=out.splitlines()
if rc==0:
    for eachline in l1:
        if 'version' and 'release' in eachline:
            print(eachline.split()[3].split('(')[0])


else:
    print('sorry babu')


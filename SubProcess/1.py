#!/bin/python3
'''
syntax
cmd='ls -ltr'
s=subprocess.Popen(cmd,shell=True,stdout=subprocess.PIPE,stderr=subprocess,subprocess.PIPE,universal_newlines=True)
'''
import subprocess

#cmd = 'ls -ltr'
cmd = ['ls','-l']

sp = subprocess.Popen(
    cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
rc = sp.wait()
out, err = sp.communicate()
print(f'The Return code {rc}')
print(out)
print(err)

l1=out.splitlines()
print(l1)


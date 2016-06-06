# file: runme.py
import subprocess
import os

target = 'example'
cppfiles = '.cppfiles'
pyfiles = '.pyfiles'
os.makedirs(cppfiles, exist_ok=True)
os.makedirs(pyfiles, exist_ok=True)

kw = dict(target=target, cppfiles=cppfiles, pyfiles=pyfiles)
out, err = subprocess.Popen(['swig -c++ -python -outdir {pyfiles} -o {cppfiles}/{target}_wrap.cpp {target}.i'.format(**kw)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).communicate()
# Call our gcd() function

print('stdout:[\n{}\n]'.format(out.decode())) if out else None
print('stderr:[\n{}\n]'.format(err.decode())) if err else None

import example


x = 42
y = 105
g = example.gcd(x, y)
print("The gcd of %d and %d is %d" % (x, y, g))

# Manipulate the Foo global variable

# Output its current value
print("Foo = ", example.cvar.Foo)

# Change its value
example.cvar.Foo = 3.1415926

# See if the change took effect
print("Foo = ", example.cvar.Foo)

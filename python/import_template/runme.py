# file: runme.py
# Test various properties of classes defined in separate modules

print("Testing the %import directive with templates")
import base
import foo
import bar
import spam

# Create some objects

print("Creating some objects")

a = base.intBase()
b = foo.intFoo()
c = bar.intBar()
d = spam.intSpam()

# Try calling some methods
print("Testing some methods")
print("", end=' ')
print("Should see 'Base::A' ---> ", end=' ')
a.A()
print("Should see 'Base::B' ---> ", end=' ')
a.B()

print("Should see 'Foo::A' ---> ", end=' ')
b.A()
print("Should see 'Foo::B' ---> ", end=' ')
b.B()

print("Should see 'Bar::A' ---> ", end=' ')
c.A()
print("Should see 'Bar::B' ---> ", end=' ')
c.B()

print("Should see 'Spam::A' ---> ", end=' ')
d.A()
print("Should see 'Spam::B' ---> ", end=' ')
d.B()

# Try some casts

print("\nTesting some casts\n")
print("", end=' ')

x = a.toBase()
print("Should see 'Base::A' ---> ", end=' ')
x.A()
print("Should see 'Base::B' ---> ", end=' ')
x.B()

x = b.toBase()
print("Should see 'Foo::A' ---> ", end=' ')
x.A()

print("Should see 'Base::B' ---> ", end=' ')
x.B()

x = c.toBase()
print("Should see 'Bar::A' ---> ", end=' ')
x.A()

print("Should see 'Base::B' ---> ", end=' ')
x.B()

x = d.toBase()
print("Should see 'Spam::A' ---> ", end=' ')
x.A()

print("Should see 'Base::B' ---> ", end=' ')
x.B()

x = d.toBar()
print("Should see 'Bar::B' ---> ", end=' ')
x.B()

print("\nTesting some dynamic casts\n")
x = d.toBase()

print(" Spam -> Base -> Foo : ", end=' ')
y = foo.intFoo_fromBase(x)
if y:
    print("bad swig")
else:
    print("good swig")

print(" Spam -> Base -> Bar : ", end=' ')
y = bar.intBar_fromBase(x)
if y:
    print("good swig")
else:
    print("bad swig")

print(" Spam -> Base -> Spam : ", end=' ')
y = spam.intSpam_fromBase(x)
if y:
    print("good swig")
else:
    print("bad swig")

print(" Foo -> Spam : ", end=' ')
y = spam.intSpam_fromBase(b)
if y:
    print("bad swig")
else:
    print("good swig")

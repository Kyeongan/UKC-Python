## Versions check

$ python -V
Python 3.6.5 :: Anaconda, Inc.
$ python3 -V
Python 3.7.0
$ which python3
/Library/Frameworks/Python.framework/Versions/3.7/bin/python3





# Python source code
$ python3 hello.py Karl
Hello there Karl
$ ./hello.py Alice  ## without needing 'python' first (Unix)
Hello there Alice








$ python3        ## Run the Python interpreter
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 6       ## set a variable in this interpreter session
>>> a           ## entering an expression prints its value
6
>>> a + 2
8
>>> a = 'hi'    ## 'a' can hold a string just as well
>>> a
'hi'
>>> len(a)      ## call the len() function on a string
2
>>> a + len(a)  ## try something that doesn't work
Traceback (most recent call last):
  File "", line 1, in
TypeError: cannot concatenate 'str' and 'int' objects
>>> a + str(len(a))  ## probably what you really wanted
'hi2'
>>> foo         ## try something else that doesn't work
Traceback (most recent call last):
  File "", line 1, in
NameError: name 'foo' is not defined
>>> ^D          ## type CTRL-d to exit (CTRL-z in Windows/DOS terminal)

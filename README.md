# Overview

## This software is only to be used on your personal equipment. __Not For Illegal Use!!__

Keylogger.py records the input typed into the computer that it is installed on and writes the inputs
to a keylog.txt file in the same directory that the keylogger is run from. Whole words are written
to the keylog.txt file so that it is easier to read.

This was my introduction to keyloggers and an opportunity to learn more about cybersecurity tools
and Python.

[Software Demo Video](https://youtu.be/koITmz3x4Ec)


# How to Use

Install: keyboard and thread libraries

`pip install keyboard thread`

Administrative privileges are needed to run keylogger.py. I have only tested it on a Linux
system. Windows may need Window's Defender turned off or an exception added. Once started
the keylogger will continually capture keys until turned off by pressing the escape key
from anywhere not just from the terminal. Open keylog.txt to view recorded keys.

# Development Environment

- Written using python 3
  - Inputs handled with boppreh's keyboard library.
  - Timing was accomplished using the Timing class from the Threaded library.


# Useful Websites

{Make a list of websites that you found helpful in this project}
* [CYBR/how-i-made-a-python-keylogger-that-sends-emails](https://cybr.com/cybersecurity/how-i-made-a-python-keylogger-that-sends-emails/)
* [Python keyboard library](https://github.com/boppreh/keyboard#keyboard.wait)

# Future Work

* Handle capitals being formatted into the keylog.txt file.
* Give user option to choose where keylog.txt is saved.
* Enable option to automatically send keylog.txt to email.

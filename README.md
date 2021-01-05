This is a simple keylogger for Bash commands. It uses the `trap` built-in to trap the DEBUG pseudo-signal, and sends the command to a remote HTTP server.

## Purpose
This can be used to log Bash history to a remote server, for auditing purposes.

## Bash
The file `shell.sh` contains Bash to be put in `.bashrc`, `.bash_profile`, or any of the other files that are eval'd by the shell when a new shell is opened. Be sure to change the IP address to the correct IP address of your logging server.

## Log Server
The file `catcher.py` contains a simple Flask app that saves keylogs to a log file.
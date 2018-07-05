#!/usr/bin/env python
import sys
import socket
import psutil
sys.stdout = open('output.txt','a')
print('{0} {1}' .format(socket.gethostname(), psutil.virtual_memory()))

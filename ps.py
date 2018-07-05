#!/usr/bin/env python
import sys
import socket
import psutil
sys.stdout = open('output.txt','a')
print('Host: {0} Memory: {1}' .format(socket.gethostname(), psutil.virtual_memory()))


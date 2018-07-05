#!/usr/bin/env python
import sys
import socket
import psutil
sys.stdout = open('output.txt','a')
print(socket.gethostname())
print(psutil.virtual_memory())

#coding:utf-8
from socket import *
import sys,time
import threading

class party():
    max_length = 1024
    received_meg = []
    Host = ''
    Port = 50025

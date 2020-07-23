#!/usr/bin/python
from helper import Block
import requests

server_tmp_file = '/tmp/url_checker'
server_endpoint = 'http://127.0.0.1:5000/block'
server_delete_endpoint= 'http://127.0.0.1:5000/block_delete'


def out():
    try:
        with open(server_tmp_file,'r') as f:
            print(f.read())
    except:
        print('')

def leftclick():
    requests.get(server_endpoint)

def rightclick():
    requests.get(server_delete_endpoint)

b = Block(out,leftcmd=leftclick,rightcmd=rightclick)
b()

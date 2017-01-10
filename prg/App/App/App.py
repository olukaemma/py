#!/usr/bin/env python3
#
#Author: Emmanuel Oluka
#Date: 1-10-17
#This program so suppossed to access netapp storage and perform specific tasks as defined by the user
#
#
__doc__
"""
This program is supposed to execute within its own console but also
Be able to interact with the users, accepting input.
The program used cmd, and paramiko ssh module

Tasks performed by the storage admin
1. Create cifs shares
2. Create NFS volumes and mount them:
    This process involves creating the nfs exports, and mounting it to the unix host
3. Create volumes
4. Resize volumes
5. Add disk and assign the disk ownership
"""
#import modules
import sys
import cmd
import paramiko
import os

#Core FrameWork Class
class FrameWork(cmd.Cmd):
    '''define the prompte, to execute the commands in'''
    promot = 'shell>'
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.host = []
        self.connection = []
        self.client = []

    def do_add_host(self, args):
        '''Add the host to be connected to via ssh'''
        print('please Enter the <hostname>,<username>')
        passwd = input(print('Passowrd: '))
        if args:
            self.host.append(split(','))
        else:
            print('Usage: host')

    def do_connect(self, args):
        '''Use Paramiko, to connect to the host using ssh'''
        for host in self.host:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            client.connect(host[0],username=host[1],password=host[2])


if __name__ == 'main':
    FrameWork().cmdloop() #Loop the program untill exited
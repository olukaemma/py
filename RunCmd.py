#!/usr/bin/env python3
#
#Scipt, to perform ssh and execute commands using the paramiko module
#Author: Emmanuel Oluka
#Date: 01/04/2017:11:00AM
#
#---Requirement---
'''
The paramiko module is required to execute this script
Please install the paramiko module using the pip
pip install prarmiko
'''
#function to connect to any ssh client and execute commands
#import pip
import sys
import paramiko
import cmd

class RunCommand(cmd.Cmd):
    """Simple Shell to run a command on the host"""
    prompt='ssh>'
    def __init__(self):
	    cmd.Cmd.__init__(self)
	    self.host = []
	    self.connections = []
		
    def do_add_host(self, args):
        if args:
            self.host.append(args.split(','))
        else:
            print ("Usage: host")
		
    def do_connect(self, args):
        """Connect to all the hosts in the host list"""
        for host in self.host:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host[0], username=host[1], password=host[2])
            self.connections.append(client)

    def do_run(self, command):
        '''Execute the commands function'''
        if command:
            for host, conn in zip(self.host, self.connections):
                stdin,stdout,stderr = conn.exec_command(command)
                stdin.close()
                for line in stdout.read().splitlines():
                    print('host: %s: %s' %(host[0],line))
        else:
            print ('Usage: run')

    def do_cls(self, args):
        '''This function, just clears the content of the screen'''
        import os
	if args:
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')

    def do_close(self, args):
        '''close the ssh connection'''
        for conn in self.connections:
            conn.close()

if __name__ == '__main__':
    RunCommand().cmdloop()

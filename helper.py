from sys import argv
import subprocess
from os import environ,chdir
from pathlib import Path


blocks_dir = Path.home() / 'Scripts' / 'Blocks'
def change_working_dir():
    chdir(blocks_dir)

def open_with_less(f,*args,**kwargs):
    cmd = ['less','-Srf']
    run_on_term(cmd+[f],*args,**kwargs)

def run_on_term(command,font=None,window_class=None):
    full_cmd = ['setsid', '-f', environ['TERMINAL']]
    if window_class:
        full_cmd += ['-c',window_class]
    if font:
        full_cmd += ['-f',font]
    full_cmd += command
    subprocess.Popen(full_cmd,stderr=subprocess.DEVNULL)

def clickable(func):
    def clickable_wrapper():
        try:
            argv[1]
        except:
            return func(None)
        button = int(argv[1])
        #If block has been right clicked, lauch editor with source code
        if button == 3:
            open_source_code() 
        return func(button)
    return  clickable_wrapper

def open_source_code():
    run_on_term([environ['EDITOR'],argv[0]])




class Block:
    def __init__(self, out, noclick=None, leftcmd=None, midcmd=None,rightcmd=open_source_code):
        self.out = out
        self.leftcmd = leftcmd
        self.midcmd = midcmd
        self.rightcmd = rightcmd
        self.noclick = noclick
        try:
            self.button = int(argv[1])
        except:
            self.button=None

    def __call__(self):
        if self.button is None:
            if self.noclick:
                self.noclick()
        elif self.button == 1:
            if self.leftcmd:
                self.leftcmd()
        elif self.button==2:
            if self.midcmd:
                self.midcmd()
        elif self.button == 3:
            self.rightcmd()
        print(self.out())

if __name__ == '__main__':
    pass

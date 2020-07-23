#!/usr/bin/python
from helper import clickable, run_on_term, change_working_dir
import subprocess

def leftclick():
    run_on_term(['neomutt'])
def noclick():
    subprocess.run(['./mail_reporter.sh'])

@clickable
def main(button):
    if button == 1:
        leftclick()
    noclick()

change_working_dir()
main()

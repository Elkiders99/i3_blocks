#!/usr/bin/python

from helper import Block,run_on_term, open_with_less
import subprocess
from pathlib import Path
from tempfile import NamedTemporaryFile


tmp_file = Path('/tmp/cal.py')


def onleftclick():
    with open(tmp_file,'w') as f:
        f.write(subprocess.check_output(['cal','-3']).decode())
    open_with_less(tmp_file,window_class='Calendar')


def output():
    return subprocess.check_output(['date', '+"%a, %d-%m %b"']).decode()


block = Block(output,leftcmd=onleftclick)
block()


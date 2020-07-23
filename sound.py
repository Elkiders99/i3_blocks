#!/usr/bin/python
import subprocess
from helper import clickable,run_on_term

def noclick():
    my_sinks = {'alsa_output.usb-Kingston_HyperX_7.1_Audio_00000000-00.analog-stereo':"🎧", 'alsa_output.pci-0000_00_1b.0.analog-stereo':"🔊"}
    vol=subprocess.run(['pulsemixer', '--get-volume'], text=True,stdout=subprocess.PIPE).stdout.split()[0]

    info=subprocess.run(['pactl', 'info'],text=True,stdout=subprocess.PIPE)
    for line in info.stdout.split('\n'):
        if 'Default Sink: ' in line:
            current_default_sink = line.split()[2]
            break
    print(my_sinks[current_default_sink],vol,"%")

def leftclick():
    run_on_term(['pulsemixer'])

@clickable
def main(button):
    if button == 1:
        leftclick()
    noclick()
main()

#!/bin/bash

'''
Hard delete to free disk space.
'''

rm -f $HOME/pcap/*
rm -f $HOME/txt/*
sudo rm -f $HOME/.local/share/Trash/files/*

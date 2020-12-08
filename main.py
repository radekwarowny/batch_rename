#!/usr/bin/env python

# batch_rename.py
# Created: 8th Dec 2020

"""This script will rename a group of files in given directory"""

__author__ = 'Radek Warowny'
__version__ = '1.0'


import glob
import os
import sys
from pathlib import Path

home_dir = str(Path.home())
current_dir = os.getcwd()
path = home_dir


def interface(home, curr):

    os.system('clear')  # clear terminal screen

    print("\n\t\t\tBATCH FILE RENAME")
    print("\t\t\t PRESS Q TO QUIT\n")
    print("HOME DIR: ", home)
    print("CURRENT DIR: ", curr)


def logic(home, curr):
    directory = input("\nWORK FROM (C)URRENT OR (H)OME DIR: ")
    if curr != home:
        if directory.upper() == 'Q':
            sys.exit()
        elif directory.upper() == 'C':
            os.chdir(curr)
            contents()
        elif directory.upper() == 'H':
            os.chdir(home)
            contents()
        else:
            print("INPUT ERROR")
            logic(home, curr)


def contents():
    content = input("\nLIST CONTENT (Y/N): ")
    if content.upper() == 'Q':
        interface()
    elif content.upper() == 'Y':
        contents = sorted([f for f in os.listdir('./') if not f.startswith('.')], key=str.lower)
        for item in contents:
            if os.path.isfile(item):
                print(item)
            else:
                print("../" + item)
    elif content.upper() == "N":
        pass
    else:
        try:
            interface(home_dir, current_dir)
        except TypeError:
            print("INPUT ERROR")
            interface(home_dir, current_dir)

    path = os.getcwd()

    while not os.path.isfile(path):

        path = input("\nFILE OR FOLDER NAME: ../")
        if path.upper() == 'Q':
            interface(home_dir, current_dir)
        elif os.path.isfile(path):
            extension = input("FILE EXT TO RENAME: ")
            file_name = ''
            for file in glob.glob("*.{}".format(extension)):
                print(file)
                file_name = file
            change = input("CHANGE FILE NAME TO: ")
            file_split = file_name.split(".")

            extension = str(file_split[1])
            n = 1
            for file in glob.glob("*.{}".format(extension)):
                os.rename(file,"{}_{}.{}".format(change, n, extension))
                n += 1
            print("FILES RENAMED")
            sys.exit()
        try:
            os.chdir(os.getcwd() + "/{}".format(path))
        except FileNotFoundError:
            print("INPUT ERROR")

        if content == 'file':
            extension = input("FILE EXT TO RENAME: ")
            for file in glob.glob("*.{}".format(extension)):
                print(file)
        elif content == 'y':
            os.system('clear')
            contents = sorted([f for f in os.listdir('./') if not f.startswith('.')], key=str.lower)
            for item in contents:
                if os.path.isfile(item):
                    print(item)
                else:
                    print("../" + item)


interface(home_dir, current_dir)
logic(home_dir, current_dir)

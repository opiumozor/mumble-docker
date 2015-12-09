#
#
# Filename: start.py
# Description: Starting script for mumble-docker.
#
# Author: Alexis Bernard
# Email: alexis.bernard33@gmail.com
#
# Created: Tue Dec  8 21:38:46 2015 (+0100)
# Last-Updated: Wed Dec  9 19:09:58 2015 (+0100)
#           By: Alexis Bernard
#     Update #: 25
#
#

import os
import subprocess

def generate_config():
    """
    """
    # check env variable and set default cfg
    try:
        welcometext = os.environ['SERVER_MSG']
    except KeyError:
        welcometext = "Welcome!"
    try:
        serverpassword = os.environ['SERVER_PASSWORD']
    except KeyError:
        serverpassword = ""
    try:
        users = os.environ['MAX_USERS']
    except KeyError:
        users = 50
    try:
        registername = os.environ['CHANNEL_NAME']
    except KeyError:
        registername = "Mumble server"
    # generate config to write
    config = open("mumble-server.ini", "r")
    config = config.read()
    config = config.format(WELCOMETEXT=welcometext,
                           SERVERPASSWORD=serverpassword,
                           USERS=users,
                           REGISTERNAME=registername)
    # write generated config to config file
    with open("mumble-server.ini", "w") as inifile:
        inifile.write(config)

def start_server():
    """
    """
    try:
        supassword = os.environ['SU_PASSWORD']
    except KeyError:
        supassword = None
    if supassword != None:
        subprocess.call(["/usr/sbin/murmurd",
                         "-ini", "/mumble/mumble-server.ini",
                         "-supw", supassword])
    subprocess.call(["/usr/sbin/murmurd",
                     "-fg",
                     "-ini", "/mumble/mumble-server.ini"])

if __name__ == '__main__':
    generate_config()
    start_server()

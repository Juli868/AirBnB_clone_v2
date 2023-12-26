#!/usr/bin/python3
import os
from fabric.api import local

def do_deploy(archive_path):
    if os.path.isdir(archive_path) is False:
        return False

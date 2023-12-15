#!/usr/bin/python3
"""Create a zip file."""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Create a .tgz zip file."""
    now = datetime.utcnow()
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file_name)).failed is True:
        return None
    return file_name

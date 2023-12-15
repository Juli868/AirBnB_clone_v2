#!/usr/bin/python3
"""Create a zip file."""
import tarfile
from fabric.api import local
import os
from datetime import datetime
import glob


def do_pack():
    """Create a .tgz zip file."""
    now = datetime.utcnow()
    file_name = f'versions/web_static_{now.year}{now.month}{now.date}'
    f'{now.hour}{now.minute}{now.seconds}.tgz'
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return filename

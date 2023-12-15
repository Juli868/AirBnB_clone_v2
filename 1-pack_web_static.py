#!/usr/bin/python3
"""Create a zip file."""
import tarfile
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
    with tarfile.open(file_name, 'w:gz') as new:
        files = glob.glob(os.path.join('web_static', '*'))
        for file_n in files:
            new.add(file_n, arcname=os.path.basename(file_n))
    return filename

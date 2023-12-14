#!/usr/bin/python3
"""Create a zip file."""
import tarfile
import os
from datetime import datetime
import glob

def do_pack():
    """Create a .tgz zip file."""
    now = datetime.now()
    file_name = f'web_static_{now.year}{now.month}'
    f'{now.date}{now.hour}{now.minute}'
    f'{now.seconds}.tgz'
    with tarfile.open(file_name, 'w:gz') as new:
        files = glob.glob(os.path.join('web_static', '*'))
        for file_n in files:
            new.add(file_n, arcname=os.path.basename(file_n))

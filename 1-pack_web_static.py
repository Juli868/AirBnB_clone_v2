#!/usr/bin/python3
"""Create a zip file."""
import tarfile
import os
from datetime import datetime


def do_pack():
    """Create a .tgz zip file."""
    now = datetime.now()
    file_name = f'web_static_{now.year}{now.month}{now.date}'\
    '{now.hour}{now.minute}{now.seconds}.tgz'
    with tarfile.open(file_name, 'w:gz') as new:
        files = glob.glob(os.path.join('web_static', '*'))
        for file_n in files:
            new.add(file_n, arcname=os.path.basement(file_n))

#!/usr/bin/python3
import os
from fabric.api import local,post,get

env.user = 'ubuntu'
env.hosts = ['54.160.86.207', '3.90.80.144']
env.key_filename = '~/.ssh/new'
def do_deploy(archive_path):
    file_name=list(achrive_path.split('/'))
    destination = '/data/web_static/releases/'
    if os.path.isdir(archive_path) is False:
        return False
    put(archive_path,'/tmp/')
    run('tar -xzvf {} -C {}'.format(file_name[-1], destination))

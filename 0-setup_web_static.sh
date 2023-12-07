#!/usr/bin/env bash
#preparing web servers
mkdir /data/
mkdir /data/web_static
mkdir /data/web_static/releases
mkdir /data/web_static/shared/
mkdir /data/web_static/releases/test/
touch /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown  -r ubuntu ubuntu /data

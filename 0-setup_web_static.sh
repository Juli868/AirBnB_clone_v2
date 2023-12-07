#!/usr/bin/env bash
#preparing web servers
sudo mkdir /data/
sudo mkdir /data/web_static
sudo mkdir /data/web_static/releases
sudo mkdir /data/web_static/shared/
sudo mkdir /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
ln -s /data/web_static/current /data/web_static/releases/test/
chown  -R ubuntu :ubuntu /data

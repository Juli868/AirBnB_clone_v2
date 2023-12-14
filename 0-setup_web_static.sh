#!/usr/bin/env bash
#preparing web servers
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "hello world!" > /data/web_static/releases/test/index.html
sudo ln -s /data/web_static/current /data/web_static/releases/test/
sudo chown  -R ubuntu:ubuntu /data
if grep -q "server{/n location /hbnb_static{/n alias /data/web_static/current/;/n }/n}" "/etc/nginx/sites-available/default";then
	true
else
	echo "server{
 location /hbnb_static{
 alias /data/web_static/current/;
 }
}" |sudo tee -a /etc/nginx/sites-available/default
fi
sudo systemctl restart nginx

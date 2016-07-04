sudo apt-get install nginx
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo apt-get install gunicorn
sudo ln -s /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.conf
sudo ln -s /home/box/web/etc/ask.conf /etc/gunicorn.d/ask.conf
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start﻿
mysql -u root -e "create database db_qa;"
mysql -u root -e "create user 'qa'@'localhost' identified by 'qa';"
mysql -u root -e "grant all privileges on *.* to 'qa'@'localhost';"
mysql -u root -e "flush privileges;"

sudo apt-get install nginx
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo apt-get install gunicorn
sudo ln -s /home/box/web/etc/hello.conf /etc/gunicorn.d/hello.conf
sudo /etc/init.d/gunicorn restart

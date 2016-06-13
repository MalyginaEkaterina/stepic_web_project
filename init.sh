sudo apt-get install nginx
mkdir home/box/web
mkdir home/box/web/public
mkdir home/box/web/public/img
mkdir home/box/web/public/css
mkdir home/box/web/public/js
mkdir home/box/web/uploads
mkdir home/box/web/etc
sudo ln -s /etc/nginx/nginx.conf /home/box/web/etc/nginx.conf
sudo nginx -s reload

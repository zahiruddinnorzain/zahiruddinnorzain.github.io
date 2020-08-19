#!/bin/bash

printf "=====bohttps V 1.2=====\n"
printf "Make sure you install nginx first\nkepaknaga@gmail.com\n"
printf "SHOW SSL VERSION\n"
sudo openssl version -a

printf "INSTALL OPENSSL\n"
printf "continue..\n"

printf "GENERATE SSL\n"
cd /etc/nginx/
sudo mkdir ssl
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/nginx/ssl/generated-private-key.key -out /etc/nginx/ssl/generated-csr.crt

printf "=====PASTE THIS IN NGINX SITES-AVAILABLE FILE=====\n"
# printf "ssl_certificate /etc/nginx/ssl/generated-csr.crt"
# printf "ssl_certificate_key /etc/nginx/ssl/generated-private-key.key"

cd /home/ubuntu/
sudo wget https://raw.githubusercontent.com/zahiruddinnorzain/zahiruddinnorzain.github.io/master/nginxtext.txt
sudo cat nginxtext.txt

printf "=====DONE, YOU CAN RUN YOUR SYMLINK COMMAND=====\n"
printf "Example: sudo ln -s /etc/nginx/sites-available/laravel /etc/nginx/sites-enabled/"
printf " \n"

sudo apt-get update

# stop apache2
sudo service apache2 stop
sudo systemctl disable apache2

# curl
sudo apt install curl

# git
sudo apt install git
git config --global user.name "zahiruddin"
git config --global user.email "kepaknaga@gmail.com"

# gcc
sudo apt-get -y install gcc

# postgres
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install postgresql-12

# nginx
sudo apt-get -y install nginx

# laravel
sudo apt-get update
sudo apt -y install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt -y install php7.4
php -v
sudo apt-get install -y php7.4-cli php7.4-curl php7.4-gd php7.4-json php7.4-mbstring php7.4-intl php7.4-mysql php7.4-xml php7.4-zip php7.4-pgsql php7.4-fpm
sudo apt install composer

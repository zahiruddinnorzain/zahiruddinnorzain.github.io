printf "===== bodeploy V3.4 =====\n"
# 28 july 2020 by zahiruddin

# stop nginx
sudo service nginx stop
printf "STOP NGINX SERVICE\n"

cd ssipr-php-laravel
sudo cp .env ../.env
sudo git checkout .
sudo git pull
sudo git status
sudo cp ../.env .env
printf "DONE UPDATE REPO AND ENV FILE\n"

sudo composer install
printf "DONE COMPOSER INSTALL\n"

sudo composer dumpautoload
# php artisan migrate:fresh
# php artisan db:seed
php artisan passport:install
php artisan storage:link
sudo chmod -R 777 storage
printf "DONE CONFIGURATION ARTISAN\n"

printf "CLEARING CACHE\n"
sudo php artisan config:cache

printf "STARTING NGINX SERVICE\n"
sudo service nginx start

# printf "Please edit .env file\n"
# printf "then, start your NGINX\n"
printf "===== ALL DONE =====\n"


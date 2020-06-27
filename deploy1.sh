# stop nginx
sudo service nginx stop
printf "STOP NGINX SERVICE\n"

cd ssipr-php-laravel
cat .env
sudo git checkout .
sudo git pull
sudo git status
printf "Done Update Repo\n"

sudo composer install 
printf "Done composer install\n"

sudo cp .env.example .env
printf "Done copy env file\n"

printf "Please edit .env file\n"
printf "then, start your NGINX\n"
printf "END\n"

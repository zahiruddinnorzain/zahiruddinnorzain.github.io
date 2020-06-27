printf "STARTING DEPLOYMENT PHASE 2\n"
cd ssipr-php-laravel
sudo composer dumpautoload
php artisan migrate:fresh
php artisan db:seed
php artisan passport:install
php artisan storage:link
sudo chmod -R 777 storage
printf "done run file\n"

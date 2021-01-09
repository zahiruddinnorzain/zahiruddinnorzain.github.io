# https://www.digitalocean.com/community/tutorials/how-to-secure-nginx-with-let-s-encrypt-on-ubuntu-18-04
# renew command     sudo certbot renew --dry-run
sudo apt-get update
sudo add-apt-repository ppa:certbot/certbot
sudo apt install python-certbot-nginx
sudo cp /etc/nginx/sites-available/laravel /etc/nginx/sites-available/laravel.bkp
echo '##### choose option 2'
echo 'sudo certbot --nginx -d domain.gov.my'


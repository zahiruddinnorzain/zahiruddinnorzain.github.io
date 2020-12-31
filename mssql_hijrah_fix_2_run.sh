# https://medium.com/@nahomt/using-sql-server-from-your-php-apps-on-ubuntu-16-04-c85671249c45

echo '####### RUNNING #######'

sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install msodbcsql17
sudo apt-get install unixodbc-dev mssql-tools

sudo ln -s /etc/php/7.3/mods-available/sqlsrv.ini /etc/php/7.3/cli/conf.d/20-sqlsrv.ini

sudo ln -s /etc/php/7.3/mods-available/pdo_sqlsrv.ini /etc/php/7.3/cli/conf.d/20-pdo_sqlsrv.ini

sudo ln -s /etc/php/7.3/mods-available/sqlsrv.ini /etc/php/7.3/fpm/conf.d/20-sqlsrv.ini

sudo ln -s /etc/php/7.3/mods-available/pdo_sqlsrv.ini /etc/php/7.3/fpm/conf.d/20-pdo_sqlsrv.ini

sudo service php7.3-fpm restart
sudo service nginx restart
echo '####### DONE #######'

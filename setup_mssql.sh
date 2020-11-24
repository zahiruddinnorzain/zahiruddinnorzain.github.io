echo "### installing mssql server"
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/18.04/mssql-server-2019.list)"
sudo apt-get update
sudo apt-get install -y mssql-server

sudo /opt/mssql/bin/mssql-conf setup

systemctl status mssql-server --no-pager

echo "### installing mssql driver"
sudo apt install php-pear
sudo add-apt-repository ppa:ondrej/php
sudo apt-get update
sudo apt-get install php7.3-dev

sudo apt-get install unixodbc-dev
sudo pecl install sqlsrv
sudo pecl install pdo_sqlsrv
sudo su
printf "; priority=20\nextension=sqlsrv.so\n" > /etc/php/7.3/mods-available/sqlsrv.ini
printf "; priority=30\nextension=pdo_sqlsrv.so\n" > /etc/php/7.3/mods-available/pdo_sqlsrv.ini
exit
sudo phpenmod -v 7.3 sqlsrv pdo_sqlsrv
echo "### DONE"

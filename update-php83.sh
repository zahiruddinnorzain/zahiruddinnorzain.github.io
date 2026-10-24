#!/usr/bin/env bash

set -Eeuo pipefail

PHP_VERSION="8.3"
PHP_FPM_SERVICE="php${PHP_VERSION}-fpm"
LOG_FILE="update-php83-$(date +%Y%m%d-%H%M%S).log"

# Log output to both terminal and file.
exec > >(tee -a "$LOG_FILE") 2>&1

trap 'rc=$?; echo "[ERROR] Script failed at line ${LINENO} (exit ${rc}). Check log: ${LOG_FILE}"; exit "$rc"' ERR

echo "=================================================="
echo " PHP ${PHP_VERSION} Update"
echo " Started: $(date)"
echo " Log: ${LOG_FILE}"
echo "=================================================="

# Require root privileges through sudo.
if [[ $EUID -eq 0 ]]; then
    SUDO=""
else
    SUDO="sudo"
fi

echo
echo "[1/8] Current PHP version"
php -v

echo
echo "[2/8] Check Ubuntu version"
cat /etc/os-release

echo
echo "[3/8] Install software-properties-common"
$SUDO apt install -y software-properties-common

echo
echo "[4/8] Add Ondrej PHP PPA"
if ! $SUDO add-apt-repository -y ppa:ondrej/php; then
    echo "[ERROR] Failed to add PPA."
    echo "Check network, proxy and Launchpad connectivity."
    exit 1
fi

echo
echo "[5/8] Update APT package lists"
$SUDO apt update

echo
echo "[6/8] Find installed PHP ${PHP_VERSION} packages"
mapfile -t PHP_PACKAGES < <(
    dpkg-query -W -f='${binary:Package}\n' 2>/dev/null \
        | grep -E '^php8\.3($|-|:)' \
        || true
)

if [[ ${#PHP_PACKAGES[@]} -eq 0 ]]; then
    echo "[ERROR] No installed PHP ${PHP_VERSION} packages found."
    exit 1
fi

printf 'Packages to upgrade:\n'
printf '  %s\n' "${PHP_PACKAGES[@]}"

echo
echo "[7/8] Upgrade installed PHP ${PHP_VERSION} packages only"
$SUDO apt --only-upgrade install -y "${PHP_PACKAGES[@]}"

echo
echo "[8/8] Verify PHP and restart PHP-FPM"
php -v

if ! systemctl cat "$PHP_FPM_SERVICE" >/dev/null 2>&1; then
    echo "[ERROR] Service ${PHP_FPM_SERVICE} was not found."
    exit 1
fi

$SUDO systemctl restart "$PHP_FPM_SERVICE"
$SUDO systemctl is-active "$PHP_FPM_SERVICE"

echo
echo "=================================================="
echo " PHP UPDATE COMPLETED"
echo " Finished: $(date)"
echo " Log: ${LOG_FILE}"
echo "=================================================="

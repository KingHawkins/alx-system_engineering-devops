#!/usr/bin/env bash
sudo apt -y update
sudo apt -y upgrade
sudo apt -y install software-properties-common
sudo add-apt-repository -y universe
sudo add-apt-repository -y ppa:certbot/certbot
sudo apt -y install certbot

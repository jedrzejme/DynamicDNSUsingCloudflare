<h1 align = 'center'>
    <img 
        src = '/assets/icon.png' 
        height = '200' 
        width = '200' 
        alt = 'Icon' 
    />
    <br>
    Dynamic DNS using Cloudflare
    <br>
</h1>

<div align = 'center'>
    <a href = 'https://github.com/jedrzejme/DynamicDNSUsingCloudflare/tags'>
        <img src = 'https://img.shields.io/github/v/tag/jedrzejme/DynamicDNSUsingCloudflare?style=for-the-badge&label=version'/>
    </a>
    <a href = 'https://github.com/jedrzejme/DynamicDNSUsingCloudflare/issues'>
        <img src = 'https://img.shields.io/github/issues/jedrzejme/DynamicDNSUsingCloudflare?style=for-the-badge'/>
    </a>
    <a href = 'https://github.com/jedrzejme/DynamicDNSUsingCloudflare/pulls'>
        <img src = 'https://img.shields.io/github/issues-pr/jedrzejme/DynamicDNSUsingCloudflare?style=for-the-badge'/>
    </a>
</div>

<br>

**What is this?** Simple script written in python that allows you to assign domain to changing IP address.

**How to use it?**
* **Using Python:** firstly, you need to install [Python](https://www.python.org/downloads/). After that you need to edit config file (paste API key, zone ID, and define other variables whoever you want), then just run python file called "main.py". If you want to run it automatically every now and then - set "autorun" to "True" in "config.ini", if you want to just run it one time - set "autorun" to "False" in "config.ini".
* [**Using docker-compose**](https://github.com/jedrzejme/DynamicDNSUsingCloudflare/#using-docker-compose-to-run-dynamic-dns-using-cloudflare)

**What did I use?**
* [Python](https://www.python.org/)
* [Python libraries](/requirements.txt)
* [Docker](https://www.docker.com/)
* [Cloudflare API](https://developers.cloudflare.com/api/)
* [Getting IP Address](https://www.ipify.org/)
* [Coding](https://code.visualstudio.com/)
* [Git management](https://desktop.github.com/)

## Using docker-compose to run Dynamic DNS using Cloudflare
1) Install docker and docker-compose
2) Create new directory called however you want
3) Create docker-compose.yml file in the created directory and paste this inside the file:
```
version: '3'
services:
  dynamic-dns-using-cloudflare:
    image: jedrzejme/dynamic-dns-using-cloudflare
    container_name: dynamic-dns-using-cloudflare
    volumes:
      - ./config.ini:/config.ini
    restart: always
```
4) Create config.ini file in the same directory and paste this inside the file:
```
[main]
autorun = 
interval = 
time_unit = 
api_token = 
zone_identifier = 
domain = 
name = 
ttl = 
proxied = 
```
5) Edit config.ini according to [wiki](https://github.com/jedrzejme/DynamicDNSUsingCloudflare/wiki/Config-File)

6) Run docker-compose in the same directory:
```
docker-compose up -d
```
7) It works!

## Features
* Assigning domain to changing IP address using Cloudflare DNS records
* Running every now and then defined by user
* Config file; learn more in the [wiki](https://github.com/jedrzejme/DynamicDNSUsingCloudflare/wiki/Config-File)

## Purpose
Assigning domain to changing IP address. Changing IP address is commonly occurring at home.

## Other informations
This project is not created by Cloudflare Inc., but it uses Cloudflare Inc. API to edit DNS zones.

## Support
<p><a href="https://www.buymeacoffee.com/jedrzejme"> <img align="left" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="jedrzejme" /></a><a href="https://ko-fi.com/jedrzejme"> <img align="left" src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" height="50" width="210" alt="jedrzejme" /></a></p><br><br><br>
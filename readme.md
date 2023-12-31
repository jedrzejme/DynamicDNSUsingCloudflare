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
    <a href = 'https://github.com/jedrzejme/DynamicDNSUsingCloudflare/issues'>
        <img src = 'https://img.shields.io/github/issues/jedrzejme/DynamicDNSUsingCloudflare'/>
    </a>
    <a href = 'https://github.com/jedrzejme/DynamicDNSUsingCloudflare/pulls'>
        <img src = 'https://img.shields.io/github/issues-pr/jedrzejme/DynamicDNSUsingCloudflare'/>
    </a>
</div>

<br>

**What is this?** Simple script written in python that allows you to assign domain to changing IP address.

**How to use it?** Firstly, you need to install [Python](https://www.python.org/downloads/). After that you need to edit config file (paste API key, zone ID, and define other variables whoever you want), then just run python file called "main.py". If you want to run it automatically every now and then - set "autorun" to "True" in "config.ini", if you want to just run it one time - set "autorun" to "False" in "config.ini".

**What did I use?**
* [Python libraries](/requirements.txt)
* [Cloudflare API](https://developers.cloudflare.com/api/)
* [Getting IP Address](https://www.ipify.org/)
* [Coding](https://code.visualstudio.com/)
* [Git management](https://desktop.github.com/)

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
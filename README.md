# GoDaddy-Dynamic-DNS
Checks to see whether or not your public IP and the IP address for your domain's A record match.  If not the program will change your A record to match your public IP.

This program requires the use of the time, requests, and godaddypy python packages.  requests and godaddypy may need to be pip installed.

You will also need to obtain your own production API keys from GoDaddy.   https://developer.godaddy.com/keys/

Before running this program be sure to open it in an editor and add your api key, api secret, and domain where indicated.


Credit:

godaddypy was created by Julian Coy.  Github repo:  https://github.com/eXamadeus/godaddypy

requests Github repo:  https://github.com/requests/requests/

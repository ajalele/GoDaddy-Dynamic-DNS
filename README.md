# GoDaddy-Dynamic-DNS
Continually checks to see whether or not your public IP and the IP address for your domain's A record match.  If not the program will change your A record to match your public IP.

This program requires the use of the datetime, time, requests, and godaddypy python packages.  requests and godaddypy may need to be installed.

You will also need to obtain your own production API keys from GoDaddy.   https://developer.godaddy.com/keys/

When running this code you must give four arguments:

domain, api key, api secret, and how often (in seconds) you want to check

Example:

dynamicdns.py mysweetsite.com <api key> <api secret> 60

If you only want the program to run once and then stop use 0 as the fourth argument.


Credit:

godaddypy was created by Julian Coy.  Github repo:  https://github.com/eXamadeus/godaddypy

requests Github repo:  https://github.com/requests/requests/

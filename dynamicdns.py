import datetime, godaddypy, requests, time   # godaddpy was created by Julian Coy.  https://github.com/eXamadeus/godaddypy
from sys import argv


def dateandtime():  # Returns the current date and time in desired format.
    return datetime.datetime.now().strftime('%D  %H:%M:%S')


def godaddyapi(key, secret):  # Returns godaddy API Client object.
    a = godaddypy.Account(api_key=key, api_secret=secret)
    return godaddypy.Client(a)


def managedns(client, domain, repeatsec):  #  Gets your public IP address and compares it to your domain's A record IP address.  Changes A record to match if needed.
    while True:
        f = open('dynamicdns_stat.txt', 'a')
        try:
            r = requests.get(r'https://httpbin.org/ip')
            public_ip = r.json()['origin']
            dns_ip = client.get_records(domain, record_type='A')[0]['data']
            if  public_ip != dns_ip:
                client.update_ip(public_ip, domains=[domain])
                f.write('{} - DNS updated from {} to {}'.format(dateandtime(), dns_ip, public_ip,) + '\r\n')
                f.close()
            else:
                f.write('{} - No changes needed\r\n'.format(dateandtime()))  # This is optional.  If you don't want this feedback feel free to remove it.
                f.close()
            if repeatsec == 0:
                break
            time.sleep(repeat)  # This is the amount of time, in seconds, the program will wait before checking again.  Change this as you see fit.
        except (requests.ConnectionError, godaddypy.client.BadResponse) as e:
            if 'Response Data:' in str(e):
                print(e.args[0]['message'])
                f.write('{} - '.format(dateandtime()) + e.args[0]['message'] + '\r\n')
                f.close()
                break
            else:
                print('Cannot connect.  Trying agian in 10 seconds')
                f.write('{} - Cannot Connect\r\n'.format(dateandtime()))
                f.close()
                time.sleep(10)  # This is the amount of time, in seconds, the program will wait before trying to connect again.  Change this as you see fit.
                continue
        
        
if __name__ == '__main__':
    try:
        managedns(godaddyapi(argv[2], argv[3]), argv[1], int(argv[4]))
    except IndexError:
        print('\nNot enough arguments given.\n\nPlease use the following format:\n\ndynamicdns.py <domain> <api key> <api secret> <how often (in seconds) you want to check IP addresses>\n')

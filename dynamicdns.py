import datetime, godaddypy, time, requests  # godaddpy was created by Julian Coy.  https://github.com/eXamadeus/godaddypy


def dateandtime():  # Returns the current date and time in desired format.
    return datetime.datetime.now().strftime('%D  %H:%M:%S')


def godaddyapi():  # Returns godaddy API Client object.
    a = godaddypy.Account(api_key='<your godaddy api key>', api_secret='<your godaddy api secret>')
    c = godaddypy.Client(a)
    return c


def managedns(client, domain):  #  Gets your public IP address and compares it to your domain's A record IP address.  Changes A record to match if needed.
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
            time.sleep(60)  # This is the amount of time, in seconds, the program will wait before checking again.  Change this as you see fit.
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
    managedns(godaddyapi(), '<your domain>')

import time, requests
from godaddypy import Client, Account  # godaddpy was created by Julian Coy.  https://github.com/eXamadeus/godaddypy


def godaddyapi():  # Creates godaddy API client
    a = Account(api_key='<your godaddy api key>', api_secret='<your godaddy api secret>')
    c = Client(a)
    return c


def managedns(client, domain):  #  Gets your public IP address and compares it to your domain's A record IP address.  Changes A record to match if needed.
    while True:
        try:
            r = requests.get(r'https://httpbin.org/ip')
        except requests.ConnectionError:
            print('Cannot Connect')
        public_ip = r.json()['origin']
        dns_ip = client.get_records(domain, record_type='A')[0]['data']
        if  public_ip != dns_ip:
            client.update_ip(public_ip, domains=[domain])
            print('DNS updated from {} to {}'.format(dns_ip, public_ip))  # This is optional.  If you don't want this feedback feel free to remove it.
        else:
            print('No changes needed')  # This is optional.  If you don't want this feedback feel free to remove it.
        time.sleep(60)  # This is the amount of time, in seconds, the program will wait before checking again.  Change this as you see fit.
        
        
if __name__ == '__main__':
    managedns(godaddyapi(), '<your domain>')
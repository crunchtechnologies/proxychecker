import requests
from datetime import datetime

start = datetime.now()

proxies_list = []
good_proxies = 0
bad_proxies = 0

with open('working_proxies.txt', 'r') as file:
    proxies = file.read().splitlines()
    for proxy in proxies:
        proxies_list.append(proxy)
        
with open("proxies.txt", 'r') as file:
    proxies = file.read().splitlines()
    for proxy in proxies:
        print ("Trying proxy: " + proxy)
        url = 'https://httpbin.org/ip'
        try:
            response = requests.get(url, proxies = {'http': proxy, 'https': proxy}, timeout = 5)
            print ('Worked with ip %s' % proxy)
            if proxy in proxies_list:
                print ("Already done that one...")
            if proxy not in proxies_list:
                proxies_list.append(proxy)
                with open("working_proxies.txt", 'a+') as file:
                    file.write(proxy + '\n')
                    file.close()
                    good_proxies =+1
        except:
            print ("Bad proxy: %s" % proxy)
            bad_proxies =+1
            
with open("working_proxies.txt", 'a+') as file:
    file.write(proxy + '\n')

print ('Finished with the following stats: ')
print ('Good Proxies: %s' % str(good_proxies))
print ('Bad Proxies: %s' % str(bad_proxies))
print ('Total checked proxies: %s' % str(good_proxies + bad_proxies))
print ('Total time elapsed: %s' & str(datetime.now() - start))

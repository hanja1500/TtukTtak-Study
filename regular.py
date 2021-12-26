import re

strin = {}
check = cnt = 0

file_name_read = input("[*] Input your address file's absolute path > ")
file_take = open(file_name_read, 'r')

while True:
    line = file_take.readline()
    if not line:
        break
    strin[cnt] = str(line)
    cnt += 1

check = cnt
cnt = 0

eth = re.compile('^0x[a-f0-9]{20,40}')
btc = re.compile('^[a-z0-9]{20,50}')
rip = re.compile('^r[a-zA-Z0-9]{20,40}')

while cnt < check:
    btc_check = btc.findall(strin[cnt])
    rip_check = rip.findall(strin[cnt])
    eth_check = eth.findall(strin[cnt])
    if btc_check:
        if eth_check:
            print("[*] %s is etherium" % eth_check)
            cnt += 1
            continue
        print("[*] %s is bitcoin" % btc_check)
    elif rip_check:
        print("[*] %s is ripple" % rip_check)
    else:
        pass
    cnt += 1
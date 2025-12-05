import sys

ip_address = sys.argv[1].split('.')

changed_ip_1 = 0
changed_ip_2 = ''
power = 3

for octet in ip_address:
    changed_ip_1 += int(octet) * 256**power
    power -= 1
changed_ip_2 = f'0{changed_ip_1:o}'

sys.stdout.write(f'{changed_ip_1}\n')
sys.stdout.write(changed_ip_2)

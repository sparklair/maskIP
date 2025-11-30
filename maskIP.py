import sys

ip_address = sys.argv[1].split('.')

changed_ip = 0
power = 3

for octet in ip_address:
    changed_ip += int(octet) * 256**power
    power -= 1

sys.stdout.write(str(changed_ip))



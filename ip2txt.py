from ipaddress import IPv4Address as v4addr
from ipaddress import IPv6Address as v6addr
from ipaddress import IPv4Network as v4nw
from ipaddress import IPv6Network as v6nw
from random import randint

MAX_COUNT = 1990000
ipv4_percent = 0.4

ipdeny = [
]
ipv4_max = v4addr(u'224.0.0.0')._ip - 1
ipv4_min = v4addr(u'1.0.0.0')._ip

ipv4list = []
print 'get ipv4 list...'
for n in xrange(int(ipv4_percent*MAX_COUNT)):
  i = randint(ipv4_min, ipv4_max+1)
  ipv4 = v4addr(i)
  while (
    ipv4 in v4nw(u'127.0.0.0/8')
  ) or (
    ipv4 in v4nw(u'172.16.0.0/16')
  ) or (
    ipv4 in v4nw(u'192.168.0.0/16')
  ) or (
    ipv4 in v4nw(u'192.167.0.0/16')
  ) or (
    str(ipv4) in ipv4list
  ) or (
    str(ipv4) in ipdeny
  ):
    i = randint(ipv4_min, ipv4_max+1)
    ipv4 = v4addr(i)
  
  ipv4list.append(str(ipv4))
  if n % 10000 == 9999:
    print '%d' % (n+1)

if n % 10000 != 9999:
  print '%d' % (n+1)

f = open('v4.txt', 'w')
for ip in ipv4list:
  f.write(ip)
  f.write('\n')
f.close()

ipv6list = []
ipv6_max = v6addr(u'F000:FFFF:FFFF:FFFF::')._ip - 1
ipv6_min = v6addr(u'1::')._ip
print 'get ipv6 list...'
for n in xrange(int((1-ipv4_percent)*MAX_COUNT)):
  i = randint(ipv6_min, ipv6_max)
  ipv6 = v6addr(i)
  while (
    ipv6 in v6nw(u'1000::/48')
  ) or (
    str(ipv6) in ipv6list
  ) or (
    str(ipv6) in ipdeny
  ):
    i = randint(ipv6_min, ipv6_max)
    ipv6 = v6addr(i)

  ipv6list.append(str(ipv6))
  if n % 10000 == 9999:
    print '%d' % (n+1)

if n % 10000 != 9999:
  print '%d' % (n+1)

f = open('v6.txt', 'w')
for ip in ipv6list:
  f.write(ip)
  f.write('\n')

f.close()

# shoe_queue_stats.py

filename = 'notes/ipv4_int_bri.txt'

format = '%-25s  %16s'
with open(filename) as f:
    for lineno, line in enumerate(f,start=1):
        interface, ipaddr, status, protocol = line.split()
        if status == 'Up':
            print format % (interface, ipaddr)
    

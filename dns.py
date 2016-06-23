# dns.py
 
import json
 
filename = 'notes/dns_servers.json'
with open(filename) as f:
    servers = json.load(f)
    for server in servers['items']:
        if not server['primary']:
            print server['ip-address']
 
    

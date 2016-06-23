#rep_tetbed.py

from telnetlib import Telnet

ed191 = ('172.24.101.40', 2026)
ed192 = ('172.24.101.40', 2027)
ed193 = ('172.24.101.40', 2028)
ed194 = ('172.24.101.40', 2029)
ed195 = ('172.24.101.40', 2032)
ed196 = ('172.24.101.40', 2033)

rep_testbed = [ed191, ed192, ed193, ed194, ed195, ed196]

tn = Telnet(*ed194)
tn.write('\n')
print tn.read_all()

##for device in rep_testbed:
##    tn = Telnet(*device)
##    print tn.read_lazy()
##    tn.write('\n')
##    print tn.read_lazy()
##    tn.write('enable\n')
##    print tn.read_lazy()
##    tn.write('reload\n')
##    print tn.read_lazy()
##    tn.write('\n')
##    print tn.read_lazy()
##    tn.write('\n')
##    print tn.read_lazy()
##    tn.close()
    

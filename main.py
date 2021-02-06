import os
# this script sets raspberry Pi clock to 00.00 at every boot
os.system('sudo date -s "01 JAN 2000 00:00:00"')
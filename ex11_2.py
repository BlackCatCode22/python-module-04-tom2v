#Tong's Ch11.2 Code Up

import re
x = 'We just received $10.00 for cookies.'
stuff = re.findall('\\$[0-9.]+',x)
print(stuff)
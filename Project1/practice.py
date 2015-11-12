import re

str = '|  8 20 15 | | -16 -15 -13   2  20 |'

parts = re.findall(u'\|(.*?)\|',str)

s = re.search(u'\|(.*?)\|',str).groups()

print parts
print [i for i in s]
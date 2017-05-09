import re
import json

FILE = 'cesm.txt'
DEBUG = False

json_data = {}
raw_data = open(FILE, 'r')
for line in raw_data:
  if DEBUG:
    print line
  match = re.search('^(\d{2})\s(.*)', line)
  if match:
    json_data[match.group(1)] = { 'title' : match.group(2) }
  match = re.search('^(\d{2})(\d{2})\s(.*)', line)
  if match:
    json_data[match.group(1)][match.group(2)] = {'title': match.group(3) }
  match = re.search('^(\d{2})(\d{2})(\d{2})\s(.*)', line)
  if match:
    json_data[match.group(1)][match.group(2)][match.group(3)] = {'title': match.group(4) }
 
print json.dumps(json_data)

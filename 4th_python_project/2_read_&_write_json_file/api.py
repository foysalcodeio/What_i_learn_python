import json
from urllib.request import urlopen

with urlopen("http://api.plos.org/search?q=title:DNA") as response:
    source = response.read()

data = json.loads(source)

#print(json.dumps(data, indent=2))

for item in data['response']:
    print(item)




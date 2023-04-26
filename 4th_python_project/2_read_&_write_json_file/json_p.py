import json
from textwrap import indent

with open('areal.json') as f:
  data = json.load(f)

for state in data['area']:
    '''print(state['name'])'''
    del state['area_codes']

with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)


"""
people_string = '''
{
    "people" : [
        {
            "name": "foysal_ahammed",
            "phone": "01790-xxxxxx",
            "email": ["foysal@gmail.com"],
            "has_license": false
        },
        {
            "name": "forhad_ahammed",
            "phone": "01940-xxxxxx",
            "email": ["forhad@gmail.com"],
            "has_license": true
        }
    ]
}
'''
data = json.loads(people_string)

for person in data['people']:
    #print(person['name'])
    del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)
"""
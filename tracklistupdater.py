import json
import requests
tracklistjson = requests.get('https://raw.githubusercontent.com/polswert1/beatologer/refs/heads/main/tracklist.json').text
artistjson = requests.get('https://raw.githubusercontent.com/polswert1/beatologer/refs/heads/main/artist.json').text
b = dict(json.loads(tracklistjson))
z = dict(json.loads(artistjson))
x = json.loads('['+input('tracklist ')+']')
print(x)
y = input('albumid ')
g = input('artist ')
n = input('album ')+'::albumid_'+y
print(x)
newdict = {y:x}
b.update(newdict)
if g in z:
    z.setdefault(g,[]).append(n)
else:
    z.update({g:[n]})
bjson = json.dumps(b)
zjson = json.dumps(z)
print(b)
print(z)
print(bjson)
print(zjson)
if input('zapisz do pliku? y/n') == 'y':
    with open("tracklist.json", "w") as f:
        f.write(bjson)
    with open("artist.json", "w") as f:
        f.write(zjson)
else:
    pass
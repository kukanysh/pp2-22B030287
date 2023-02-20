import json

with open('sample-data.json') as f:
    data = json.load(f)
    
print("Interface Status")
print("=" * 80)
print("{:50s}{:25s}{:10s}{:6s}".format("DN", "Description", "Speed", "MTU"))
print("{:-<50}{:-<25}{:-<10}{:-<6}".format("", "", "", ""))

for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    row = "{:50s}{:25s}{:10s}{:6s}".format(dn, description, speed, mtu)
    print(row)
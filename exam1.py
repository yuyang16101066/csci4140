import re

string = "Tho chinose University of Hong Kong"
x = re.sub("o", "e", string, 2)
print(x)

'''string ="123.0.0.1"
pattern ="^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
m = re.search(pattern, string)
invalid = False
if m:
    for p in m.groups():
        if int(p) > 255:
            invalid = True
            print("Invalid IPv4 address: {} is greater than 255.".format(p))
            break
    if not invalid:
        print("Valid IPv4 address")
else:
    print("Invalid IPv4 address")'''

#Tong's Ch10 Code Up

fname = input('Enter file name: ')
if len(fname) < 1 : fname = 'clown.txt'

hand = open(fname)

many = dict()

for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # print(wds)
    for w in wds:
       many[w] = many.get(w,0) + 1

# Find the top 5 word by frequency

temp: dict()
newlist = list()
for k,v in many.items():
    tup = (v,k)
    newlist.append(tup)

cool = sorted(newlist, reverse = True)

for v,k in cool[:5]:
    print(k,v)



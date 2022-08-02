abc=322
efg="abc"
eitan= [32, "kuku", True , abc, efg]

for x in eitan:
    if isinstance(x,(int))  :
        print(x, end=" | ")

print("")

for x in eitan:
    if type(x) is int  :
        print(x, end=" | ")

print("")

for x in eitan:
    if isinstance(x,(str))  :
        print(x, end=" | ")

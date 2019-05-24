f = open("pass.txt", "r")
f1 = f.readlines()
p = open("targets.txt", "r")
f2 = p.readlines()
q = open("combo.txt", "w")
for y in f2:
    for x in f1:
        q.write(y[:-1]+":"+x)
q.close()
f.close()
p.close()

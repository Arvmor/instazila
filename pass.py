x = 1370
f = open("pass.txt", "w")
while x != 1386:
    f.write(str(x)+str(x)+"\n")
    x = x + 1
f.close()

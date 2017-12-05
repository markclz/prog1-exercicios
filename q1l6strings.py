p = "Universidade"
nv = ""
for i in range(len(p)-1,-1,-1):
    print("Decrescente %d"%i)
    nv+= p[i]
print(nv)
print()
nv = ""
for i in range(len(p)):
    print("crescente %d, decrescente %d" %(i,len(p)-1-i))
    nv+=p[len(p)-1-i]
print(nv)


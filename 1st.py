
f1=open('Book1.txt')
f2=open('Book2.txt')
f3=open('Book3.txt')

l1 = f1.readlines()
l2 = f1.readlines()
#l3= f3.readlines()
string = l1[0]
strsplit = string.split()
f1 = []
for k in strsplit:
         f1.append(len(k))
         e = max(f1)
for m in strsplit:
         if len(m) == e:
             print("The longest word is", m, "and it is", len(m,"characters long")

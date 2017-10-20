
f1=open("running-config.cfg")
f2=open("conf-txt","w")

for line in f1:
	f=f2.write(line.replace('172','192'))
	print(line)





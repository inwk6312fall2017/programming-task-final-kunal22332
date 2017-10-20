
f1=open("running-config.cfg")
f2=open("conf-txt","w")
old_ip="172."
new_ip="192."


def main():
   f1=open("running-config.cfg")
   f2 = open(conf-txt,"w")
    for line in f1:
        line_change = line.edit(old_ip,new_ip)
        f2.write(line_change)
    f1.close()
    f2.close()

if __name__ == '__main__':
    main()
	


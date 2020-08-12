import re
print("TCS Codevitta Zone1: Diet Plan")
out=re.findall('[0-9]+',input(''))
inp=(input('').split('|'))
f=list()
g=list()
for i in range(0,len(inp),1):
    f.append(re.findall('[0-9]+',inp[i]))
sum1=0
sum2=0
sum3=0
j=0
while(j<len(inp)+1 and sum1<=int(out[0]) and sum2<=int(out[1]) and sum3<=int(out[2])):
    for i in f:
        if(sum1+int(i[0])<int(out[0]) and sum2+int(i[1])<int(out[1]) and sum3+int(i[2])<int(out[2])):
            sum1+=int(i[0])
            sum2+=int(i[1])
            sum3+=int(i[2])
        else:
            j+=1
g.append([(int(out[0])-sum1),(int(out[1])-sum2),(int(out[2])-sum3)])
#print(sum1,sum2,sum3)
for i in f:
    if(sum1+int(i[0])<=int(out[0]) and sum2+int(i[1])<=int(out[1]) and sum3+int(i[2])<=int(out[2])):
        sum1+=int(i[0])
        sum2+=int(i[1])
        sum3+=int(i[2])
        g.append([(int(out[0])-sum1),(int(out[1])-sum2),(int(out[2])-sum3)])
        sum1-=int(i[0])
        sum2-=int(i[1])
        sum3-=int(i[2])
#print("gb4",g)
g.sort()
#print("gaf",g)
print(g[0][0],g[0][1],g[0][2])

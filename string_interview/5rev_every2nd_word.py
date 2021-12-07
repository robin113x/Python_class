s= input('Enter any string : ')
l = s.split()
l2 =[]
i=0
while i<len(l):
    if i%2==0:
        l2.append(l[i])
    else:
        l2.append(l[i][::-1])
    i+=1

out = ' '.join(l2)
print(out)
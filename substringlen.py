l1=[]
def sstrln(st):
  for i in range(0,len(st)):
    l1.append(st[i])
  print(len(list(set(l1))))
sstrln(str(input))

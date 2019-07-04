s = input()
l = len(s)
c = 0
for i in s:
  i = int(i)
  c += pow(i,l)
if c == int(s):
  print("yes")
else:
  print("no")

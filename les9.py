a = (32, 43, 56.65, 'sd') #kortej - spisok kotorii nel'za izmenit
b= [32, 43, 56.65, 'sd']
print (a)
print (b)
b[0] = 34
print (a.__sizeof__ ())
print (b.__sizeof__ ())
print (b)
c = tuple ('hello world') #tuple- razdeliaet kazdij element korteja
print (c)
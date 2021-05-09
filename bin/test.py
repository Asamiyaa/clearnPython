#https://www.runoob.com/python/python-tutorial.html

# -*- coding:utf-8 -*-
print "python hello word !!!";

for letter in 'Python':
   print 'this is for  :', letter

bool=False;
if bool:
    print ("True")
else:
    print ("False")


#raw_input("please input your info...\n")


one=1;
two=2;
print one ;
print two ;

dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
tinydict = {'name': 'runoob','code':6734, 'dept': 'sales'}
print dict['one']          # 输出键为'one' 的值
print dict[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键
print tinydict.values()    # 输出所有值
a = 5;
list = [1, 2, 3, 4, 5 ];
if ( a in list ):
   print "1 -----" ,a;
else:
    print "2=====";

plus = one * two;
print "this is + ", plus;
print "this is + ", 9//2;
print "this is + ", one == two;


count = 0
while (count < 9):
   print 'The count is:', count
   count = count + 1

print "Good bye!"

i = 2
while(i < 100):
   j = 2
   while(j <= (i/j)):
      if not(i%j): break
      j = j + 1
   if (j > i/j) : print i, " is su shu"
   i = i + 1

print "Good bye!"


for letter in 'Python':
   if letter == 'h':
      pass
      print 'pass block'
   print 'this num :', letter

print "Good bye!"


var1 = 'Hello World!'

print "output :- ", var1[:6] + 'Runoob!'

my_dic = {'Sales':'125256', 'Variance': '250689.4444', 'Division':'4568.25'}

print('for value in my_dic.items():  print(value')
for value in my_dic.items():
    print(value)
print('\nfor key, value in my_dic.items(): print(key,value)')
for key, value in my_dic.items():
    print(key,value)
print('\nfor item in my_dic.items(): print(item)')
for item in my_dic.items():
            print(item)
print('\nfor key in my_dic.items(): print(key)')
for key in my_dic.items():
    print(key)
print('\nfor item in my_dic.items(): print(item[0], item[1]')
for item in my_dic.items():
    print(item[0], item[1])
print('\nfor key in my_dic.__iter__(): print(key,my_dic[key]')

for key in my_dic.__iter__():
    print(key,my_dic[key])
print('\nfor key in my_dic:print(key, my_dic[key]')
for key in my_dic:
    print(key, my_dic[key])
print('\nfor key in my_dic.keys():  print(key, my_dic[key]')
for key in my_dic.keys():
    print(key, my_dic[key])

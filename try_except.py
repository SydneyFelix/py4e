L = []

while True:
    i = input('input a number or type \'done\' if your through: ')
    try:
        i = float(i)
        L.append(i)
    except:
             print('Against protocol')
             quit()
    if i == 'done' or i == 'Done' or i == 'DONE' and len(L) != 0:break
    elif i == 'D' or i  == 'd':
        print('you need to re-input a number: ')
        continue
    elif i == 'Do' or i == 'DO' or i == 'do' or i == 'dO':
        print('you need to re-input a number: ')
        continue
    else: i == 'done' or i == 'Done' or i == 'DONE' and len(L) == 0
    print('you need to re-input a number: ')
    continue

ave = sum(L)/len(L)
print('average = ',ave)







# finally:
#      print('Goodbye!')





# print('proceeding....')

syd = {'school':'ADU','Course':'Accounting','College':'PUP','Balance':1000.25}

for key in syd.__iter__():
    if key=='Balance':
        print(key,'{:,.5f}'.format(syd[key]))

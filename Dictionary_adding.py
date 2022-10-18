syd = {}

#1.using braces method: fill up the empty dictionary with 2 list elements,both are
#list : Hobies=kain, tulog ; the one is paboritong_ulam =
#Biryani at menudo

syd={'Hobies':['kain','tulog'],'paboritong_ulam':['torta','biryani']}

#2.bracket method, add an element in the dictionary: nationality = pinoy
syd['Nationality'] = 'Pinoy'
#3.using append method, add 'lechon' in pab_ulam
syd['paboritong_ulam'].append('lechon')

#4.using update method, key in Hobies as Pasyal, what happened?
#naging isa na lang hobbies mo
syd.update({'Hobies':['pasyal']})

#5.using bracket method , bring back Hobbies: kain
syd['Hobies']+=['kain']

#6.using bracket method , bring back Hobbies: tulog
syd['Hobies']+=['tulog']

#7.using extend method, add menudo and prito to paboritong_ulam
syd['paboritong_ulam'].extend(['prito','menudo'])

#8.using update method, add school as Adamson
syd.update({'school':['Adamson']})

#9.using update method, add school as PUP
syd.update({'school': 'PUP','course':'accounting'})

#10.what happened to adamson? na replace? now use again
#update method and ensure PUP is a list so later you
#can add Adamson to it.
syd.update({'school':['PUP']})
#11.this time add 'adamson as school using extend method'
syd['school'].extend(['Adamson'])
#notice now you both have PUP and Adamson

#12.using bracket method, add street = basilan
# syd['Street']+=['Basilan']

#hindi pwede diba, hindi kasi iyon list. achaka
#new entry ito e. better yet use update method.
syd.update({'Street':'Basilan'})

#13.using bracket method, add ' St.' to make it 'Basilan St.'
syd['Street']+=' St.'
#14.using update method, add Gender = male
syd.update({'Gender':'Male'})
#15 now print(syd.get('school','wala')), parasaan kaya ito?
print(syd.get('school','wala'))
#since nag print na PUP, Adamson, school mo yon e
#16 now print(syd.get('asawa','wala')), parasaan kaya ito?
print(syd.get('wife','wala'))
#wala ka namang asawa kaya nag print na 'wala'
print(syd)

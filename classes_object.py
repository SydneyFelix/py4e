class vegetables:
    pangalan = ''
    vit_content = ''
    madulas_tf = ''
    kulay = ''

    def paalala(self):
        desc = f'Madulas ba ang {self.pangalan} ? {self.madulas_tf}. Subalit ito ay kulay {self.kulay} at mayaman sa vitamin {self.vit_content}.'
        # desc = 'Madulas ba ang %s ? %s. Subalit ito ay kulay %s at mayaman sa vitamin %s.'%(self.pangalan,self.madulas_tf,self.kulay,self.vit_content)
        return desc

talong = vegetables()
talong.pangalan='Talong'
talong.vit_content='B'
talong.madulas_tf='hindi'
talong.kulay='violet'

print(talong.paalala())
print('galing')

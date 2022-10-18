# from PyPDF2 import PdfFileReader, PdfFileWriter
# import logging

data = []
F = open('5.txt')
for f in F:
    l = f.strip()
    if len(l)<1:continue
    data.append(l)
print(data)

# with open('1.txt','r', encoding='utf-8') as F:
#     data = F.readlines()
#     print(data)

#***********************************************************

# file_path = 'letuspray.pdf'
# pdf = 	PdfFileReader(file_path)

# # with open('sulatan.txt', 'w', encoding='utf-8') as f:
# with open('sulatan.txt', 'w') as f:
#     for p in range(pdf.numPages):
#         pageObj = pdf.getPage(p)
#
#         try:
#             txt = pageObj.extractText()
#             print(''.center(100,'-'))
#         except:
#             pass
#         else:
#             f.write('Page {0}\n'.format(p+1))
#             f.write(''.center(100,'-'))
#             f.write(txt)
#
#     f.close()

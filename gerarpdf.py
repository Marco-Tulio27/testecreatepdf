from PIL import Image
from fpdf import FPDF
resp= 's','n'
item=dict()
lista=list()
item['Vendedor']=input('Vendedor: \n')
while resp !='n':
    item['Produto']=input('Produto \n')
    item['Valor']=float(input('Valor \n'))  
    lista.append(item.copy())
    resp=input('deseja continuar:')
    
soma = 0
for i in lista:
    for k,v in i.items():
        print(k,v,end=' ')
        print('')
    soma += i['Valor']  # add the value of each item to the total sum
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
#add local image
# image = Image.open("C:\\Users\\Usuario\\Pictures\\opção_disel_2.png")
image = image.resize((595, 50))
#add image and resize at the page
#pdf.image('C:\\Users\\Usuario\\Pictures\\opção_disel_2.png',x=0, y=0, w=210, h=50)
pdf.cell(10,77,txt='telefone:(31)3821-5425 (31)38214-4331 whatsapp: (31) 98854-5425',ln=1)
pdf.cell(20,5,txt='Vendedor: ',ln=0)
pdf.cell(25,5,txt=item['Vendedor'],ln=1)
pdf.cell(30,28,txt='CNPJ/PIX: 18.778.644/0001-70 ',ln=5)
for x in lista:
    pdf.cell(100,1,txt=f"{x['Produto']}: R${x['Valor']}", ln=1)    
    pdf.cell(100,5,txt="-"*210, ln=1)    
pdf.cell(100,10, txt=f"Total: R${soma}", ln=1)
import random
r=random.randint(1,1000)
nome=input('digite o nome do arquivo: ')
pdf.output(f"{nome,r}.pdf")
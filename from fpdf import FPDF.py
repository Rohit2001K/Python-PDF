from fpdf import FPDF

pdf=FPDF(orientation='P',unit='pt',format='A4') #pdf basic formate

#adding pgae in pdf
pdf.add_page()

#adding image in pdf
pdf.image('logo.png',w=50,h=50,x=300)
pdf.set_font(family='arial',size=14)
pdf.cell(w=0,h=50,txt='Valorent which is also know as Valo is 5vs 5 FPS game.')

#saving pdf and nameing
pdf.output('pdf01.pdf')



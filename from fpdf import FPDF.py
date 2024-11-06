from fpdf import FPDF

pdf=FPDF(orientation='P',unit='pt',format='A4') #pdf basic formate

#adding pgae in pdf
pdf.add_page()

#adding image in pdf
pdf.image('logo.png',w=50,h=50,x=250)
pdf.set_font(family='arial',size=24,style='BU')
pdf.cell(w=0,h=50,txt='Valorent',align="C",ln=1)



#multi cell for multiple line data
pdf.set_font(family='arial',size=14)
text1="""Valorant is an online multiplayer computer game, produced by Riot Games. It is a first-person shooter game,consisting of two teams of five, where one team attacks and the other defends. Players control characters known as agents,who all have different abilities to use during gameplay. The game matchmaking system automatically groups players of similar skill together."""
pdf.multi_cell(w=0,h=20,txt=text1 )

#table data
pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Online")
pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Yes", ln=1)


pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Players")
pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="5 Vs 5" ,ln=1)

pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Control Type")
pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Mouse and Keyboard" ,ln=1)

pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Account Requried")
pdf.set_font(family='arial',size=14)
pdf.cell(w=200,h=20,txt="Yes" ,ln=1)

#saving pdf and nameing
pdf.output('pdf01.pdf')



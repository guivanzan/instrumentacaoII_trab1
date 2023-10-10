from rolamento import roll
from deslizamento import slide
from matplotlib.pyplot import scatter,show

mass = 0.03 #massa = 30 g = 0.03 kg
grav = 9.787899 #fornecido pelo Observatório Nacional em 1999
raio = 0.03 #raio do cilindro = 3 cm = 0.003 m

movslide45,movslide60 = slide()

enerKinSlide45 = []
for i in range(len(movslide45[0])):
    enerKinSlide45.append(((movslide45[0][i]**2)*mass)/2)

enerKinSlide60 = []
for i in range(len(movslide60[0])):
    enerKinSlide60.append(((movslide60[0][i]**2)*mass)/2)

movroll30,movroll45,movroll60 = roll()

enerKinRoll30 = []
for i in range(len(movroll30[0])):
    enerKinRoll30.append(((movroll30[0][i]**2)*mass)/2)

enerKinRoll45 = []
for i in range(len(movroll45[0])):
    enerKinRoll45.append(((movroll45[0][i]**2)*mass)/2)

enerKinRoll60 = []
for i in range(len(movroll60[0])):
    enerKinRoll60.append(((movroll60[0][i]**2)*mass)/2)

def kin():
    return enerKinRoll30,enerKinRoll45,enerKinRoll60,enerKinSlide45,enerKinSlide60

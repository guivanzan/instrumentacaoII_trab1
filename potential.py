from rolamento import roll
from deslizamento import slide
from matplotlib.pyplot import scatter,show

mass = 0.03 #massa = 30 g = 0.03 kg
grav = 9.787899 #fornecido pelo Observatório Nacional em 1999

movroll30,movroll45,movroll60 = roll()
movslide45,movslide60 = slide()


enerPotRoll30 = []
for i in range(len(movroll30[2])):
    enerPotRoll30.append(movroll30[2][i]*mass*grav)

enerPotRoll45 = []
for i in range(len(movroll45[2])):
    enerPotRoll45.append(movroll45[2][i]*mass*grav)

enerPotRoll60 = []
for i in range(len(movroll60[2])):
    enerPotRoll60.append(movroll60[2][i]*mass*grav)

enerPotSlide45 = []
for i in range(len(movslide45[2])):
    enerPotSlide45.append(movslide45[2][i]*mass*grav)

enerPotSlide60 = []
for i in range(len(movslide60[2])):
    enerPotSlide60.append(movslide60[2][i]*mass*grav)

def pot():
    return enerPotRoll30,enerPotRoll45,enerPotRoll60,enerPotSlide45,enerPotSlide60
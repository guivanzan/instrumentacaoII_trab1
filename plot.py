from matplotlib.pyplot import plot,scatter,show,subplots
from kinetic import kin
from potential import pot
from deslizamento import slide
from rolamento import roll

timeSlide45 = slide()[0][1]
timeSlide60 = slide()[1][1]

timeRoll30 = roll()[0][1]
timeRoll45 = roll()[1][1]
timeRoll60 = roll()[2][1]

enerKinRoll30,enerKinRoll45,enerKinRoll60,enerKinSlide45,enerKinSlide60 = kin()
enerPotRoll30,enerPotRoll45,enerPotRoll60,enerPotSlide45,enerPotSlide60 = pot()

fig, (ax1, ax2) = subplots(2,1)

ax1.plot(timeSlide45,enerKinSlide45)
ax1.plot(timeSlide45,enerPotSlide45)
ax1.grid()
ax1.title.set_text('Cilindro deslizando, h = 45 cm')


ax2.plot(timeSlide60,enerKinSlide60)
ax2.plot(timeSlide60,enerPotSlide60)
ax2.grid()
ax2.title.set_text('Cilindro deslizando, h = 60 cm')

show()

fig, (ax1, ax2, ax3) = subplots(3,1)

ax1.plot(timeRoll30,enerKinRoll30)
ax1.plot(timeRoll30,enerPotRoll30)
ax1.grid()
ax1.title.set_text('Cilindro deslizando com rolamento, h = 30 cm')


ax2.plot(timeRoll45,enerKinRoll45)
ax2.plot(timeRoll45,enerPotRoll45)
ax2.grid()
ax2.title.set_text('Cilindro deslizando com rolamento, h = 45 cm')


ax3.plot(timeRoll60,enerKinRoll60)
ax3.plot(timeRoll60,enerPotRoll60)
ax3.grid()
ax3.title.set_text('Cilindro deslizando com rolamento, h = 60 cm')

show()

print(f'O trabalho da força de atrito no primeiro movimento é: {enerPotSlide45[0]-enerKinSlide45[-1]:.4f}')
print(f'O trabalho da força de atrito no segundo movimento é: {enerPotSlide60[0]-enerKinSlide60[-1]:.4f}')
print(f'A energia de rolamento no primeiro movimento é: {enerPotRoll30[0]-enerKinRoll30[-1]:.4f}')
print(f'A energia de rolamento no segundo movimento é: {enerPotRoll45[0]-enerKinRoll45[-1]:.4f}')
print(f'A energia de rolamento no terceiro movimento é: {enerPotRoll60[0]-enerKinRoll60[-1]:.4f}')
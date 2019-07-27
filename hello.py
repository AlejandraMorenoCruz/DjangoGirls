"""
name = 'Sonja'
if name =='Ola':
    print('Hey Ola')
elif name == 'Sonja':
    print('Hey Sonja')
else:
    print('Hey anonymous!')


volume = 57
if volume <20:
    print("It's kinda quiet")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, Ican hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")
  

def hi(name):
    if name == 'Ola':
        print("Hi there!")
    elif name == 'Sonja':
        print("How are you")
    else:
        print("Hi anontmous!")

hi("")
  """

def hi(name):
    print("Hi " + name + "!")

girls = ["Rachel", "Monica", "Phoebe", "Ola", "You"]
for i in range(1,6):
    #hi(name)
    #print("next girl")
    print(i)
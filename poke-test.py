import tkinter as tk
from pokeapi import *
from random import *

#function to extract data for labels
def showPokemonData(event = None):
    num = txtPokemonNo.get()
    txtPokemonNo.delete(0,99)
    try:
        pokemonData = getPokemonData(num)
        lblNameValue.configure(text = pokemonData['name'].capitalize())
        lblHPValue.configure(text = pokemonData["stats"][5]['base_stat'])
        lblAttackValue.configure(text = pokemonData["stats"][4]['base_stat'])
        lblDefenceValue.configure(text = pokemonData["stats"][3]['base_stat'])
        lblSpeedValue.configure(text = pokemonData["stats"][0]['base_stat'])
        # something not quite working with PIL, commenting out until later
        #pokemonImage = getPokemonImage(num)
        #add the image and add it to a label
        #lblImage.configure(image=pokemonImage)
        #lblImage.image = pokemonImage
    except:
        txtPokemonNo.insert(0, 'Invalid choice')

smallFont = ["Helvetica", 14]
mediumFont = ["Helvetica", 18]
bigFont	= ["Helvetica",	30]

#create	a new GUI window
window = tk.Tk()
window.config(bg="#e0e0ff")
window.bind('<Return>',showPokemonData)
window.title("Pokedex")

#a label containing the instructions
lblInstructions	= tk.Label(window,text="Enter a number between 1 and 718:")
lblInstructions.pack()

#an 'entry' textbox for	typing in the pokemon number
txtPokemonNo = tk.Entry(window)
txtPokemonNo.pack()

#a button that will get the info for a pokemon
btnGetInfo = tk.Button(window,text="Get Data!", command=showPokemonData)
btnGetInfo.pack()

#labels	for the pokemon name, HP, Attack, Defence and Speed
lblNameText = tk.Label(window,text="Name:")
lblNameText.config(bg="#e0e0ff", fg="#111111", font=mediumFont)
lblNameText.pack()
lblNameValue = tk.Label(window,text="???")
lblNameValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblNameValue.pack()

lblHP = tk.Label(window,text="HP:")
lblHP.config(bg="#e0e0ff", fg="#111111",font=mediumFont)
lblHP.pack()
lblHPValue = tk.Label(window,text="0")
lblHPValue.config(bg="#e0e0ff",	fg="#111111",font=bigFont)
lblHPValue.pack()

lblAttack = tk.Label(window,text="Attack:")
lblAttack.config(bg="#e0e0ff",	fg="#111111",	
font=mediumFont)
lblAttack.pack()
lblAttackValue = tk.Label(window,text="0")
lblAttackValue.config(bg="#e0e0ff",	fg="#111111",	
font=bigFont)
lblAttackValue.pack()

lblDefence = tk.Label(window,text="Defence:")
lblDefence.config(bg="#e0e0ff",	fg="#111111",font=mediumFont)
lblDefence.pack()
lblDefenceValue = tk.Label(window,text="0")
lblDefenceValue.config(bg="#e0e0ff",fg="#111111",font=bigFont)
lblDefenceValue.pack()

lblSpeed = tk.Label(window,text="Speed:")
lblSpeed.config(bg="#e0e0ff", fg="#111111",font=mediumFont)
lblSpeed.pack()
lblSpeedValue = tk.Label(window,text="0")
lblSpeedValue.config(bg="#e0e0ff", fg="#111111", font=bigFont)
lblSpeedValue.pack()

#label for the pokemon image
lblImage = tk.Label(window)
lblImage.config(bg="#e0e0ff", fg="#111111")
lblImage.pack()

window.mainloop()

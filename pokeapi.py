from io import BytesIO
import tkinter as tk
#from PIL import Image, ImageTk
import requests

#function to get the data for a pokemon
def getPokemonData(num):
    r = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(num))
    #convert the json data into a python dictionary
    pokemonDict = r.json()
    return pokemonDict

#function to get the image for a pokemon
def getPokemonImage(num):
    image_bytes = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/"+str(num) + ".png")
    data_stream = BytesIO(image_bytes.content)
    pil_image = Image.open(data_stream)
    tk_image = ImageTk.PhotoImage(pil_image)
    return tk_image

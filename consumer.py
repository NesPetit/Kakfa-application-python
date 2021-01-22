from kafka import KafkaConsumer
from kafka.errors import KafkaError
from tkinter import *
import tkinter.ttk
import time
import json
import requests
import msgpack
from requests.exceptions import HTTPError
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from matplotlib.animation import FuncAnimation

# To consume latest messages and auto-commit offsets
consumer = KafkaConsumer('crypto2',
                         group_id='my-group',
                         bootstrap_servers=['localhost:9092'],
                         value_deserializer=lambda m: json.loads(m.decode('ascii')), 
                         auto_offset_reset = 'earliest')

def Tableau():
    window = Tk()
    window.title("My Application")
    window.geometry("800x600")
    window.minsize(400, 200)
    frame = Frame(window)
    
    tableau = tkinter.ttk.Treeview(frame, columns=('compteur','symbol', 'name', 'price', 'varia'))

    tableau.column('compteur', width=30, minwidth = 30, anchor = "center")
    tableau.column('symbol', width=80, minwidth = 80, anchor = "center")
    tableau.column('name', width=100, minwidth = 100, anchor = "center")
    tableau.column('price', width=90, minwidth = 90, anchor = "center")
    tableau.column('varia', width=100, minwidth = 100, anchor = "center")

    tableau.heading('compteur', text=' ')
    tableau.heading('symbol', text='Symbol')
    tableau.heading('name', text='Name')
    tableau.heading('price', text='Price')
    tableau.heading('varia', text='% Variation')
    tableau['show'] = 'headings'
    #Inserts
    first_value = 0
    tableau.insert("", 1, "1", text = 1, values = (1, "BTC", "Bitcoin", "str(msg.value['bitcoin']['usd'])", "Variation depuis la premiere prise"))
    tableau.insert("", 2,"2" , text = 2, values = (2, "ETH", "Ethereum", "Prix actuel", "Variation depuis la premiere prise"))
    tableau.insert("", 3,"3", text = 3, values = (3, "DOT", "Polkadot", "Prix actuel", "Variation depuis la premiere prise"))

    i = 0
    str
    consumer.poll()
    consumer.seek_to_beginning()
    for msg in consumer:
        calcul = first_value / msg.value['bitcoin']['usd']
        if calcul > 0:
            str = "+"
        if first_value == 0:
            first_value = msg.value['bitcoin']['usd']

        tableau.delete(1,2,3)
        tableau.insert("", 1, "1", text = 1, values = (1, "BTC2", "Bitcoin", str(msg.value['bitcoin']['usd']), str() + "%"))
        tableau.insert("", 2,"2", text = 2, values = (2, "ETH2", "Ethereum", "Prix actuel", "Variation depuis la premiere prise"))
        tableau.insert("", 3,"3", text = 3, values = (3, "DOT2", "Polkadot", "Prix actuel", "Variation depuis la premiere prise"))
        tableau.pack(expand=YES, fill='both')
        frame.pack(expand=YES, fill='both', padx = 10, pady = 40)

        window.update_idletasks()
        window.update()
    #window.mainloop()

# #Afficher
# def Graph(coin, currencie):
#     x_vals = []
#     y_vals = []
#     fig = plt.figure()
#     plt.title('Cours du ' + coin + 'en fonction de ' currencie)
#     plt.xlabel('Time (s)')         # Nom de la grandeur en abscisse
#     plt.ylabel('Price')         # Nom de la grandeur en ordonnée
#     ax = fig.add_subplot(111)
#     i = 0
  #   consumer.poll()
  #   consumer.seek_to_beginning()
#     for msg in consumer:
#         x_vals.append(i)
#         y_vals.append(msg.value[coin][currencie])
#         print(msg.value[coin][currencie])

#         ax.plot(x_vals, y_vals, color='b')
#         fig.canvas.draw()
#         ax.set_xlim(right=i + 10)
#         fig.show()
#         plt.pause(0.01)
#         i += 1

    # plt.close()


def menu():
    choix = ''
    print("Menu principal")
    print("Quelle action souhaitez-vous effectuer ?")
    print("1 - Affichage d'un graphique crypto en temps reel (environ 2 minutes interval d'actualisation)")
    print("2 - Tableau de toutes les cryptos en temps reel avec sa variation depuis le lancement de l'appli")
    print("3 - Quitter l'application")

    while choix != '1' and choix!= '2':
        choix = input("Selection : ")
    
    if choix == '1':
        #Faire le graph avec plot
        print("Veuillez choisir une crypto (BITCOIN, ETH, DOT, LINK, SNX, REN, ADA) :")
        choix1 = input().lower()
        print("Veuillez choisir une seconde monnaie supportée (EUR, USD, BTC, ETH, BNB :")
        choix2 = input().lower()
        #Graph(choix1, choix2)


    if choix == '2':
        #Faire le tableau avec tkinter
        Tableau()


menu()


consumer.close()

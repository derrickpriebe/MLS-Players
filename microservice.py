import time
import zmq
from flask import Flask, jsonify, render_template, json, redirect, request
import pandas as pd 
import webbrowser

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://127.0.0.1:5555")
while True:
    #  Wait for next request from client
    message = socket.recv_string()
    print(f"Received request: {message}")

    #  Do some 'work'


    #  Send reply back to client


    table = pd.read_csv("S.csv")
    table.fillna('', inplace=True)
    table_dict = {col: list(table[col]) for col in table.columns}
    headings = list(table.columns)
    data = list(table.values)

    rowindex = int(message)
    info = list(data[rowindex-1])
    
    player_id = info[len(info)-1]
    ID = player_id
    id = str(ID)
    
    a = "https://www.transfermarkt.com/oskar-agren/profil/spieler/"
    b = "https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query="
    url = ""

    if ID > 0:
        url =  a + id
 
    if ID == 0:
        name1 = str(info[0])
        name2 = str(info[1])
        Name = name1 + "+" + name2
        url = b + Name
        
    socket.send_string(url)


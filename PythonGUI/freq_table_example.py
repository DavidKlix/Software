# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 21:49:19 2019

@author: S524113
"""
	
from tkinter import *
from tkinter import filedialog
import frequencytables as ft
import pandas as pd
 
window = Tk()
 
window.title("Dr. Jornaz Statistics -- Frequency Tables")

window.geometry("500x500")

selected = IntVar()
result = "" 

instructions = Label(window, text="Please select column then press a button.")

file = filedialog.askopenfilename(title='Choose a file')
df = pd.read_csv(file)
columns = list(df.columns.values)

tkvar = StringVar(window)
tkvar.set(columns[0])
choices = OptionMenu(window, tkvar, *columns)
def freq_tab():
    global result
    result = ft.frequency_table(tkvar.get(), df)
    results = Label(window, text=result)
    results.pack()
def rel_freq():
    global result
    result = ft.relative_frequency_table(tkvar.get(), df)
    results = Label(window, text=result)
    results.pack()
btn_freq = Button(window, text="Frequency Table", command=freq_tab)
btn_rel = Button(window, text="Relative Frequency Table", command=rel_freq)

results = Label(window, text=result)

instructions.pack()
choices.pack()
btn_freq.pack()
btn_rel.pack()
results.pack()
window.mainloop()
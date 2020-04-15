import pandas_datareader as pdr
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from tkinter import Tk, Label, Button, Entry, IntVar, END, W, E
#https://wiki.python.org/moin/TkInter
#Main Class
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class StockApp:

    def __init__(self, master):
        self.master = master
        master.title("Finance")
        self.stock = " "
        self.entered_number = " "

        self.total_label_text = IntVar()
        self.total_label_text.set(self.stock)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Stock Ticker:")

        vcmd = master.register(self.validate)  # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))
        self.buildChart_button = Button(master, text="Build", command=lambda: self.update("Build Chart"))
        self.GetDow_button = Button(master, text ="Get Dow",command=lambda: self.update("getDow"))

    

        # LAYOUT
        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)
        self.entry.grid(row=2, column=0, columnspan=3, sticky=W+E)
        self.reset_button.grid(row=2, column=2, sticky=W+E)
        self.buildChart_button.grid(row=1, column=2)
        self.GetDow_button.grid(row=1, column=1)

    #Functions
    def validate(self, new_text):
        if not new_text:  # the field is being cleared
            self.entered_ticker = " "
            return True
        try:
            self.entered_ticker = new_text
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "Build Chart":
            buildChart(self.entered_ticker)
        if method == "getDow":
            getDow()
        else:  # reset
            self.stock = " "

        self.total_label_text.set(self.stock)
        self.entry.delete(0, END)

def buildChart(ticker):
        style.use('fast')
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2020, 1, 1)
        df = pdr.DataReader(ticker, 'yahoo', start, end)
        df['Adj Close'].plot()
        plt.show()

def getDow():
        style.use('fast')
        start = dt.datetime(2000, 1, 1)
        end = dt.datetime(2020, 1, 1)
        df = pdr.DataReader('^DJI','yahoo',start,end)
        df['Adj Close'].plot()
        plt.show()

#Main functionality below!!
root = Tk()
my_gui = StockApp(root)
root.mainloop()

### IDEAS
# Add a way to keep the graph inside the GUI and update it upon change in stock ticker
# Add a feature to open a new tab with a graph
# Make a way to draw lines so that you can analyze it on the graphes??
# Add a way to run a regression on it? see if it fits any common trends.
# Make a way to select what date frame you want to look at!!
# Portfolio tracker?? Can you do this automatically?
    #https://www.reddit.com/r/RobinHood/comments/7173l1/python_script_for_portfolio_tracking/
# Other Ideas??


#This is an app for personal growth in coding and will be useful to my goals.
#if anyone else is interested reach out. I don't think spencer is but we can see!!
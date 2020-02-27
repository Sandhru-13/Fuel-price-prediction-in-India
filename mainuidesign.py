# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:11:21 2019

@author: SRIVIGNESH
"""


from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import matplotlib.pyplot as plt 
from statsmodels.tsa.arima_model import ARIMA
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as ms
from collections import OrderedDict
from dateutil import relativedelta
from PIL import ImageTk, Image
import os
import statsmodels.api as sm

series = read_csv('petrol&dieselfinaldata.csv',header=0)
def arimaForecast(data,od):
    model = ARIMA(data, order=(od[0],od[1],od[2]))
    model_fit = model.fit(disp=0)
    #print(model_fit.summary())
    forecast1=[]
    forecast1=model_fit.forecast(steps=30)[0]
    return(forecast1)
predict=[]
order=[0,2,2]
predict.append(arimaForecast(series['DELHI (P)'],order))
order=[1,1,1]
predict.append(arimaForecast(series['MUMBAI(P)'],order))
order=[2,2,1]
predict.append(arimaForecast(series['CHENNAI(P)'],order))
order=[0,2,1]
predict.append(arimaForecast(series['KOLKATA(P)'],order))
order=[0,2,2]
predict.append(arimaForecast(series['DELHI(D)'],order))
order=[3,2,2]
predict.append(arimaForecast(series['MUMBAI(D)'],order))
order=[0,2,2]
predict.append(arimaForecast(series['CHENNAI(D)'],order))
order=[0,2,1]
predict.append(arimaForecast(series['KOLKATA(D)'],order))    

series = read_csv('Fuel_prices_IEA.csv',header=0)

def lineartrend(x,y):
    results = sm.OLS(y, x).fit()
    #print(results.summary())
    return(results)
globalpredict=[]
globalpredict.append(lineartrend(series['Changes petrol'],series['France(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Germany(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Italy(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Spain(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['UK(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Japan(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Canada(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['USA(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['India(p)']))
globalpredict.append(lineartrend(series['Changes petrol'],series['France(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Germany(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Italy(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Spain(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['UK(p)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Japan(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['Canada(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['USA(d)'])) 
globalpredict.append(lineartrend(series['Changes petrol'],series['India(d)']))

series1 = read_csv('avg.csv',header=0)
xcrude=series1[['Changes','INDIA( CRUDE OIL)']]
y=[]
y.append(series1['DELHI (P)'])
y.append(series1['MUMBAI(P)'])
y.append(series1['CHENNAI(P)'])
y.append(series1['KOLKATA(P)'])
y.append(series1['DELHI(D)'])
y.append(series1['MUMBAI(D)'])
y.append(series1['CHENNAI(D)'])
y.append(series1['KOLKATA(D)'])

def reg_m(y, x):
    X = sm.add_constant(x)
    results = sm.OLS(y, X).fit()
    #predict= results.predict(X)
    #print(predict)
    return results
def predict_mult(c,x_new1,x_new2):
    x_new=[x_new1]
    
    Y=[x_new2]
    const=[1]
    pred=pd.DataFrame({'const':const,
                   'X':x_new,
                   'Y':Y})
    D=pred[['const','X','Y']]
    d=c.predict(D)
    return float(d)
 
#print(globalpredict[0].predict(x))

class design:
    def __init__(self,master):
        self.master=master
        self.crudeval= StringVar()
        self.crudeval1=StringVar()
        self.username = StringVar()
        self.password = StringVar()
        self.first=None
        self.second=None
        self.third=None
        self.fourth=None
        self.StartUpDateTime    = datetime.now()
        self.DefaultYear        = self.StartUpDateTime.year   
        self.DefaultMonthNumber = self.StartUpDateTime.month  
        self.DefaultDayOfMonth  = self.StartUpDateTime.day
        self.YearAndMonthLengths =  [  365,31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
        self.EnglishMonthNames = ( 'Entire Year','January','February', 'March', 
                      'April', 'May', 'June', 'July', 'August', 'September', 
                      'October', 'November', 'December' )
        self.Month_Names = self.EnglishMonthNames
        self.DaysInMonth = OrderedDict()    
        for i in range( 0, len( self.Month_Names ) ):   
            self.DaysInMonth[ self.Month_Names[ i ] ] = self.YearAndMonthLengths[ i ]  

        self.DefaultMonthName   = self.Month_Names[ self.DefaultMonthNumber ]
        self.DefaultMonthLength = self.DaysInMonth[ self.DefaultMonthName ]
        # Initialize the Spinbox interface variables to todays date
        self.SelectedYear        = IntVar(    value = self.DefaultYear )
        self.SelectedMonthName   = StringVar( value = self.DefaultMonthName ) 
        self.SelectedMonthLength = IntVar(   value = self.DefaultMonthLength )
        self.SelectedDay         = IntVar(    value = self.DefaultDayOfMonth )
        
        self.SelectedYear1        = IntVar(    value = self.DefaultYear )
        self.SelectedMonthName1   = StringVar( value = self.DefaultMonthName ) 
        self.SelectedMonthLength1 = IntVar(   value = self.DefaultMonthLength )
        self.SelectedDay1         = IntVar(    value = self.DefaultDayOfMonth )
        
        self.SelectedYear2        = IntVar( )
        self.SelectedMonthName2   = StringVar( value = self.DefaultMonthName ) 
        self.SelectedMonthLength2 = IntVar(   value = self.DefaultMonthLength )
        self.SelectedDay2         = IntVar(    value = self.DefaultDayOfMonth )
        
        self.SelectedYear3        = IntVar(  )
        self.SelectedMonthName3   = StringVar( value = self.DefaultMonthName ) 
        self.SelectedMonthLength3 = IntVar(   value = self.DefaultMonthLength )
        self.SelectedDay3         = IntVar(    value = self.DefaultDayOfMonth )
        
        self.SelectedYear11        = IntVar(    value = self.DefaultYear )
        self.SelectedMonthName11   = StringVar( value = self.DefaultMonthName )
        
        self.SelectedYear12        = IntVar(    value = self.DefaultYear )
        self.SelectedMonthName12   = StringVar( value = self.DefaultMonthName )        
        
        self.code=0
        self.code1=0
        self.MonthSpinBox=None
        self.YearSpinBox=None
        self.predictbtn=None
        self.DaySpinBox=None
        self.bgtabs='#3B3B98'
        self.bgselected='#1B9CFC'
        self.countries=["France","Germany","Italy","Spain","United Kingdom","Japan","Canada","U.S.A","India"]
    def getMonth(self,month):
        for i in range(13):
            if(self.EnglishMonthNames[i] == month):
                print("yes")
                return i
            else:
                print("no")
            
    def main_ui(self):
        if(self.second is not None):
            self.second.pack_forget()
        if(self.third is not None):
            self.third.pack_forget()
            self.thirdimg.pack_forget()
        if(self.fourth is not None):
            self.fourth.pack_forget()
        if(self.first is not None):
            self.first.pack_forget()
            self.firstimg.pack_forget()        
        self.first = Frame(self.master,padx =5,pady = 10,bg='white')
        self.first.pack()
        self.firstimg=Frame(self.master,bg='white')
        self.firstimg.pack()
        self.one=Button(self.first,text='Fuel Price Analysis in INDIA',padx=10,bd=0,fg=('black'),font=('',12),bg=self.bgselected,command=self.main_ui).grid(row=0,column=0)
        self.two=Button(self.first,text='Fuel Price Prediction in INDIA',padx=10,command=(self.twoSelected),bg=self.bgtabs,bd=0,fg=('#58B19F'),font=('',12)).grid(row=0,column=1)                
        self.three=Button(self.first,text='Analysis accross global',fg=('#58B19F'),command=self.threeSelected,bg=self.bgtabs,padx=10,bd=0,font=('',12)).grid(row=0,column=2)
        self.four=Button(self.first,text='Prediction of global fuel price',bd=0,bg=self.bgtabs,padx=10,command=(self.fourSelected),fg=('#58B19F'),font=('',12)).grid(row=0,column=3)                                                    
        self.img1 = ImageTk.PhotoImage(Image.open("formated graphs india.png"))
        self.panel = Button(self.firstimg, image = self.img1)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")


    def threeSelected(self):
        if(self.second is not None):
            self.second.pack_forget()
        if(self.third is not None):
            self.third.pack_forget()
            self.thirdimg.pack_forget()
        if(self.fourth is not None):
            self.fourth.pack_forget()
        if(self.first is not None):
            self.first.pack_forget()
            self.firstimg.pack_forget()        
        self.third = Frame(self.master,padx =5,pady = 10,bg='white')
        self.third.pack()
        self.thirdimg=Frame(self.master,bg='white')
        self.thirdimg.pack()
        self.one=Button(self.third,text='Fuel Price Analysis in INDIA',padx=10,bd=0,fg=('#58B19F'),font=('',12),bg=self.bgtabs,command=self.main_ui).grid(row=0,column=0)
        self.two=Button(self.third,text='Fuel Price Prediction in INDIA',padx=10,command=(self.twoSelected),bg=self.bgtabs,bd=0,fg=('#58B19F'),font=('',12)).grid(row=0,column=1)                
        self.three=Button(self.third,text='Analysis accross global',fg=('black'),command=self.threeSelected,bg=self.bgselected,padx=10,bd=0,font=('',12)).grid(row=0,column=2)
        self.four=Button(self.third,text='Prediction of global fuel price',bd=0,bg=self.bgtabs,padx=10,command=(self.fourSelected),fg=('#58B19F'),font=('',12)).grid(row=0,column=3)                                                    
        self.img1 = ImageTk.PhotoImage(Image.open("formated international1.png"))
        self.panel = Button(self.thirdimg, image = self.img1)
        self.panel.pack(side = "bottom", fill = "both", expand = "yes")




                     
    def twoSelected(self):
        if(self.second is not None):
            self.second.pack_forget()
        if(self.third is not None):
            self.third.pack_forget()
            self.thirdimg.pack_forget()
        if(self.fourth is not None):
            self.fourth.pack_forget()
        if(self.first is not None):
            self.first.pack_forget()
            self.firstimg.pack_forget()
        self.second=Frame(self.master,padx=5,pady=10,bg='white')
        self.one=Button(self.second,text='Fuel Price Analysis in INDIA',padx=10,bd=0,fg=('#58B19F'),command=self.main_ui,bg=self.bgtabs,font=('',12)).grid(row=0,column=0)
        self.two=Button(self.second,text='Fuel Price Prediction in INDIA',padx=10,bg=self.bgselected,command=(self.twoSelected),bd=0,fg=('black'),font=('',12)).grid(row=0,column=1)
        self.three=Button(self.second,text='Analysis accross global',fg=('#58B19F'),command=self.threeSelected,bg=self.bgtabs,padx=10,bd=0,font=('',12)).grid(row=0,column=2)
        self.four=Button(self.second,text='Prediction of global fuel price',bg=self.bgtabs,command=(self.fourSelected),bd=0,padx=10,fg=('#58B19F'),font=('',12)).grid(row=0,column=3)
        
        self.petrol=Button(self.second,text="PETROL",font=('',18),bd=0,bg="yellow",pady=0,padx=0).grid(row=1,column=0)
        self.delhip=Button(self.second,text="DELHI",bg='white',font = ('',15),bd=0,command=(self.delhippredict),padx = 50)
        self.orig_color=self.delhip.cget("background")
        self.delhip.grid(row=1,column=1)
        self.mumbaip=Button(self.second,text="MUMBAI",bg='white',font = ('',15),bd=0,command=(self.mumbaippredict),padx = 50)
        self.mumbaip.grid(row=1,column=2)
        self.chennaip=Button(self.second,text="CHENNAI",bg='white',font = ('',15),bd=0,command=(self.chennaippredict),padx = 50)
        self.chennaip.grid(row=1,column=3)
        self.kolkatap=Button(self.second,text="KOLKATA",bg='white',font = ('',15),bd=0,command=(self.kolkatappredict),padx = 50)
        self.kolkatap.grid(row=1,column=4)
        
        
        
        self.diesel=Button(self.second,text="DIESEL",font=('',18),bg="yellow",padx=0,bd=0).grid(row=5,column=0)
        self.delhid=Button(self.second,text="DELHI",bg='white',font = ('',15),command=(self.delhidpredict),padx = 50,bd=0)
        self.delhid.grid(row=5,column=1)
        self.mumbaid=Button(self.second,text="MUMBAI",bg='white',font = ('',15),padx = 50,command=(self.mumbaidpredict),bd=0)
        self.mumbaid.grid(row=5,column=2)
        self.chennaid=Button(self.second,text="CHENNAI",bg='white',font = ('',15),padx = 50,command=(self.chennaidpredict),bd=0)
        self.chennaid.grid(row=5,column=3)
        self.kolkatad=Button(self.second,text="KOLKATA",bg='white',font = ('',15),padx = 50,command=(self.kolkatadpredict),bd=0)
        self.kolkatad.grid(row=5,column=4)
        
        #Prediction Based on Crude OIl Price
        Label(self.second,text="Based on Crude OIL",font=('',18),bg=('white'),pady=5).grid(row=9,column=0)
        self.petrolc=Button(self.second,text="PETROL",font=('',18),bd=0,bg="yellow",pady=0,padx=0).grid(row=10,column=0)
        self.delhicp=Button(self.second,text="DELHI",bg='white',font = ('',15),bd=0,command=(self.delhicppredict),padx = 50)
        self.orig_color=self.delhicp.cget("background")
        self.delhicp.grid(row=10,column=1)
        self.mumbaicp=Button(self.second,text="MUMBAI",bg='white',font = ('',15),bd=0,command=(self.mumbaicppredict),padx = 50)
        self.mumbaicp.grid(row=10,column=2)
        self.chennaicp=Button(self.second,text="CHENNAI",bg='white',font = ('',15),bd=0,command=(self.chennaicppredict),padx = 50)
        self.chennaicp.grid(row=10,column=3)
        self.kolkatacp=Button(self.second,text="KOLKATA",bg='white',font = ('',15),bd=0,command=(self.kolkatacppredict),padx = 50)
        self.kolkatacp.grid(row=10,column=4)
        
        
        
        self.dieselc=Button(self.second,text="DIESEL",font=('',18),bg="yellow",padx=0,bd=0).grid(row=5+9,column=0)
        self.delhicd=Button(self.second,text="DELHI",bg='white',font = ('',15),command=(self.delhicdpredict),padx = 50,bd=0)
        self.delhicd.grid(row=5+9,column=1)
        self.mumbaicd=Button(self.second,text="MUMBAI",bg='white',font = ('',15),padx = 50,command=(self.mumbaicdpredict),bd=0)
        self.mumbaicd.grid(row=5+9,column=2)
        self.chennaicd=Button(self.second,text="CHENNAI",bg='white',font = ('',15),padx = 50,command=(self.chennaicdpredict),bd=0)
        self.chennaicd.grid(row=5+9,column=3)
        self.kolkatacd=Button(self.second,text="KOLKATA",bg='white',font = ('',15),padx = 50,command=(self.kolkatacdpredict),bd=0)
        self.kolkatacd.grid(row=5+9,column=4)        
        self.second.pack()
        
    def fourSelected(self):
        if(self.second is not None):
            self.second.pack_forget()
        if(self.third is not None):
            self.third.pack_forget()
            self.thirdimg.pack_forget()
        if(self.fourth is not None):
            self.fourth.pack_forget()
        if(self.first is not None):
            self.first.pack_forget()
            self.firstimg.pack_forget()
        
        self.fourth=Frame(self.master,padx=5,pady=10,bg='white')
        self.one=Button(self.fourth,text='Fuel Price Analysis in INDIA',padx=10,bd=0,fg=('#58B19F'),bg=self.bgtabs,font=('',12),command=self.main_ui).grid(row=0,column=0)
        self.two=Button(self.fourth,text='Fuel Price Prediction in INDIA',bg=self.bgtabs,padx=10,command=(self.twoSelected),bd=0,fg=('#58B19F'),font=('',12)).grid(row=0,column=1)
        self.three=Button(self.fourth,text='Analysis accross global',command=self.threeSelected,bg=self.bgtabs,fg=('#58B19F'),padx=10,bd=0,font=('',12)).grid(row=0,column=2)
        self.four=Button(self.fourth,text='Prediction of global fuel price',bg=self.bgselected,command=(self.fourSelected),bd=0,padx=10,fg=('black'),font=('',12)).grid(row=0,column=3)
        self.fpetrol=Button(self.fourth,text="PETROL",font=('',18),bd=0,bg="yellow",pady=0,padx=0).grid(row=1,column=0)
        Label(self.fourth,text="Choose a country",font=('',14),padx=6,pady=5,bg='white').grid(row=2,column=1,sticky=W)
        self.menu=ttk.Combobox(self.fourth,values=self.countries,state='readonly')
        self.menu.current(0)
        self.menu.grid(row=3,column=1)
        self.YearSpinBox4  = Spinbox(self.fourth, 
                        from_ = 2018, to = 2020,
                        textvariable = self.SelectedYear2, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox4  = Spinbox(self.fourth,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName2, 
                         wrap = TRUE, state = 'readonly', width = 10 )
        self.YearSpinBox4.grid(row=4,column=1,sticky=W)
        self.MonthSpinBox4.grid(row=4,column=2,sticky=W)
        self.prdbtn4=Button(self.fourth,text='PREDICT',font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue41).grid(row=5,column=1)
        
        self.fdiesel=Button(self.fourth,text="DIESEL",font=('',18),bd=0,bg="yellow",pady=0,padx=0).grid(row=8,column=0)
        Label(self.fourth,text="Choose a country",font=('',14),padx=6,pady=5,bg='white').grid(row=9,column=1,sticky=W)
        self.menu1=ttk.Combobox(self.fourth,values=self.countries,state='readonly')
        self.menu1.current(0)
        self.menu1.grid(row=10,column=1)
        self.YearSpinBox41  = Spinbox(self.fourth, 
                        from_ = 2018, to = 2020,
                        textvariable = self.SelectedYear3, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox41  = Spinbox(self.fourth,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName3, 
                         wrap = TRUE, state = 'readonly', width = 10 )
    
        self.YearSpinBox41.grid(row=11,column=1,sticky=W)
        self.MonthSpinBox41.grid(row=11,column=2,sticky=W)
        self.prdbtn41=Button(self.fourth,text='PREDICT',font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue42).grid(row=12,column=1)
        
        
        self.fourth.pack()
    
    
    def getCountryIndex(self,con):
        for i in range(len(self.countries)):
            if(self.countries[i]==con):
                return i
        
    
    def prdvalue41(self):
        conindex=self.getCountryIndex(self.menu.get())
        mon=self.getMonth(self.SelectedMonthName2.get())
        date1="2017-10-01"
        date2=str(self.SelectedYear2.get())+"-"+str(mon)+"-"+"01"
        monrem=self.months_between(date1,date2)
        predvalp=float(globalpredict[conindex].predict(monrem))
        Label(self.fourth,text="Predicted Petrol price is",font=('',18),bg='white').grid(row=6,column=1)
        Label(self.fourth,text=str(predvalp)+" dollars",font=('',18),bg='white').grid(row=6,column=2)
        
    def prdvalue42(self):
        conindex=self.getCountryIndex(self.menu1.get())
        mon=self.getMonth(self.SelectedMonthName3.get())
        date1="2017-10-01"
        date2=str(self.SelectedYear3.get())+"-"+str(mon)+"-"+"01"
        monrem=self.months_between(date1,date2)
        predvald=float(globalpredict[conindex+9].predict(monrem))
        Label(self.fourth,text="Predicted Diesel price is",font=('',18),bg='white').grid(row=13,column=1)
        Label(self.fourth,text=str(predvald)+" dollars",font=('',18),bg='white').grid(row=13,column=2)
        
    def dateSelection(self):
        ''''if self.MonthSpinBox is not None:
            '''
            
        self.YearSpinBox  = Spinbox(self.second, 
                        from_ = 2019, to = 2020,
                        textvariable = self.SelectedYear, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox  = Spinbox(self.second,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName, 
                         wrap = TRUE, state = 'readonly', width = 10,command=self.update_days )       
        self.DaySpinBox  = Spinbox(self.second, 
                       from_ = 1, 
                       to = self.SelectedMonthLength.get(), 
#                       to = DaysInMonth[ SelectedMonthName.get() ],
#                       values = tuple( str( i ) for i in range( 1, SelectedMonthLength.get() + 1 ) ),
#                       vsssalues = lambda : tuple( str( i ) for i in range( 1, DaysInMonth[ SelectedMonthName.get() ] + 1 ) )
                       textvariable = self.SelectedDay,  
                       wrap = TRUE, state = 'readonly', width = 5
                     )
        
        self.MonthSpinBox.grid(row = 2, column = 1)
        self.DaySpinBox.grid(row = 2, column = 2)
        self.YearSpinBox.grid(row = 2, column = 3)
        self.predictbtn=Button(self.second,text="PREDICT",font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue1).grid(row=3,column=2)
    def dateSelection1(self):
        ''''if self.MonthSpinBox is not None:
            '''
            
        self.YearSpinBox1  = Spinbox(self.second, 
                        from_ = 2019, to = 2020,
                        textvariable = self.SelectedYear1, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox1  = Spinbox(self.second,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName1, 
                         wrap = TRUE, state = 'readonly', width = 10,command=self.update_days1 )       
        self.DaySpinBox1  = Spinbox(self.second, 
                       from_ = 1, 
                       to = self.SelectedMonthLength1.get(), 
#                       to = DaysInMonth[ SelectedMonthName.get() ],
#                       values = tuple( str( i ) for i in range( 1, SelectedMonthLength.get() + 1 ) ),
#                       vsssalues = lambda : tuple( str( i ) for i in range( 1, DaysInMonth[ SelectedMonthName.get() ] + 1 ) )
                       textvariable = self.SelectedDay1,  
                       wrap = TRUE, state = 'readonly', width = 5
                     )
        
        self.MonthSpinBox1.grid(row = 6, column = 1)
        self.DaySpinBox1.grid(row = 6, column = 2)
        self.YearSpinBox1.grid(row = 6, column = 3)
        self.predictbtn1=Button(self.second,text="PREDICT",font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue2).grid(row=7,column=2)

    def dateSelection3(self):
        ''''if self.MonthSpinBox is not None:
            '''
            
        self.YearSpinBox11  = Spinbox(self.second, 
                        from_ = 2019, to = 2020,
                        textvariable = self.SelectedYear11, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox11  = Spinbox(self.second,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName11, 
                         wrap = TRUE, state = 'readonly', width = 10 )
        Label(self.second,text="Crude OIL price",font=('',16),bg='white').grid(row=11,column=1)
        self.crudep=Entry(self.second,bd = 5,textvariable=self.crudeval,font = ('',15),bg='white').grid(row=11,column=2)
        self.MonthSpinBox11.grid(row = 11, column = 3)
        self.YearSpinBox11.grid(row = 11, column = 4)
        self.predictbtn11=Button(self.second,text="PREDICT",font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue3).grid(row=12,column=2)

    def dateSelection4(self):
        ''''if self.MonthSpinBox is not None:
            '''
            
        self.YearSpinBox12  = Spinbox(self.second, 
                        from_ = 2019, to = 2020,
                        textvariable = self.SelectedYear12, 
                        wrap = TRUE, state = 'readonly', width = 7 )
        self.MonthSpinBox12  = Spinbox(self.second,  
                         values = tuple( self.DaysInMonth.keys() )[1:],                         
                         textvariable = self.SelectedMonthName12, 
                         wrap = TRUE, state = 'readonly', width = 10 )
        Label(self.second,text="Crude OIL price",font=('',16),bg='white').grid(row=15,column=1)
        self.cruded=Entry(self.second,bd = 5,textvariable=self.crudeval1,font = ('',15),bg='white').grid(row=15,column=2)        
        self.MonthSpinBox12.grid(row = 15, column = 3)
        self.YearSpinBox12.grid(row = 15, column = 4)
        self.predictbtn12=Button(self.second,text="PREDICT",font=('',10),bd=5,padx=3,pady=5,command=self.prdvalue4).grid(row=16,column=2)

    def delhippredict(self):
        self.delhip.config(bg="yellow")
        self.mumbaip.config(bg=self.orig_color)
        self.chennaip.config(bg=self.orig_color)
        self.kolkatap.config(bg=self.orig_color) 
        self.code=1
        self.dateSelection()
    
    def mumbaippredict(self):
        self.mumbaip.config(bg="yellow")
        self.delhip.config(bg=self.orig_color)
        self.chennaip.config(bg=self.orig_color)
        self.kolkatap.config(bg=self.orig_color)
        self.code=2
        self.dateSelection()
        
    def chennaippredict(self):
        self.chennaip.config(bg="yellow")
        self.delhip.config(bg=self.orig_color)
        self.mumbaip.config(bg=self.orig_color)
        self.kolkatap.config(bg=self.orig_color)
        self.code=3
        self.dateSelection()
    
    def kolkatappredict(self):
        self.kolkatap.config(bg="yellow")
        self.delhip.config(bg=self.orig_color)
        self.chennaip.config(bg=self.orig_color)
        self.delhip.config(bg=self.orig_color)
        self.code=4
        self.dateSelection()
    def delhidpredict(self):
        self.delhid.config(bg="yellow")
        self.chennaid.config(bg=self.orig_color)
        self.mumbaid.config(bg=self.orig_color)
        self.kolkatad.config(bg=self.orig_color)
        self.code=5
        self.dateSelection1()
        
    def mumbaidpredict(self):
        self.mumbaid.config(bg="yellow")
        self.delhid.config(bg=self.orig_color)
        self.chennaid.config(bg=self.orig_color)
        self.kolkatad.config(bg=self.orig_color)
        self.code=6
        self.dateSelection1()
        
    def chennaidpredict(self):
        self.chennaid.config(bg="yellow")
        self.delhid.config(bg=self.orig_color)
        self.mumbaid.config(bg=self.orig_color)
        self.kolkatad.config(bg=self.orig_color)
        self.code=7
        self.dateSelection1()
    
    def kolkatadpredict(self):
        self.kolkatad.config(bg="yellow")
        self.delhid.config(bg=self.orig_color)
        self.mumbaid.config(bg=self.orig_color)
        self.chennaid.config(bg=self.orig_color)
        self.code=8
        self.dateSelection1()    
        
    def delhicppredict(self):
        self.delhicp.config(bg="yellow")
        self.mumbaicp.config(bg=self.orig_color)
        self.chennaicp.config(bg=self.orig_color)
        self.kolkatacp.config(bg=self.orig_color) 
        self.code=1
        self.dateSelection3()
    
    def mumbaicppredict(self):
        self.mumbaicp.config(bg="yellow")
        self.delhicp.config(bg=self.orig_color)
        self.chennaicp.config(bg=self.orig_color)
        self.kolkatacp.config(bg=self.orig_color)
        self.code=2
        self.dateSelection3()
        
    def chennaicppredict(self):
        self.chennaicp.config(bg="yellow")
        self.delhicp.config(bg=self.orig_color)
        self.mumbaicp.config(bg=self.orig_color)
        self.kolkatacp.config(bg=self.orig_color)
        self.code=3
        self.dateSelection3()
    
    def kolkatacppredict(self):
        self.kolkatacp.config(bg="yellow")
        self.delhicp.config(bg=self.orig_color)
        self.chennaicp.config(bg=self.orig_color)
        self.delhicp.config(bg=self.orig_color)
        self.code=4
        self.dateSelection3()
    def delhicdpredict(self):
        self.delhicd.config(bg="yellow")
        self.chennaicd.config(bg=self.orig_color)
        self.mumbaicd.config(bg=self.orig_color)
        self.kolkatacd.config(bg=self.orig_color)
        self.code=5
        self.dateSelection4()
        
    def mumbaicdpredict(self):
        self.mumbaicd.config(bg="yellow")
        self.delhicd.config(bg=self.orig_color)
        self.chennaicd.config(bg=self.orig_color)
        self.kolkatacd.config(bg=self.orig_color)
        self.code=6
        self.dateSelection4()
        
    def chennaicdpredict(self):
        self.chennaicd.config(bg="yellow")
        self.delhicd.config(bg=self.orig_color)
        self.mumbaicd.config(bg=self.orig_color)
        self.kolkatacd.config(bg=self.orig_color)
        self.code=7
        self.dateSelection4()
    
    def kolkatacdpredict(self):
        self.kolkatacd.config(bg="yellow")
        self.delhicd.config(bg=self.orig_color)
        self.mumbaicd.config(bg=self.orig_color)
        self.chennaicd.config(bg=self.orig_color)
        self.code=8
        self.dateSelection4()    
        
        
    def prdvalue1(self):
        self.predval=0
        self.monthval=self.getMonth(self.SelectedMonthName.get())
        d1=str(self.SelectedYear.get())+"-"+str(self.monthval)+"-"+str(self.SelectedDay.get())
        d2=str(self.DefaultYear)+"-"+str(self.DefaultMonthNumber)+"-"+str(self.DefaultDayOfMonth)
        
        datedif=self.days_between(d1,d2)
        #print(datedif)
        if(datedif>=30):
            msg="Please Select a Different Date"
            ms.showinfo("WARNING",msg)
        else:
            self.predval=predict[self.code-1][datedif-1]
            
            Label(self.second,text="Predicted Petrol Price is:",bg='white',font=('',18)).grid(row=4,column=1)
            Label(self.second,text="Rs: "+str(self.predval),font=('',18),padx=5,bg='white').grid(row=4,column=2)
        #if(self.code is 1):
            
        
    
    def prdvalue2(self):
        self.predval1=0
        self.monthval=self.getMonth(self.SelectedMonthName1.get())        
        d1=str(self.SelectedYear1.get())+"-"+str(self.monthval)+"-"+str(self.SelectedDay1.get())
        d2=str(self.DefaultYear)+"-"+str(self.DefaultMonthNumber)+"-"+str(self.DefaultDayOfMonth)
        datedif=self.days_between(d1,d2)
        #print(datedif)
        if(datedif>=30):
            msg="Please Select a Different Date"
            ms.showinfo("WARNING",msg)
        else:
            self.predval1=predict[self.code-1][datedif-1]   
        
            Label(self.second,text="Predicted Diesel Price is:",bg='white',font=('',18)).grid(row=8,column=1)
            Label(self.second,text="Rs "+str(self.predval1),font=('',18),padx=5,bg='white').grid(row=8,column=2)

    def prdvalue3(self):
        mon=self.getMonth(self.SelectedMonthName11.get())
        date1="2017-06-01"
        date2=str(self.SelectedYear11.get())+"-"+str(mon)+"-"+"01"
        monrem=self.months_between(date1,date2)
        crval=float(self.crudeval.get())
        print(crval)
        c=reg_m(y[self.code-1], xcrude)
        predicted_value=predict_mult(c,monrem,crval)
        Label(self.second,text="Predicted Petrol Price is:",font=('',18),bg='white').grid(row=13,column=1)
        Label(self.second,text="Rs "+str(predicted_value),font=('',18),padx=5,bg='white').grid(row=13,column=2)        
    
    def prdvalue4(self):
        mon=self.getMonth(self.SelectedMonthName12.get())
        date1="2017-06-01"
        date2=str(self.SelectedYear12.get())+"-"+str(mon)+"-"+"01"
        monrem=self.months_between(date1,date2)
        crval=float(self.crudeval1.get())
        c=reg_m(y[self.code-1], xcrude)
        predicted_value1=predict_mult(c,monrem,crval)
        Label(self.second,text="Predicted Petrol Price is:",font=('',18),bg='white').grid(row=17,column=1)
        Label(self.second,text="Rs "+str(predicted_value1),font=('',18),padx=5,bg='white').grid(row=17,column=2)             
    
    
    def update_days(self):
        maxdays = int(self.DaysInMonth[self.SelectedMonthName.get()])
        self.DaySpinBox.config(to=maxdays)
    def update_days1(self):
        maxdays = int(self.DaysInMonth[self.SelectedMonthName.get()])
        self.DaySpinBox1.config(to=maxdays)
    
    def days_between(self,d1, d2):
        d1 = datetime.strptime(d1, "%Y-%m-%d")
        d2 = datetime.strptime(d2, "%Y-%m-%d")
        return abs((d2 - d1).days)
    def months_between(self,date1,date2):
        date1 = datetime.strptime(str(date1), '%Y-%m-%d')
        date2 = datetime.strptime(str(date2), '%Y-%m-%d')
        r = relativedelta.relativedelta(date2, date1)
        return(r.months)
   
    def plot (self):
        x=np.array ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        v= np.array ([16,16.31925,17.6394,16.003,17.2861,17.3131,19.1259,18.9694,22.0003,22.81226])
        p= np.array ([16.23697,     17.31653,     17.22094,     17.68631,     17.73641 ,    18.6368,
            19.32125,     19.31756 ,    21.20247  ,   22.41444   ,  22.11718  ,   22.12453])

        fig = Figure(figsize=(6,6))
        a = fig.add_subplot(111)
        a.scatter(v,x,color='red')
        a.plot(p, range(2 +max(x)),color='blue')
        a.invert_yaxis()

        a.set_title ("Estimation Grid", fontsize=16)
        a.set_ylabel("Y", fontsize=14)
        a.set_xlabel("X", fontsize=14)

        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.get_tk_widget().pack()
        canvas.draw()
    def admin_login(self):
        #self.first.pack_forget()
        self.userframe=Frame(self.master,padx=10,bg='white')
        Label(self.userframe,text = 'User name: ',font = ('',20),pady=5,padx=5,bg='white').grid(sticky = W)
        Entry(self.userframe,bd = 5,textvariable=self.username,font = ('',15)).grid(row=0,column=1)
        #adname.grid(row=0,column=1)
        Label(self.userframe,text = 'Password:',font = ('',20),pady=5,padx=5,bg='white').grid(row=1,sticky=W)
        Entry(self.userframe,bd = 5,textvariable=self.password,font = ('',15),show = '*').grid(row=1,column=1)
        Button(self.userframe,text = ' Login ',bd = 5 ,font = ('',15),padx=5,pady=5,command=self.check_user).grid(sticky=E)
        Button(self.userframe,text='Sign up',bd=5,font=('',15),padx=5,pady=5).grid(sticky=N,row=2,column=1)
        self.userframe.pack()    

    def check_user(self):
        uname=['srivignesh','sridhar','lakshman','sandhru','abinaya']
        pwd=['sri281999','sridhar','lakshman','sandhru','abi']
        cnt=0
        for i in range(len(uname)):
            if(self.username.get()== uname[i]):
                cnt=1
                print("check")
                #print('Successfully logged in as'+self.username.get())
                if(self.password.get()==pwd[i]):
                    cnt=2
        if(cnt==1):
            ms.showinfo("WARNING","INCORRECT PASSWORD")
        elif(cnt==0):
            ms.showinfo("WARNING","USERNAME IS INCORRECT")
        elif(cnt==2):
            ms.showinfo('SUCCESS','\t'+self.username.get()+'\n you are logged in successfully')
            self.userframe.pack_forget()
            self.username.set('')
            self.password.set('')
            self.main_ui()


        
def Main_Ui():
    root = Tk()
    root.title("FUEL PRICE HIKE PREDICTION AND ANALYSIS")
    root.geometry('1366x760')
    root.configure(background='white')
    fd_lbl=Label(root,text="FUEL PRICE HIKE ANALYSIS",font = ('',35),pady = 7,bg='#ff6348')
    fd_lbl.pack(fill=X)
    d=design(root)
    d.admin_login()
    root.mainloop()
    
Main_Ui()

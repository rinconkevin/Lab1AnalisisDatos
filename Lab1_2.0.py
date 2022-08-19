#Interfaz
from tkinter import ttk, Tk, Frame,Button 
import tkinter as tk

#Graficas
import pandas as pd
import matplotlib.pyplot as plot
from  scipy import stats
import numpy  as np
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk) 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from statistics import *
import scipy.stats as stats
from scipy.stats import kurtosis

main_window = tk.Tk()

#indicamos la ruta del archivo y lo leemos con pandas
url= "abalone.csv"
datos = pd.read_csv(url)

#asignamos las columnas de la tabla
columnas = ['Sexo', 'Longitud', 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
#ingresar las columnas
datos.columns = columnas


# ------------------------------ Funcion Principal ----------------------------
def hallarAtipicos(datos, columnas):
    valor = 999
    contador = 0;
    Atipicos1 = []
    k = comboConstante.get();
    if(k == ""):
        k = "1.5"
    for i in range(len(datos["Longitud"])):
        Atipicos1.append(0);
    
    for i in columnas:
        if(i != "Sexo"):    
            p1 = np.quantile(datos[i], 0.25)
            u1 = np.quantile(datos[i], 0.75)
            
            RI1 = u1 - p1
            
            Lp11 = p1 - (float(k) * RI1)
            Lp21 = u1 + (float(k) * RI1)
    
            for j in datos[i]:
                if(j<Lp11 or j>Lp21):
                    Atipicos1[contador] = valor
                    contador = contador + 1
            contador = 0
            
    return Atipicos1

def EliminarDatosAtipicos(datos1, Atipicos):
    contador = 0
    for i in Atipicos:
        if(i == 999):
            datos1 = datos1.drop(index = [contador])
        contador = contador + 1
    return datos1

def Graficar1(datos, columna):
    ventana = Tk()
    ventana.geometry('990x325')
    ventana.wm_title('Graficas Matplotlib')
    ventana.minsize(width=950,height=325)
    
    frame = Frame(ventana,  bg='blue')
    frame.grid(column=0,row=0, sticky='nsew')
    
    fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
    sharey=True, facecolor='#00f9f844')
    fig.suptitle(f'Historama de {columna}')
    axs.hist(datos[columna])
    canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0)
    
    fig = plot.hist(datos[columna])
    plot.subplots()
            
def Graficar2(datos, columnas):
    ventana = Tk()
    ventana.geometry('990x325')
    ventana.wm_title('Graficas Matplotlib')
    ventana.minsize(width=950,height=325)
    
    frame = Frame(ventana,  bg='blue')
    frame.grid(column=0,row=0, sticky='nsew')
    
    fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
    sharey=True, facecolor='#00f9f844')
    fig.suptitle(f'Cajas y bigotes de {columnas}')
    axs.boxplot(datos[columnas])
    canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0)
    
    print("sex mode")
    plot.boxplot(datos[columnas])
    plot.subplots()
def Graficar3(datos, columnas):
    print("111")
    
    ventana = Tk()
    ventana.geometry('990x325')
    ventana.wm_title('Graficas Matplotlib')
    ventana.minsize(width=950,height=325)
    
    frame = Frame(ventana,  bg='blue')
    frame.grid(column=0,row=0, sticky='nsew')
    
    fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
    sharey=True, facecolor='#00f9f844')
    aux = fig.add_subplot(111)
    res = stats.probplot(datos[columnas], dist = stats.norm, plot = aux)
    #s.boxplot(datos[columnas])
    canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0)
    """
    fig= plot.figure()
    ax = fig.add_subplot(111)
    res = stats.probplot(datos[columnas], dist = stats.norm, plot = ax)
    plot.subplots()"""
    
def Graficar4(datos, columnas1, columna2):           
    ventana = Tk()
    ventana.geometry('990x325')
    ventana.wm_title('Graficas Matplotlib')
    ventana.minsize(width=950,height=325)
    
    frame = Frame(ventana,  bg='blue')
    frame.grid(column=0,row=0, sticky='nsew')
    
    fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
    sharey=True, facecolor='#00f9f844')
    fig.suptitle(f'Historama de {columnas1} - {columna2}')
    axs.xcorr(datos[columnas1], datos[columna2])
    canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
    canvas.draw()
    canvas.get_tk_widget().grid(column=0, row=0)
    
    fig = plot.xcorr(datos[columnas1], datos[columna2])
    plot.subplots()
    
def Graficar5(datos, R1, R2, R3, R4, R5, R6, R7, R8, SALIDA, N):
    print("hola")
    if(N == "1"):
        X=datos[[R1]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
        canvas.get_tk_widget().grid(column=0, row=0)
    elif(N == "2"):
        X=datos[[R1,R2]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "3"):
        X=datos[[R1,R2, R3]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "4"):
        X=datos[[R1,R2, R3, R4]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "5"):
        X=datos[[R1,R2, R3, R4, R5]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "6"):
        X=datos[[R1,R2, R3, R4, R5, R6]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "7"):
        X=datos[[R1,R2, R3, R4, R5, R6, R7]]
        Y=datos[SALIDA]
        X_train, X_test, y_train, y_test = train_test_split(
                                                X,
                                                Y,
                                                train_size   = 0.5,
                                            )
        modelo = LinearRegression()
        modelo.fit(X =(X_train), y = y_train)
        
        ventana = Tk()
        ventana.geometry('990x325')
        ventana.wm_title('Graficas Matplotlib')
        ventana.minsize(width=950,height=325)
        
        frame = Frame(ventana,  bg='blue')
        frame.grid(column=0,row=0, sticky='nsew')
        
        fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
        sharey=True, facecolor='#00f9f844')
        fig.suptitle(f'Cajas y bigotes de {columnas}')
        axs.Scatter(X_test, y_test)
        canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
        canvas.draw()
    elif(N == "8"):
          X=datos[[R1,R2, R3, R4, R5, R6, R7, R8]]
          Y=datos[SALIDA]
          X_train, X_test, y_train, y_test = train_test_split(
                                                  X,
                                                  Y,
                                                  train_size   = 0.5,
                                              )
          modelo = LinearRegression()
          modelo.fit(X =(X_train), y = y_train)  
          
          ventana = Tk()
          ventana.geometry('990x325')
          ventana.wm_title('Graficas Matplotlib')
          ventana.minsize(width=950,height=325)
          
          frame = Frame(ventana,  bg='blue')
          frame.grid(column=0,row=0, sticky='nsew')
          
          fig, axs = plot.subplots(dpi=80, figsize=(13, 4),
          sharey=True, facecolor='#00f9f844')
          fig.suptitle(f'Cajas y bigotes de {columnas}')
          axs.Scatter(X_test, y_test)
          canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
          canvas.draw()
def  Graficar6(datos):
    def datosEstadisticos(datos):
        lista_datos = []
        lista_datos.append(mean(datos))
        lista_datos.append(mode(datos))
        lista_datos.append(median(datos))
        lista_datos.append(stats.kurtosis(datos))
        lista_datos.append(stats.skew(datos))
        
        return lista_datos
    list_length=datosEstadisticos(datos['Longitud'])
    list_Diameter=datosEstadisticos(datos['Diametro'])
    list_Height=datosEstadisticos(datos['Altura'])
    list_Whole_weight=datosEstadisticos(datos['Peso entero'])
    list_Shucked_weight=datosEstadisticos(datos['Peso desbullado'])
    list_Viscera_weight=datosEstadisticos(datos['Peso de vísceras'])
    list_Shell_weight=datosEstadisticos(datos['Peso de la cáscara'])
    list_Rings=datosEstadisticos(datos['Anillos'])
    #"Longitud", 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"
    ventana_2 = tk.Tk()
    ventana_2.title("Data analytics and artificial intelligence")
    
    #titulo
    
    
    label_1 = tk.Label(ventana_2,text="Columm's Name",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_1.grid(padx=10, pady=10, row=1, column=0,)
    
    
    label_2 = tk.Label(ventana_2,text="Longitud",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_2.grid(padx=10, pady=10, row=2, column=0, )
    
    label_3 = tk.Label(ventana_2,text="Diametro",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_3.grid(padx=10, pady=10, row=3, column=0, )
    
    label_4 = tk.Label(ventana_2,text="Altura",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_4.grid(padx=10, pady=10, row=4, column=0, )
    
    label_5 = tk.Label(ventana_2,text="Peso entero",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_5.grid(padx=10, pady=10, row=5, column=0, )
    
    label_6 = tk.Label(ventana_2,text="Peso desbullado",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_6.grid(padx=10, pady=10, row=6, column=0, )
    
    label_7 = tk.Label(ventana_2,text="Peso de vísceras",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_7.grid(padx=10, pady=10, row=7, column=0, )
    
    label_8 = tk.Label(ventana_2,text="Peso de la cáscara",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_8.grid(padx=10, pady=10, row=8, column=0, )
    
    label_9 = tk.Label(ventana_2,text="Anillos",
                              fg="blue",
                              font="consolas 12 bold",borderwidth=3)
    label_9.grid(padx=10, pady=10, row=9, column=0, )
    
    
    
    label_10 = tk.Label(ventana_2,text="Mediana",
                              fg="blue",
                              font="consolas 12 bold",)
    label_10.grid(padx=10, pady=10, row=1, column=1, )
    
    label_11 = tk.Label(ventana_2,text="Moda",
                              fg="blue",
                              font="consolas 12 bold",)
    label_11.grid(padx=10, pady=10, row=1, column=2, )
    
    label_12 = tk.Label(ventana_2,text="Media",
                              fg="blue",
                              font="consolas 12 bold",)
    label_12.grid(padx=10, pady=10, row=1, column=3, )
    
    label_13 = tk.Label(ventana_2,text="Kurtosis",
                              fg="blue",
                              font="consolas 12 bold",)
    label_13.grid(padx=10, pady=10, row=1, column=4, )
    
    label_14 = tk.Label(ventana_2,text="Skewness",
                              fg="blue",
                              font="consolas 12 bold",)
    label_14.grid(padx=10, pady=10, row=1, column=5, )
    
    len_mean = tk.Label(ventana_2,text=str(list_length[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=2, column=1)
    len_mode = tk.Label(ventana_2,text=str(list_length[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=2, column=2)
    len_median = tk.Label(ventana_2,text=str(list_length[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=2, column=3)
    len_kurtosis = tk.Label(ventana_2,text=str(list_length[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=2, column=4)
    len_skew = tk.Label(ventana_2,text=str(list_length[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=2, column=5)
    
    len_mean2 = tk.Label(ventana_2,text=str(list_Diameter[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=3, column=1)
    len_mode2 = tk.Label(ventana_2,text=str(list_Diameter[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=3, column=2)
    len_median2 = tk.Label(ventana_2,text=str(list_Diameter[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=3, column=3)
    len_kurtosis2 = tk.Label(ventana_2,text=str(list_Diameter[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=3, column=4)
    len_skew2 = tk.Label(ventana_2,text=str(list_Diameter[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=3, column=5)
    
    len_mean3 = tk.Label(ventana_2,text=str(list_Height[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=4, column=1)
    len_mode3 = tk.Label(ventana_2,text=str(list_Height[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=4, column=2)
    len_median3 = tk.Label(ventana_2,text=str(list_Height[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=4, column=3)
    len_kurtosis3 = tk.Label(ventana_2,text=str(list_Height[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=4, column=4)
    len_skew3 = tk.Label(ventana_2,text=str(list_Height[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=4, column=5)
    
    len_mean4 = tk.Label(ventana_2,text=str(list_Whole_weight[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=5, column=1)
    len_mode4 = tk.Label(ventana_2,text=str(list_Whole_weight[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=5, column=2)
    len_median4 = tk.Label(ventana_2,text=str(list_Whole_weight[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=5, column=3)
    len_kurtosis4 = tk.Label(ventana_2,text=str(list_Whole_weight[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=5, column=4)
    len_skew4 = tk.Label(ventana_2,text=str(list_Whole_weight[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=5, column=5)
    
    len_mean5 = tk.Label(ventana_2,text=str(list_Shucked_weight[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=6, column=1)
    len_mode5 = tk.Label(ventana_2,text=str(list_Shucked_weight[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=6, column=2)
    len_median5 = tk.Label(ventana_2,text=str(list_Shucked_weight[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=6, column=3)
    len_kurtosis5 = tk.Label(ventana_2,text=str(list_Shucked_weight[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=6, column=4)
    len_skew5 = tk.Label(ventana_2,text=str(list_Shucked_weight[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=6, column=5)
    
    len_mean6 = tk.Label(ventana_2,text=str(list_Viscera_weight[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=7, column=1)
    len_mode6 = tk.Label(ventana_2,text=str(list_Viscera_weight[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=7, column=2)
    len_median6 = tk.Label(ventana_2,text=str(list_Viscera_weight[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=7, column=3)
    len_kurtosis6 = tk.Label(ventana_2,text=str(list_Viscera_weight[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=7, column=4)
    len_skew6 = tk.Label(ventana_2,text=str(list_Viscera_weight[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=7, column=5)
    
    len_mean7 = tk.Label(ventana_2,text=str(list_Shell_weight[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=8, column=1)
    len_mode7 = tk.Label(ventana_2,text=str(list_Shell_weight[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=8, column=2)
    len_median7 = tk.Label(ventana_2,text=str(list_Shell_weight[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=8, column=3)
    len_kurtosis7 = tk.Label(ventana_2,text=str(list_Shell_weight[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=8, column=4)
    len_skew7 = tk.Label(ventana_2,text=str(list_Shell_weight[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=8, column=5)
    
    len_mean8 = tk.Label(ventana_2,text=str(list_Rings[0]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=9, column=1)
    len_mode8 = tk.Label(ventana_2,text=str(list_Rings[1]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=9, column=2)
    len_median8 = tk.Label(ventana_2,text=str(list_Rings[2]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=9, column=3)
    len_kurtosis8 = tk.Label(ventana_2,text=str(list_Rings[3]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=9, column=4)
    len_skew8 = tk.Label(ventana_2,text=str(list_Rings[4]),bg="White",fg="black",font="consolas 14 bold",state="normal").grid(padx=10, pady=10, row=9, column=5)
    
def show_selection():
    tipo = comboTpGrafica.get()
    columna1 = comboTpDatos1.get()
    columna2 = comboTpDatos2.get()
    atipicos = comboDatosAtipicos.get()
    
    Atipicos = hallarAtipicos(datos, columnas)
    datos2 = EliminarDatosAtipicos(datos, Atipicos)
    
    if(tipo == "Histograma"):
        if(atipicos == "Si"):        
            Graficar1(datos, columna1)
        else:
            Graficar1(datos2, columna1)
    elif(tipo == "Cajas y Bigotes"):
        if(atipicos == "Si"):        
            Graficar2(datos, columna1)
        else:
            Graficar2(datos2, columna1)
    elif(tipo == "Normal"):    
        if(atipicos == "Si"):        
            Graficar3(datos, columna1)
        else:
            Graficar3(datos2, columna1)
    elif(tipo == "Combinaciones"):
        if(atipicos == "Si"):        
            Graficar4(datos, columna1, columna2)
        else:
            Graficar4(datos2, columna1, columna2)
    elif(tipo == "Regresion"):
        R1 = ComboRE1.get()
        R2 = ComboRE2.get()
        R3 = ComboRE3.get()
        R4 = ComboRE4.get()
        R5 = ComboRE5.get()
        R6 = ComboRE6.get()
        R7 = ComboRE7.get()
        R8 = ComboRE8.get()
        SALIDA = ComboSalida.get()
        N = ComboNVariables.get()
        if(atipicos == "Si"):        
            Graficar5(datos, R1, R2, R3, R4, R5, R6, R7, R8, SALIDA, N)
        else:
            Graficar5(datos2, R1, R2, R3, R4, R5, R6, R7, R8, SALIDA, N)
    elif(tipo == "Tabla Estadistica"):      
        if(atipicos == "Si"):        
            Graficar6(datos)
        else:
            Graficar6(datos2)


#----------------------------------------- Principal --------------------------



main_window.config(width=1200, height=700)
main_window.title("Proyecto")
main_window.resizable(width = False, height = False)
fondo = tk.PhotoImage(file= "Fondo.PNG")
fondo1 = tk.Label(main_window, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)

#Seleccionar el tipo de grafica
def selectionDatos(event):
    selection = comboTpGrafica.get()
    if(selection == "Combinaciones"):
        comboTpDatos2["values"]=["Longitud", 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
    elif(selection == "Regresion"):
        ComboNVariables["values"]= ["1","2","3","4","5","6","7","8"]
        ComboSalida["values"]= ["Longitud", 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
    else:
        comboTpDatos2["values"]=[]
        ComboNVariables["values"]=[]
        ComboSalida["values"]=[]
#"1","2","3","4","5","6","7","8"
comboTpGrafica = ttk.Combobox(values=["Cajas y Bigotes", "Histograma", "Normal", "Combinaciones", "Regresion", "Tabla Estadistica"])
comboTpGrafica.bind("<<ComboboxSelected>>", selectionDatos)
comboTpGrafica.place(x=250, y=100)
comboTpGrafica.configure(width=43, height=10)

#Seleccionar las variables
comboTpDatos1 = ttk.Combobox(
    state="readonly",
    values=["Longitud", 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
)
comboTpDatos1.place(x=70, y=270)
comboTpDatos1.configure(width=35, height=10)

comboTpDatos2 = ttk.Combobox(
    state="readonly",
    values=[]
)
comboTpDatos2.place(x=480, y=270)
comboTpDatos2.configure(width=35, height=10)

comboDatosAtipicos = ttk.Combobox(
    state="readonly",
    values=["Si","No"]
)
comboDatosAtipicos.place(x=70, y=400)
comboDatosAtipicos.configure(width=35, height=10)

comboConstante = ttk.Combobox(
    text = "1.5",
    state="readonly",
    values=["1,5","2", "2,5", "3", "3,5", "4"]
)
comboConstante.place(x=480, y=400)
comboConstante.configure(width=35, height=10)

#-------------------- Regresion --------------------------

def Regres():
    selection = ComboNVariables.get()
    ComboRE1["values"] = []
    ComboRE2["values"] = []
    ComboRE3["values"] = []
    ComboRE4["values"] = []
    ComboRE5["values"] = []
    ComboRE6["values"] = []
    ComboRE7["values"] = []
    ComboRE8["values"] = []
    
    Regre = ["Longitud", 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
    if(selection == "1"):
        ComboRE1["values"] = Regre
    elif(selection == "2"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
    elif(selection == "3"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE3["values"] = Regre
    elif(selection == "4"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE3["values"] = Regre
        ComboRE4["values"] = Regre
    elif(selection == "5"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE3["values"] = Regre
        ComboRE4["values"] = Regre
        ComboRE5["values"] = Regre
    elif(selection == "6"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE3["values"] = Regre
        ComboRE4["values"] = Regre
        ComboRE5["values"] = Regre
        ComboRE6["values"] = Regre
    elif(selection == "7"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE4["values"] = Regre
        ComboRE5["values"] = Regre
        ComboRE6["values"] = Regre
        ComboRE7["values"] = Regre
        ComboRE3["values"] = Regre
    elif(selection == "8"):
        ComboRE1["values"] = Regre
        ComboRE2["values"] = Regre
        ComboRE3["values"] = Regre
        ComboRE4["values"] = Regre
        ComboRE5["values"] = Regre
        ComboRE6["values"] = Regre
        ComboRE7["values"] = Regre
        ComboRE8["values"] = Regre

        
ComboRE7 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE7.place(x=800, y=420)
ComboRE7.configure(width=20, height=10)

ComboRE8 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE8.place(x=980, y=420)
ComboRE8.configure(width=20, height=10)

ComboRE5 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE5.place(x=800, y=340)
ComboRE5.configure(width=20, height=10)

ComboRE6 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE6.place(x=980, y=340)
ComboRE6.configure(width=20, height=10)

ComboRE3 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE3.place(x=800, y=260)
ComboRE3.configure(width=20, height=10)

ComboRE4 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE4.place(x=980, y=260)
ComboRE4.configure(width=20, height=10)


ComboRE1 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE1.place(x=800, y=180)
ComboRE1.configure(width=20, height=10)

ComboRE2 = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboRE2.place(x=980, y=180)
ComboRE2.configure(width=20, height=10)

ComboNVariables = ttk.Combobox(values=[])
ComboNVariables.place(x=900, y=100)
ComboNVariables.configure(width=20, height=10)

ComboSalida = ttk.Combobox(
    state="readonly",
    values=[]
)
ComboSalida.place(x=900, y=500)
ComboSalida.configure(width=20, height=10)

buttonActu = tk.Button(command=Regres, width= 5, height=1)
buttonActu.place(x=1050, y=100)


button = tk.Button(command=show_selection, width= 34, height=3)
button.place(x=480, y=590)
main_window.mainloop()
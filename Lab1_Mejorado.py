from tkinter import Tk, Frame,Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy  as np
import pandas as pd



#indicamos la ruta del archivo y lo leemos con pandas
url= "abalone.csv"
datos = pd.read_csv(url)
#asignamos las columnas de la tabla
colimnas = ['Sexo', 'Longitud', 'Diametro','Altura','Peso entero','Peso desbullado', "Peso de vísceras", "Peso de la cáscara", "Anillos"]
#ingresar las columnas
datos.columns = colimnas



ventana = Tk()
ventana.geometry('990x325')
ventana.wm_title('Graficas Matplotlib')
ventana.minsize(width=950,height=325)



frame = Frame(ventana,  bg='blue')
frame.grid(column=0,row=0, sticky='nsew')



nombres = ['Azul', 'Rojo', 'Verde', 'Magenta','Negro']
colores = ['blue','red','green','magenta', 'black']
tamaño = [15, 25, 10, 20, 30]



fig, axs = plt.subplots(1,4 , dpi=80, figsize=(13, 4),
    sharey=True, facecolor='#00f9f844')



fig.suptitle('Graficas Matplotlib')




axs[0].hist(datos["Longitud"])





#fig= plot.figure()
#ax = fig.add_subplot(111)
#res = stats.probplot(datos["Diametro"], dist = stats.norm, plot = ax)




canvas = FigureCanvasTkAgg(fig, master = frame)  # Crea el area de dibujo en Tkinter
canvas.draw()
canvas.get_tk_widget().grid(column=0, row=0)




ventana.mainloop()
import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'Nombre':['Jhon','Maria','Pedro','Jenifer','Bob','Lisa','Jose'],
    'Edad':[23,78,22,19,45,33,20],
    'Ciudad':['Bogota','Medellin','Bogota','Medellin','Bogota','Armenia','Armenia'],
    'Numero niños':[2,0,0,3,2,1,4],
    'Numero mascotas':[5,1,0,5,2,2,3],
}

tabla = pd.DataFrame(datos)

tabla[['Edad']].plot(kind='hist',bins=[0,20,40,60,80,100],rwidth=0.8)

plt.show()
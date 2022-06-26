#Setja inn panda packan fyrir exel import
import pandas as pd

#Setja inn pyplot fyrir data visualysation
from matplotlib import pyplot as plt

#Lesa in exelskjalið
ExelRead  = pd.read_excel("C:\\Users\\sirjo\\Desktop\\Prototype\\ExelPrufa.xlsx", sheet_name = "Sheet1")

#Taka út röð af tölum 
column = ExelRead["Dalkur 2"]

row = [1,2,3,4,5,6,7,8,9,10]

plt.plot(row, column)
plt.show()


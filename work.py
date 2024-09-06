import math

print()
#Environment Variables
annualConsuption = 12000
averageLight = 5 #horas
panelEffiency = 0.15
panelSurface = 1.6
averageRadiation = 5

#Daily Power
dailyPower = (panelSurface) * (averageRadiation) * (panelEffiency)
print(f"Potencia Diaria: {dailyPower} Kwh")

#Saber el uso de las funciones.
#Ceil

#Annual Power
annualPower = dailyPower * 365 
print(f"Potencia Anual: {annualPower} Kwh")

#Number Of Panels. Round to 1 decimal.
numberOfPanels = (annualConsuption / annualPower)
print(f"Número Paneles: {math.ceil(numberOfPanels)}")

print("Extra")
print()

newAnnualConsuption = float(input("Ingresa Consumo Anual: "))
#--------------------------------------------------------------
newPanelEfficiency = float(input("Ingresa Eficiencia del Panel %: "))
#--------------------------------------------------------------
newPanelSurface = float(input("Ingresa Superficie Promedio del Panel: "))
#--------------------------------------------------------------
newAverageRadiation = float(input("Ingresa Radiación Solar Promedio: "))
#--------------------------------------------------------------
newAverageLight = float(input("Ingresa Horas Promedio de Sol / Día: "))

print()

newDailyPower = (newPanelSurface) * (newAverageRadiation) * (newPanelEfficiency / 100)
print(f"Potencia Diaria: {newDailyPower} Kwh")

newAnnualPower = newDailyPower * 365
print(f"Potencia Anual: {newAnnualPower} Kwh")

newNumberOfPanels = newAnnualConsuption / newAnnualPower
aproxVar = math.ceil(newNumberOfPanels)
print(f"Número de Paneles: {aproxVar}")

totalArea = (newPanelSurface * newNumberOfPanels)
print(f"El área necesaria para instalar {aproxVar} es de: {round(totalArea, 2)} Mts Cuadrados.")
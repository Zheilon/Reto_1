import math

print()
#EnvironmentVariables
annualConsuption = 12000
averageLight = 5 #horas
panelEffiency = 0.15
panelSurface = 1.6
#averageRadiation = averageLight / panelSurface / 1
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
#-------------------------------
newPanelEfficiency = float(input("Ingresa Eficiencia del Panel %: "))
#-------------------------------
newPanelSurface = float(input("Ingresa Superficie Promedio del Panel: "))
#-------------------------------
newAverageRadiation = float(input("Ingresa Radiación Solar Promedio: "))
#-------------------------------
newAverageLight = float(input("Ingresa Horas Promedio de Sol / Día: "))

print()

newDailyPower = (newPanelSurface) * (newAverageRadiation) * (newPanelEfficiency / 100)
print(f"Potencia Diaria: {newDailyPower}")

newAnnualPower = newDailyPower * 365
print(f"Potencia Anual: {newAnnualPower}")

newNumberOfPanels = newAnnualConsuption / newAnnualPower
print(f"Número de Paneles: {newNumberOfPanels}")
















__author__ = 'claytobw01'

Distance = 100
NameOfRunner = ""
SpeedOfRunner = 0
MStoMPH = 2.24
SpeedInMPH = 0
SpeedLimit = 20

NameOfRunner = input ("Name of Runner: ")
TimeTaken = float (input ("Time Taken: "))

SpeedOfRunner = Distance / TimeTaken

SpeedInMPH = SpeedOfRunner * MStoMPH

print (NameOfRunner + "ran the " + Distance + "M race in: " + str (round (SpeedInMPH)))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.ExcelFile('/Users/evanmckinley/Desktop/Environmental Studies/CatchData.xlsx')
trips = pd.read_excel(data, 'Trips')
gallatin = pd.read_excel(data, 'Gallatin River Catches')
madison = pd.read_excel(data, 'Madison River Catches')
hyalite = pd.read_excel(data, 'Hyalite Reservoir Catches')

hy_av_len = hyalite['Length (inches)'].mean()
print(f"Average length: {hy_av_len:.2f} inches")

hy_av_wt = hyalite['Weight (lbs)'].mean()
print(f"Average weight: {hy_av_wt:.2f} pounds")

species_count = []
species = {
    1: "Brook Trout",
    2 : "Cutthroat Trout",
    3 : "Brown Trout",
    4 : "Rainbow Trout",
    5 : "Carp",
    6 : "Whitefish",
    7 : "Largemouth Bass",
    8 : "Burbot",
    9 : "Longnose Sucker"
}
brookie = 0
cuttie = 0
#if hyalite['Species'] == 'Brook Trout':
 #   brookie = 1
 #   species_count.append(brookie)
#elif hyalite['Species'] == 'Cutthroat Trout':
#    cuttie = 2
 #   species_count.append(cuttie)'''

#i = 0
#while i != 7:

   # print("The number", i, "is a", species[i])
   # i += 1

#print(hyalite["Species"] == "Brook Trout")

'''if hyalite['Species'] == "Brook Trout":
    brookie += 1
    species_count.append(brookie)
print(species_count)'''

num_of_species = len(species)
j = 1
for i in range(num_of_species):
    print(j, "is the number paired with the species", species[i])
    j+=1
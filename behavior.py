# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Import the raw data
data = pd.ExcelFile('/Users/evanmckinley/Desktop/Environmental Studies/CatchData.xlsx')
trips = pd.read_excel(data, 'Trips')
gallatin = pd.read_excel(data, 'Gallatin River Catches')
madison = pd.read_excel(data, 'Madison River Catches')
hyalite = pd.read_excel(data, 'Hyalite Reservoir Catches')
canyon = pd.read_excel(data, 'Canyon Ferry Reservoir Catches')


# Length calculations
hy_len = pd.Series(hyalite['Length (inches)']) # A pandas Series of all the lengths in Hyalite Reservoir catches
cf_len = pd.Series(canyon['Length (inches)']) # A pandas Series of all the lengths in the Canyon Ferry Reservoir catches

total_sum = hy_len.sum() + cf_len.sum()
total_count = len(hy_len) + len(cf_len)
average_len = total_sum / total_count
print(f"Overall average length: {average_len:.2f} inches")


hy_av_len = hyalite['Length (inches)'].mean()
print(f"Average length: {hy_av_len:.2f} inches")




# Weight calculations
hy_av_wt = hyalite['Weight (lbs)'].mean()
print(f"Average weight: {hy_av_wt:.2f} pounds")




all_catches = pd.concat(
    [gallatin, madison, hyalite, canyon],
    ignore_index=True # Reset ro index so it's continuous
)

print("\nSpecies count across (sorted by most common):")
print(all_catches["Species"].value_counts().to_string())

print("\nSpecies by water body:")
for sheet_name, df in [
    ("Gallatin River", gallatin),
    ("Madison River", madison),
    ("Hyalite Reservoir", hyalite),
    ("Canyon Ferry Reservoir", canyon)
]:
    if 'Species' in df.columns and not df.empty:
        counts = df['Species'].value_counts()
        if not counts.empty:
            print(f"\n{sheet_name}:")
            print(counts.to_string())
        else:
            print(f"{sheet_name}: No catches recorded")
    else:
        print(f"{sheet_name}: No species data or empty sheet")


# Create a dictionary of species
species_count = Counter(all_catches['Species'].dropna())
species = {
    1 : "Brook Trout",
    2 : "Yellowstone Cutthroat Trout",
    3 : "Brown Trout",
    4 : "Rainbow Trout",
    5 : "Carp",
    6 : "Whitefish",
    7 : "Largemouth Bass",
    8 : "Burbot",
    9 : "Longnose Sucker",
    10 : "Smallmouth Bass",
    11 : "Northern Pike",
    12 : "Lake Trout",
    13 : "Cutbow",
    14 : "Tiger Trout",
    15 : "Arctic Grayling",
    16 : "Mountain Whitefish",
    17 : "Westslope Cutthroat Trout",
    18 : "Yellow Perch",
    19 : "Bluegill",
    20 : "Green Sunfish",
    21 : "Walleye",
    22 : "Channel Catfish"

}

# Find the key for each species name and print how much of each species was caught
print("\nMapped to numbers:")
for sp, count in species_count.items():
    for key, value in species.items():
        if value == sp:
            print(f"{key}: {value} - {count}")
            break

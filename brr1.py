# make bar plot from csv file
import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
# Read CSV file
data = pd.read_csv("data.csv")

# Make bar plot
plt.bar(data['Category'], data['Values'])
plt.xlabel('Category')
plt.ylabel('Values')
plt.title('Bar Plot from CSV')
plt.show()
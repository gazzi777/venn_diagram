import matplotlib.pyplot as plt
from matplotlib_venn import venn3
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
set1 = {'B', 'B', 'C'}
set2 = {'A', 'B', 'D'}
set3 = {'Н', 'E', 'F'}
venn3([set1, set2, set3], ('Gйцуй', 'йцуцйу', 'йцуйуцй'))
plt.show()
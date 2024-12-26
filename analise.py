import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('exams.csv')

df.groupby('lunch')['avarage_Score'].mean().plot(kind='bar')w
plt.show()
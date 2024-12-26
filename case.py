import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('StudentsPerformance .csv')
df.info()

print(df.describe())

def avarage_Score(data):
    result = (data['math score']+ data['reading score']+ data ['writing score']) / 3
    return round(result)
df['avarage_Score'] = df.apply(avarage_Score, axis=1)

df.info()

df.to_csv('exams.csv', index = False)

# df['math score'].plot(kind='hist')
# plt.show()

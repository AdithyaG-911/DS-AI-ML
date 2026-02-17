import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.DataFrame({
    'Transmission': ['Automatic', 'Manual', 'Automatic', 'Manual'],
    'Color': ['Red', 'Blue', 'Green', 'Blue']
})
print("Original Data:\n",df)

le = LabelEncoder()
df['Transmission'] = le.fit_transform(df['Transmission'])
print("Label Encoding for Transmission:\n",df)

df = pd.get_dummies(df, columns=['Color'], drop_first=True)
print("One-Hot Encoding for Color(One Column is Dropped):\n",df)

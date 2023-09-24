import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report
df = pd.read_excel("E:\\Lupus\\updated_lupus_data.xlsx", sheet_name='Sheet1')
# Encode categorical variables
label_encoder = LabelEncoder()
df['Gender'] = label_encoder.fit_transform(df['Gender'])
# Define X (features) and y (target)
X = df.drop(['S.0', 'Lupus +ve', 'Total'], axis=1)
y = df['Lupus +ve']
# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Create a decision tree classifier
clf = DecisionTreeClassifier()
# Fit the classifier to the training data
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)


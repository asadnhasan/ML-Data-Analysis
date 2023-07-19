import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Read the data from a CSV file
data = pd.read_csv('C:/Users/Syed Asad/OneDrive/Desktop/Python Files/ML Swansea Prices/house_data.csv')

# Preprocess the data
label_encoder = LabelEncoder()
data['location_encoded'] = label_encoder.fit_transform(data['location'])

# Split the data into training and testing sets
X = data[['size', 'bedrooms', 'location_encoded']]
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict house prices for the test set
y_pred = model.predict(X_test)

# Check if the test set has more than one sample to compute accuracy
if len(X_test) > 1:
    # Compute and print the accuracy
    accuracy = model.score(X_test, y_test)
    print(f"Accuracy: {accuracy}")
else:
    print("Not enough samples in the test set to compute accuracy.")

# Example usage: Predict the price of a house in Swansea
size = 1000
bedrooms = 2
location = 'swansea central'

# Check if the lowercase location is present in the training data
if location in label_encoder.classes_:
    # Get the corresponding encoded value
    location_encoded = label_encoder.transform([location])[0]

    # Make a prediction
    price_pred = model.predict([[size, bedrooms, location_encoded]])
    print(f"Predicted price: {price_pred[0]}")
else:
    print("Location not found in the training data.")




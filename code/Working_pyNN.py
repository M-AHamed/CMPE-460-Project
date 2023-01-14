import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import backend as K
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
# Load the data
data = pd.read_csv(
    "C:\\Users\\Mohammad\\Desktop\\Uni\\Uni work\\Year 4\\Term 7, fall 2022\\CMPE 460 Deep Learning\\project\\CMPE-460-Project\\dataset\\cars.csv",
    encoding='iso-8859-1')

# drop rows where the price is less than 500
data = data[data['price'] >= 500]

# # Drop the totalPrice column
# data['doornumber'] = data['doornumber'].replace({'four':'4','two':'2'}, regex=True)
# # Drop rows with missing or empty values in the "Doors" column
# data = data[data['doornumber'].str.strip() !='']
# data['doornumber'] = data['doornumber'].astype(int)


def check_missing_values(dataframe):
    missing_values = dataframe.isnull().any()
    if missing_values.any():
        print("Missing values in columns:")
        print(missing_values[missing_values == True])
    else:
        print("No missing values.")


check_missing_values(data)

data

if 'Manufacturer' in data.columns:
    data = data.drop('Manufacturer', axis=1)
else:
    print("Manufacturer column not found")

if 'Model ' in data.columns:
    data = data.drop('Model ', axis=1)
else:
    print("Model  column not found")

data

# list = [car_id,symboling,fuel_type_data, aspiration_data,doorsNumber_data, catagory_data,driveWheels_data, engine_location,wheel_base,car_length, car_width, car_height, car_weight, engine_type ,cylinders_data, engine_size, fuel_system, bore_ratio, stroke, compression, horesepower, peakrpm, citympg, highway_mpg]

print(data)

# Define the list of categorical columns
categorical_cols = [
    'symboling', 'Fuel type', 'aspiration', 'doornumber', 'Category',
    'Drive wheels', 'enginelocation', 'enginetype', 'Cylinders', 'fuelsystem'
]

# Create the main array with car_ID column
main_array = np.array(data['car_ID']).reshape(-1, 1)

# Iterate through columns in the dataframe
for col in data.columns:
    # Check if the column is in the list of categorical columns
    if col in categorical_cols:
        # Perform one-hot encoding on the column
        temp = np.array(pd.get_dummies(data[col]))
    else:
        # Otherwise, reshape the column
        temp = np.array(data[col]).reshape(-1, 1)
    # Stack the column with the main array
    main_array = np.hstack((main_array, temp))

# Remove the car_ID column
main_array = main_array[:, 2:]

# Display the array as a dataframe
pd.DataFrame(main_array)

# Define the features and labels
X = main_array[:, :-1]
y = main_array[:, -1].reshape(-1, 1)

for i, val in enumerate(X):
    for j, value in enumerate(val):
        if isinstance(value, str):
            print("string value found in X at index [{}, {}]: {}".format(
                i, j, value))

xScaler = StandardScaler()
yScaler = StandardScaler()

X_scaled = xScaler.fit_transform(X)
Y_scaled = yScaler.fit_transform(y)

print("Shape of X_data: {}".format(X.shape))
print("Shape of y_data: {}".format(y.shape))
print("==========X_data after rescaling===============")
print(pd.DataFrame(X_scaled).head())
print("==========y_data after rescaling===============")
print(Y_scaled.ravel())

X_train, X_test, y_train, y_test = train_test_split(X_scaled,
                                                    Y_scaled,
                                                    test_size=0.1,
                                                    shuffle=False)
print("Shape of X_train: {}".format(X_train.shape))
print("Shape of X_test: {}".format(X_test.shape))
print("Shape of y_train: {}".format(y_train.shape))
print("Shape of y_test: {}".format(y_test.shape))

model = Sequential()
model.add(Dense(8, activation='relu', input_shape=(None, 57)))
model.add(Dense(4, activation='relu'))
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.summary()
# storing the model structure
model_josn = model.to_json()
with open("model.json", "w") as file:
    file.write(model_josn)
model.save_weights("weights.h5")


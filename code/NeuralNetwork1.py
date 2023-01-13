# ### Start from here
#

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

# def check_missing_values(dataframe):
#     missing_values = dataframe.isnull().any()
#     if missing_values.any():
#         print("Missing values in columns:")
#         print(missing_values[missing_values == True])
#     else:
#         print("No missing values.")

# check_missing_values(data)

# data

if 'Manufacturer' in data.columns:
    data = data.drop('Manufacturer', axis=1)
else:
    print("Manufacturer column not found")

if 'Model ' in data.columns:
    data = data.drop('Model ', axis=1)
else:
    print("Model  column not found")



# data

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
# pd.DataFrame(main_array)

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

history = model.fit(x=X_train,
                    y=y_train,
                    epochs=100,
                    validation_data=(X_test, y_test),
                    verbose=0)

plt.plot(history.history['loss'], label="train_loss")
plt.plot(history.history['val_loss'], label="val_loss")
plt.legend()
plt.show()

# # testing the output from row five as an input
# PREDICT_ROW = 5
# predict_data = main_array[PREDICT_ROW, :].reshape(1, -1)
# print(main_array)
# X_predict = predict_data[:, :-1]
# y_true = predict_data[:, -1]
# predict_data_scaled = xScaler.transform(X_predict)
# y_pred_scaled = model.predict(predict_data_scaled)
# y_pred = yScaler.inverse_transform(y_pred_scaled)
# print("Prediction price result: {}".format(float(y_pred)))
# print("True price: {}".format(float(y_true)))
# print("Percentage error: {}".format(
#     str(float(abs(y_true - y_pred) * 100 / y_true))))

# #----------------------------------------------------------------------------------------------------------

#def predict_price(features):
# Create a dataframe from the input features
# input_df = pd.DataFrame([features], columns=["symboling", "Fuel type", "aspiration", "doornumber", "Category", "Drive wheels", "enginelocation", "enginetype"])
# One-hot encode the categorical columns
#input_df = pd.get_dummies(input_df, columns=["symboling", "Fuel type", "aspiration", "doornumber", "Category", "Drive wheels", "enginelocation", "enginetype"])
# Fill in the missing values for the numerical columns
#input_df = input_df.fillna(input_df.mean())
# Scale the input features
#input_scaled = xScaler.transform(input_df)
# Make a prediction using the trained model
# prediction = model.predict(input_scaled)
# Inverse the transformation of the target variable
# prediction = yScaler.inverse_transform(prediction)
# return prediction

# VERSION 1

# VERSION 2
def preprocessing_data(df):

    data2 = pd.read_csv(
        "C:\\Users\\Mohammad\\Desktop\\Uni\\Uni work\\Year 4\\Term 7, fall 2022\\CMPE 460 Deep Learning\\project\\CMPE-460-Project\\dataset\\cars.csv",
        encoding='iso-8859-1')


    data2 = data2[data2['price'] >= 500]    

    if 'Manufacturer' in data.columns:
        data2 = data2.drop('Manufacturer', axis=1)
    else:
        print("Manufacturer column not found")

    if 'Model ' in data.columns:
        data2 = data2.drop('Model ', axis=1)
    else:
        print("Model  column not found")


    data2 = data2[:-1]
    data2 = data2.append(df)

    categorical_cols = [
        'symboling', 'Fuel type', 'aspiration', 'doornumber', 'Category',
        'Drive wheels', 'enginelocation', 'enginetype', 'Cylinders',
        'fuelsystem'
    ]
    main_array = np.array(data2['car_ID']).reshape(-1, 1)

    # Iterate through columns in the dataframe
    for col in data2.columns:
        # Check if the column is in the list of categorical columns
        if col in categorical_cols:
            # Perform one-hot encoding on the column
            temp = np.array(pd.get_dummies(data2[col]))
        else:
            # Otherwise, reshape the column
            temp = np.array(data2[col]).reshape(-1, 1)
        # Stack the column with the main array
        main_array = np.hstack((main_array, temp))
    print("preprocessign check")

    main_array = main_array[:, 2:]
    X_main = main_array[:, :-1]
    X_main = X_main[:, :-1]

    

    predict_price(X_main)


# predict_data = main_array[PREDICT_ROW, :].reshape(1, -1)
# print(main_array)
# X_predict = predict_data[:, :-1]
# y_true = predict_data[:, -1]


# preprocess the gui data to run it through the model
def predict_price(df):

    predict_data = df[-1, :].reshape(1, -1)

    # last_row = df.iloc[-1]
    # print(last_row)

    print(df)
    X_predict = predict_data[:, :-1]
    y_true = predict_data[:, -1]

    # xScaler = StandardScaler()
    # yScaler = StandardScaler()


    predict_data_scaled = xScaler.transform(X_predict)
    y_pred_scaled = model.predict(predict_data_scaled)
    y_pred = yScaler.inverse_transform(y_pred_scaled)
    print("Prediction price result: {}".format(float(y_pred)))
    print("True price: {}".format(float(y_true)))
    print("Percentage error: {}".format(
        str(float(abs(y_true - y_pred) * 100 / y_true))))

    # return y_pred

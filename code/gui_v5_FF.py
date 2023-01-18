import tkinter as tk
from tkinter import ttk
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
from sklearn.preprocessing import StandardScaler
import h5py

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

from joblib import load
from tkinter import *
# window attributes
window = tk.Tk()
window.title("PriceMatch")
window.configure(background="#F3EFE0")
# styling of the widgets on the gui, and the frame:
s = ttk.Style()
s.configure('frame1.TFrame', background='#F5EDCE')
s.configure("TLabel",
            font=('Helvetica', 12),
            background="#F5EDCE",
            pady=20,
            padx=10)
s.configure("TMenubutton",
            background="#F5EDCE",
            font=('Helvetica', 13),
            pady=20,
            padx=10)
s.configure(
    "TButton",
    font=('calibri', 16, 'bold'),
    foreground='#0A2647',
    # or #3C2A21
    background='#F3EFE0',
    highlightForeground='#579BB1',
    highlightBackground='#579BB1')

font = ("Helvetica", 14)
# frame attributes:
frame1 = ttk.Frame(window, width=800, height=600, style='frame1.TFrame')
frame1.grid(row=0, column=0)

frame2 = ttk.Frame(window)
frame2.grid(row=1, column=0)
# datasets input
guiData1 = pd.read_csv("C:\\Users\\hp\\Desktop\\University\\CMPE 460\\Project_deep\\cars.csv",encoding='iso-8859-1')
# the manufacturer and model file
guiData = pd.read_csv("C:\\Users\\hp\\Desktop\\University\\CMPE 460\\Project_deep\\cars.csv",encoding='iso-8859-1')

guiData = guiData.groupby('Manufacturer')['Model '].apply(
    lambda x: x.unique().tolist()).reset_index()
# store the different manufacturers from the dataframe into a list
manufacturer_options = guiData['Manufacturer']
# display the first item in the list in the drop-down menu
manufactuer_var = manufacturer_options[0]

# clean the data to store it into the different drop down menus
guiData1Category = guiData1.drop_duplicates(subset=['Category'])
guiData1DriveWheels = guiData1.drop_duplicates(subset=['Drive wheels'])
guiData1FuelType = guiData1.drop_duplicates(subset=['Fuel type'])
guiData1DoorsNumber = guiData1.drop_duplicates(subset=['doornumber'])
guiData1NumberOfCylinders = guiData1.drop_duplicates(subset=['Cylinders'])
guiData1Aspiration = guiData1.drop_duplicates(subset=['aspiration'])
guiData1EngineType = guiData1.drop_duplicates(subset=['enginetype'])
guiData1EngineLocation = guiData1.drop_duplicates(subset=['enginelocation'])
guiData1FuelSystem = guiData1.drop_duplicates(subset=['fuelsystem'])
catagory_options = guiData1Category['Category']
catagory_var = catagory_options[0]
# list for different drive wheels options Drive wheels
driveWheels_options = guiData1DriveWheels['Drive wheels']

# list for different fuel types
fuel_type_options = guiData1FuelType['Fuel type']
fuel_type_var = fuel_type_options[0]

# list for possible door numbers

doorsNumber_options = guiData1DoorsNumber['doornumber']

# list of possible number of cylinders

cylinders_options = guiData1NumberOfCylinders['Cylinders']

# list of possible engine aspirations
engine_aspiration_options = guiData1Aspiration['aspiration']

# list of possible engine types
engine_type_options = guiData1EngineType['enginetype']
engineLocation_options = guiData1EngineLocation['enginelocation']
engineFuelSystem_options = guiData1FuelSystem['fuelsystem']
# the string vars that are used to save data from the form
aspiration_var = StringVar()
manufactuer_var = StringVar()
model_var = StringVar()
catagory_var = StringVar()
Leather_interior_var = StringVar()
fuel_type_var = StringVar()
cylinders_var = StringVar()
driveWheels_var = StringVar()
doorsNumber_var = StringVar()
engineType_var = StringVar()
engineLocation_var = StringVar()
fuelSystem_var = StringVar()

# data labels
# Title fo the gui
title = ttk.Label(frame1,
                  text="Car Price Predictor",
                  font=("Helvetica", 14),
                  background='#F3EFE0',
                  padding=15,
                  foreground="#3C2A21").grid(row=0, column=0, columnspan=2)
# labels on the left side of the gui
manufacturer = ttk.Label(frame1, text="car manufacturer").grid(row=1, column=0)
catagory = ttk.Label(frame1, text="catagory").grid(row=3, column=0)
fuel_type = ttk.Label(frame1, text="fuel type").grid(row=4, column=0)
cylinders = ttk.Label(frame1, text="number of cylinders").grid(row=5, column=0)
driveWheels = ttk.Label(frame1, text="Drive wheels").grid(row=6, column=0)
doorsNumber = ttk.Label(frame1, text="number of doors").grid(row=7, column=0)
engineAspiration = ttk.Label(frame1, text="enigne aspiration").grid(row=8,
                                                                    column=0)
engineType = ttk.Label(frame1, text="engine type").grid(row=9, column=0)
engineLocation = ttk.Label(frame1, text="engine Location").grid(row=10,
                                                                column=0)
fuelSystem = ttk.Label(frame1, text="Fuel System").grid(row=11, column=0)
# prediction result:
prdictionResult = ttk.Label(frame2,
                            text=" ",
                            font=("Helvetica", 12),
                            background='#F3EFE0',
                            padding=10,
                            foreground="#3C2A21").grid(row=0,
                                                       column=0,
                                                       columnspan=1)

# setting the display options for each dropDown
manufactuer_var.set(manufacturer_options[0])
catagory_var.set(catagory_options[0])
driveWheels_var.set(driveWheels_options[0])
fuel_type_var.set(fuel_type_options[0])
doorsNumber_var.set(doorsNumber_options[0])
cylinders_var.set(cylinders_options[0])
aspiration_var.set(engine_aspiration_options[0])
engineType_var.set(engine_type_options[0])
engineLocation_var.set(engineLocation_options[0])
fuelSystem_var.set(engineFuelSystem_options[0])

# Data entry and dataLabel.
# in order for the window to render at the correct size
# the values are changed inside the on_manufacturer select
model_entry = ttk.OptionMenu(frame1, model_var, "input a manufacturer",
                             "input a manufacturer").grid(row=2, column=1)
model = ttk.Label(frame1, text="Model ").grid(row=2, column=0)


# takes in an event, when the user selects a certain manufacturer
# displays the models assosiated with each manufacturer only
def on_manufacturer_select(event):
    selected_manufacturer = manufactuer_var.get()
    models = guiData[guiData['Manufacturer'] ==
                     selected_manufacturer]['Model '].values[0]
    model_var.set(models[0])
    model_entry = ttk.OptionMenu(frame1, model_var, *models).grid(row=2,
                                                                  column=1)
    model = ttk.Label(frame1, text="Model ").grid(row=2, column=0)


# data entry optionMenus
# each option menu takes a frame, a variable to display at the top
# and an array of things to display

# bug fix: function to resit the element displayed to the user
# after the selection has been made:

# manufacturer dropDown calls the on_manufacturer_select
# this influences the output of the model_dropDown
manufacturer_dropDown = ttk.OptionMenu(frame1,
                                       manufactuer_var,
                                       *manufacturer_options,
                                       command=on_manufacturer_select).grid(
                                           row=1, column=1)
catagory_dropDown = ttk.OptionMenu(frame1, catagory_var,
                                   *catagory_options).grid(row=3, column=1)
fuel_type_entry = ttk.OptionMenu(frame1, fuel_type_var,
                                 *fuel_type_options).grid(row=4, column=1)
cylinders_entry = ttk.OptionMenu(frame1, cylinders_var,
                                 *cylinders_options).grid(row=5, column=1)
driveWheels_entry = ttk.OptionMenu(frame1, driveWheels_var,
                                   *driveWheels_options).grid(row=6, column=1)
doorsNumber = ttk.OptionMenu(frame1, doorsNumber_var,
                             *doorsNumber_options).grid(row=7, column=1)
engineAspiration = ttk.OptionMenu(frame1, aspiration_var,
                                  *engine_aspiration_options).grid(row=8,
                                                                   column=1)
engineType = ttk.OptionMenu(frame1, engineType_var,
                            *engine_type_options).grid(row=9, column=1)
engineLocation = ttk.OptionMenu(frame1, engineLocation_var,
                                *engineLocation_options).grid(row=10, column=1)
fuelSystem = ttk.OptionMenu(frame1, fuelSystem_var,
                            *engineFuelSystem_options).grid(row=11, column=1)


# function that takes the variables from the gui
# user inputs and converts it into a dataframe
def submit():
    manufacturer_data = manufactuer_var.get()
    model_data = model_var.get()
    catagory_data = catagory_var.get()
    fuel_type_data = fuel_type_var.get()
    cylinders_data = cylinders_var.get()
    driveWheels_data = driveWheels_var.get()
    doorsNumber_data = doorsNumber_var.get()
    aspiration_data = aspiration_var.get()
    engine_type = engineType_var.get()
    engine_location = engineLocation_var.get()
    fuel_system = fuelSystem_var.get()

    # average of the values in the dataset
    # this is due to the fact that some of these details are
    # too technical for the user to know about their car
    car_id = 206
    symboling = 1
    wheel_base = 98.789
    car_length = 174.14
    car_width = 65.9
    car_height = 53.7
    car_weight = 2560
    engine_size = 127.1478
    bore_ratio = 3.33
    stroke = 3.3
    compression = 10.2
    horesepower = 104.4
    peakrpm = 5127.9
    citympg = 25.2
    highway_mpg = 30.7
    price = 13347.2

    # variables gathered from the user and from the averages
    # stored in a list
    list = [[car_id], [symboling], [fuel_type_data], [aspiration_data],
            [doorsNumber_data], [catagory_data], [driveWheels_data],
            [engine_location], [wheel_base], [car_length], [car_width],
            [car_height], [car_weight], [engine_type], [cylinders_data],
            [engine_size], [fuel_system], [bore_ratio], [stroke],
            [compression], [horesepower], [peakrpm], [citympg], [highway_mpg],
            [price]]
    # dataframe with both names of coulmns and the values
    # consists of one row and 25 coloumns
    df_data = pd.DataFrame(list).transpose()
    df_data.columns = [
        'car_ID', 'symboling', 'Fuel type', 'aspiration', 'doornumber',
        'Category', 'Drive wheels', 'enginelocation', 'wheelbase', 'carlength',
        'carwidth', 'carheight', 'curbweight', 'enginetype', 'Cylinders',
        'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio',
        'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'price'
    ]

    # passing the reutned prediciton to the get prediciton funciton
    predict(df_data)
    print(df_data)
    # returning the dataframe


# function to reset the dropDown menus
# by resetting the variables
def reset():
    manufactuer_var.set(manufacturer_options[0])
    model_var.set("input a manufacturer")
    catagory_var.set(catagory_options[0])
    driveWheels_var.set(driveWheels_options[0])
    fuel_type_var.set(fuel_type_options[0])
    doorsNumber_var.set(doorsNumber_options[0])
    cylinders_var.set(cylinders_options[0])
    aspiration_var.set(engine_aspiration_options[0])
    engineType_var.set(engine_type_options[0])
    engineLocation_var.set(engineLocation_options[0])
    fuelSystem_var.set(engineFuelSystem_options[0])


#Get the prediction value, and display it in a label
def get_prediction(prediciton):
    prediciton_result = ttk.Label(frame2,
                                  text=f"prediction result:{prediciton}",
                                  font=("Helvetica", 14),
                                  background='#F3EFE0',
                                  padding=15,
                                  foreground="#3C2A21").grid(row=0, column=0)


# function to process the data coming in from the user
# and run through the prediction
def predict(df):
    loaded_model = tf.keras.models.load_model('my_model_22.h5')
    xScaler = load("xScaler22.pkl")
    yScaler = load("yScaler22.pkl")

    data2 = pd.read_csv("C:\\Users\\hp\\Desktop\\University\\CMPE 460\\Project_deep\\cars.csv",encoding='iso-8859-1')

    data2 = data2[data2['price'] >= 500]

    if 'Manufacturer' in data2.columns:
        data2 = data2.drop('Manufacturer', axis=1)
    else:
        print("Manufacturer column not found")

    if 'Model ' in data2.columns:
        data2 = data2.drop('Model ', axis=1)
    else:
        print("Model  column not found")

    data2 = data2[:-1]
    data2 = data2.append(df)  # df is the input from the user which is coming from the gui file

    categorical_cols = [
        'symboling', 'Fuel type', 'aspiration', 'doornumber', 'Category',
        'Drive wheels', 'enginelocation', 'enginetype', 'Cylinders',
        'fuelsystem'
    ]
    # Create the main array with car_ID column
    main_array1 = np.array(data2['car_ID']).reshape(-1, 1)

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
        main_array1 = np.hstack((main_array1, temp))

    # Remove the car_ID column
    main_array1 = main_array1[:, 2:]

    pd.DataFrame(main_array1)

    main_array11 = main_array1.astype(float)

    # print(main_array11)
    # pd.main_array1
    # Get the input data from the user
    user_data = main_array11[-1:].reshape(1, -1)

    X_predict = user_data[:, :-1]
    # y_predict = user_data[:, -1]

    # Preprocess the input data using the same scaler that was used for the training data
    input_data_xscaled = xScaler.transform(X_predict)

    # Make predictions using the loaded model
    x_prediction = loaded_model.predict(input_data_xscaled)

    # Rescale the prediction
    prediction = yScaler.inverse_transform(x_prediction)
    prediction = float(prediction)
    print("Prediction price result: {}".format(float(prediction)))
    get_prediction(prediction)


sub_btn = ttk.Button(frame1, text='submit featuers',
                     command=submit).grid(row=12, column=1)
sub_btn = ttk.Button(frame1, text='Reset', command=reset).grid(row=12,
                                                               column=0)
window.mainloop()


# Code by: Mohammed G. Nasseir, Mohammad Hamed.
# ID: 119200029, 120200155

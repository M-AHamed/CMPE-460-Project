from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np

#from NeuralNetwork1 import predict_price_two_caller
# window attributes
window = Tk()
window.title("PriceMatch")
window.geometry('320x360')

window.configure(background="#5A5A5A")
guiData1 = pd.read_csv(
    "C:\\Users\\Mohammad\\Desktop\\Uni\\Uni work\\Year 4\\Term 7, fall 2022\\CMPE 460 Deep Learning\\project\\CMPE-460-Project\\dataset\\cars.csv",
    encoding='iso-8859-1')

guiData = pd.read_csv(
    "C:\\Users\\Mohammad\\Desktop\\Uni\\Uni work\\Year 4\\Term 7, fall 2022\\CMPE 460 Deep Learning\\project\\CMPE-460-Project\\dataset\\cars.csv",
    encoding='iso-8859-1')

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

# data labels
manufacturer = Label(window, text="car manufacturer").grid(row=0, column=0)

catagory = Label(window, text="catagory").grid(row=3, column=0)

fuel_type = Label(window, text="fuel type").grid(row=5, column=0)
cylinders = Label(window, text="number of cylinders").grid(row=7, column=0)
driveWheels = Label(window, text="Drive wheels").grid(row=9, column=0)
doorsNumber = Label(window, text="number of doors").grid(row=10, column=0)
engineAspiration = Label(window, text="enigne aspiration").grid(row=11,
                                                                column=0)
engineType = Label(window, text="engine type").grid(row=12, column=0)
# setting the display options
manufactuer_var.set(manufacturer_options[0])
catagory_var.set(catagory_options[0])
driveWheels_var.set(driveWheels_options[0])
fuel_type_var.set(fuel_type_options[0])
doorsNumber_var.set(doorsNumber_options[0])
cylinders_var.set(cylinders_options[0])
aspiration_var.set(engine_aspiration_options[0])
engineType_var.set(engine_type_options[0])
# function to set the data displayed in the models feild based on
# the uesr input in the manufacturer feild


def on_manufacturer_select(event):
    selected_manufacturer = manufactuer_var.get()
    models = guiData[guiData['Manufacturer'] ==
                     selected_manufacturer]['Model '].values[0]
    model_var.set(models[0])
    model_entry = OptionMenu(window, model_var, *models).grid(row=1, column=1)
    model = Label(window, text="Model ").grid(row=1, column=0)


# data entry forms
manufactuer_dropDown = OptionMenu(window,
                                  manufactuer_var,
                                  *manufacturer_options,
                                  command=on_manufacturer_select).grid(
                                      row=0, column=1)

catagory_dropDown = OptionMenu(window, catagory_var,
                               *catagory_options).grid(row=3, column=1)

fuel_type_entry = OptionMenu(window, fuel_type_var,
                             *fuel_type_options).grid(row=5, column=1)

cylinders_entry = OptionMenu(window, cylinders_var,
                             *cylinders_options).grid(row=7, column=1)

driveWheels_entry = OptionMenu(window, driveWheels_var,
                               *driveWheels_options).grid(row=9, column=1)

doorsNumber = OptionMenu(window, doorsNumber_var,
                         *doorsNumber_options).grid(row=10, column=1)

doorsNumber = OptionMenu(window, aspiration_var,
                         *engine_aspiration_options).grid(row=11, column=1)

doorsNumber = OptionMenu(window, engineType_var,
                         *engine_type_options).grid(row=12, column=1)

# function to define the contentes of the model feild

# submit function, takes data from the vars and saves them to variables


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

    car_id = 206
    symboling = 3
    engine_location = "front"
    wheel_base = 103.1
    car_length = 192.7
    car_width = 64.5
    car_height = 48.8
    car_weight = 2500
    engine_size = 110
    fuel_system = "mpfi"
    bore_ratio = 2.68
    stroke = 3.4
    compression = 8.6
    horesepower = 150
    peakrpm = 5000
    citympg = 24
    highway_mpg = 28
    price = 750.0

    list = [[car_id], [symboling], [fuel_type_data], [aspiration_data],
            [doorsNumber_data], [catagory_data], [driveWheels_data],
            [engine_location], [wheel_base], [car_length], [car_width],
            [car_height], [car_weight], [engine_type], [cylinders_data],
            [engine_size], [fuel_system], [bore_ratio], [stroke],
            [compression], [horesepower], [peakrpm], [citympg], [highway_mpg],
            [price]]

    df_data = pd.DataFrame(list).transpose()
    df_data.columns = [
        'car_ID', 'symboling', 'Fuel type', 'aspiration', 'doornumber',
        'Category', 'Drive wheels', 'enginelocation', 'wheelbase', 'carlength',
        'carwidth', 'carheight', 'curbweight', 'enginetype', 'Cylinders',
        'enginesize', 'fuelsystem', 'boreratio', 'stroke', 'compressionratio',
        'horsepower', 'peakrpm', 'citympg', 'highwaympg', 'price'
    ]
    # from prediction import preprocessing_data
    # preprocessing_data(data)
    print(df_data)
    return df_data


def reset():
    manufactuer_var.set("")
    model_var.set("")
    catagory_var.set("")
    fuel_type_var.set("")
    cylinders_var.set("")
    driveWheels_var.set("")
    doorsNumber_var.set("")
    engineType_var.set("")
    aspiration_var.set("")


sub_btn = Button(window, text='submit featuers', command=submit).grid(row=14,
                                                                      column=1)
sub_btn = Button(window, text='Reset', command=reset).grid(row=14, column=0)

window.mainloop()

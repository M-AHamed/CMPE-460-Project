import tkinter as tk
from tkinter import ttk
import pandas as pd
import numpy as np
#from NeuralNetwork1 import predict_price_two_caller
# window attributes
window = tk.Tk()
window.title("PriceMatch")
window.configure(background="#F3EFE0")

# styling attributse:
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
aspiration_var = tk.StringVar()
manufactuer_var = tk.StringVar()
model_var = tk.StringVar()
catagory_var = tk.StringVar()
Leather_interior_var = tk.StringVar()
fuel_type_var = tk.StringVar()
cylinders_var = tk.StringVar()
driveWheels_var = tk.StringVar()
doorsNumber_var = tk.StringVar()
engineType_var = tk.StringVar()
engineLocation_var = tk.StringVar()
fuelSystem_var = tk.StringVar()

# data labels
# Header of the gui
title = ttk.Label(frame1,
                  text="Car Price Predictor",
                  font=("Helvetica", 14),
                  background='#F3EFE0',
                  padding=15,
                  foreground="#3C2A21").grid(row=0, column=0, columnspan=2)
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

# setting the display options
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
# function to set the data displayed in the models feild based on
# the uesr input in the manufacturer feild
# model entry and label
model_entry = ttk.OptionMenu(frame1, model_var, "input a manufacturer",
                             "input a manufacturer").grid(row=2, column=1)
model = ttk.Label(frame1, text="Model ").grid(row=2, column=0)


def on_manufacturer_select(event):
    selected_manufacturer = manufactuer_var.get()
    models = guiData[guiData['Manufacturer'] ==
                     selected_manufacturer]['Model '].values[0]
    model_var.set(models[0])
    model_entry = ttk.OptionMenu(frame1, model_var, *models).grid(row=2,
                                                                  column=1)
    model = ttk.Label(frame1, text="Model ").grid(row=2, column=0)


# data entry forms

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

engineLocation = ttk.OptionMenu(
    frame1,
    engineLocation_var,
    *engineLocation_options,
).grid(row=10, column=1)
fuelSystem = ttk.OptionMenu(frame1, fuelSystem_var,
                            *engineFuelSystem_options).grid(row=11, column=1)

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
    get_prediction(5)
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
    engineLocation_var.set("")
    fuelSystem_var.set("")


def get_prediction(prediciton):
    prediciton_result = ttk.Label(frame2,
                                  text=f"prediction result:{prediciton}",
                                  font=("Helvetica", 14),
                                  background='#F3EFE0',
                                  padding=15,
                                  foreground="#3C2A21").grid(row=0, column=0)


sub_btn = ttk.Button(frame1, text='submit featuers',
                     command=submit).grid(row=12, column=1)
sub_btn = ttk.Button(frame1, text='Reset', command=reset).grid(row=12,
                                                               column=0)

window.mainloop()
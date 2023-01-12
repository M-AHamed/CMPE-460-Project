from tkinter import *
from tkinter import ttk
import pandas as pd

# window attributes
window = Tk()
window.title("PriceMatch")
window.geometry('320x360')

window.configure(background="#5A5A5A")


data = pd.read_csv("D:\\Downloads\\car_price_prediction.csv")
data = data.drop_duplicates()
# data = data[data.Manufacturer.str.match('^[A-Za-z]+$')]
data = data.groupby('Manufacturer')['Model'].apply(
    lambda x: x.unique().tolist()).reset_index()

print(data)


# the manufacturer list of items:
manufacturer_options = ["ACURA", "ALFA ROMEO", "ASTON MARTIN", "AUDI", "BENTLEY", "BMW", "BUICK", "CADILLAC", "CHEVROLET", "CHRYSLER", "CITROEN",
                        "DAEWOO", "DAIHATSU", "DODGE", "FERRARI", "FIAT", "FORD", "GAZ", "GMC", "GREATWALL", "HAVAL", "HONDA", "HUMMER", "HYUNDAI", "INFINITI", "ISUZU", "JAGUAR", "JEEP", "KIA", "LAMBORGHINI", "LANCIA", "LAND ROVER",
                        "LEXUS", "LINCOLN", "MASERATI", "MAZDA", "MERCEDES-BENZ", "MERCURY", "MINI", "MITSUBIS", "MOSKVICH", "NISSAN",
                        "OPEL", "PEUGEOT", "PONTIAC", "PORSCHE", "RENAULT", "ROVER", "SAAB", "SATURN", "SCION", "SEAT", "SKODA", "SSANGYONG",
                        "SUBARU", "SUZUKI", "TESLA", "TOYOTA", "UAZ", "VAZ", "VOLKSWAGEN", "VOLVO", "ZAZ"]

# list for different catogaries
catagory_options = ["Jeep", "Hatchback", "Sedan", "Microbus", "Goods wagon", "Universal", "Coupe",
                    "Minivan", "Cabriolet", "Limousine", "Pickup"]

# list for different drive wheels options
driveWheels_options = ["4x4", "Front", "Rear"]

# list for different leather interior options
leather_interior_options = ["yes", "no"]

# list for different gearBox options
gear_box_options = ['Automatic', 'Tiptronic', 'Variator', 'Manual']

# list for different fuel types
fuel_type_options = ["Hybrid", "Petrol", "Diesel",
                     "CNG", "Plug-in Hybrid", "LPG", "Hydrogen"]


# the string vars that are used to save data from the form
manufactuer_var = StringVar()
model_var = StringVar()
production_year_var = StringVar()
catagory_var = StringVar()
Leather_interior_var = StringVar()
fuel_type_var = StringVar()
milage_var = StringVar()
cylinders_var = StringVar()
gear_box_var = StringVar()
driveWheels_var = StringVar()
doorsNumber_var = StringVar()
airbags_var = StringVar()

# data labels
manufacturer = Label(window, text="car manufacturer").grid(row=0, column=0)
prduction_year = Label(window, text="production year").grid(row=2, column=0)
catagory = Label(window, text="catagory").grid(row=3, column=0)
Leather_interior = Label(window, text="Leather interior").grid(row=4, column=0)
fuel_type = Label(window, text="fuel type").grid(row=5, column=0)
milage = Label(window, text="car milage").grid(row=6, column=0)
cylinders = Label(window, text="number of cylinders").grid(row=7, column=0)
gear_box = Label(window, text="gear box type").grid(row=8, column=0)
driveWheels = Label(window, text="Drive wheels").grid(row=9, column=0)
doorsNumber = Label(window, text="number of doors").grid(row=10, column=0)
airbags = Label(window, text="airbags").grid(row=11, column=0)

# setting the display options
manufactuer_var.set(manufacturer_options[0])
catagory_var.set(catagory_options[0])
driveWheels_var.set(driveWheels_options[0])
Leather_interior_var.set(leather_interior_options[1])
gear_box_var.set(gear_box_options[0])
fuel_type_var.set(fuel_type_options[0])

# function to set the data displayed in the models feild based on
# the uesr input in the manufacturer feild


def on_manufacturer_select(event):
    selected_manufacturer = manufactuer_var.get()
    models = data[data['Manufacturer'] ==
                  selected_manufacturer]['Model'].values[0]
    model_var.set(models[0])
    model_entry = OptionMenu(window, model_var,  *models).grid(row=1, column=1)
    model = Label(window, text="Model").grid(row=1, column=0)


# data entry forms
manufactuer_dropDown = OptionMenu(
    window, manufactuer_var, *manufacturer_options, command=on_manufacturer_select).grid(row=0, column=1)
production_year_entry = Entry(
    window, textvariable=production_year_var).grid(row=2, column=1)
catagory_dropDown = OptionMenu(
    window, catagory_var, *catagory_options).grid(row=3, column=1)
Leather_interior_entry = OptionMenu(
    window,  Leather_interior_var, *leather_interior_options).grid(row=4, column=1)
fuel_type_entry = OptionMenu(
    window, fuel_type_var, *fuel_type_options).grid(row=5, column=1)
milage_entry = Entry(window, textvariable=milage_var).grid(row=6, column=1)
cylinders_entry = Entry(
    window, textvariable=cylinders_var).grid(row=7, column=1)
gear_box_entry = OptionMenu(
    window, gear_box_var, *gear_box_options).grid(row=8, column=1)
driveWheels_entry = OptionMenu(
    window, driveWheels_var, *driveWheels_options).grid(row=9, column=1)
doorsNumber = Entry(window, textvariable=doorsNumber_var).grid(
    row=10, column=1)
airbags = Entry(window, textvariable=airbags_var).grid(row=11, column=1)

# function to define the contentes of the model feild


# submit function, takes data from the vars and saves them to variables

def submit():
    manufacturer_data = manufactuer_var.get()
    model_data = model_var.get()
    production_year_data = production_year_var.get()
    catagory_data = catagory_var.get()
    Leather_interior_data = Leather_interior_var.get()
    fuel_type_data = fuel_type_var.get()
    milage_data = milage_var.get()
    cylinders_data = cylinders_var.get()
    gear_box_data = gear_box_var.get()
    driveWheels_data = driveWheels_var.get()
    doorsNumber_data = doorsNumber_var.get()
    airbags_data = airbags_var.get()


# saving the data into a list from teh
    list = [manufacturer_data, model_data, production_year_data, catagory_data,
            Leather_interior_data, fuel_type_data, milage_data, cylinders_data, gear_box_data, driveWheels_data, doorsNumber_data, airbags_data]

    print(' '.join(map(str, list)))


def reset():
    manufactuer_var.set("")
    model_var.set("")
    production_year_var.set("")
    catagory_var.set("")
    Leather_interior_var.set("")
    fuel_type_var.set("")
    milage_var.set("")
    cylinders_var.set("")
    gear_box_var.set("")
    driveWheels_var.set("")
    doorsNumber_var.set("")
    airbags_var.set("")


sub_btn = Button(window, text='submit featuers',
                 command=submit).grid(row=12, column=1)
sub_btn = Button(window, text='Reset', command=reset).grid(row=12, column=0)

window.mainloop()

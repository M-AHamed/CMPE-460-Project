from tkinter import *
from tkinter import ttk
import tkinter as tk

# window attributes
window = Tk()
window.title("PriceMatch")
window.geometry('1080x1920')
window.configure(background = "gray")

# the manufacturer dataframe:
manufacturer_options= ["LEXUS", "CHEVROLET","GREATWALL","HONDA","FORD","HYUNDAI","TOYOTA",
                                                     "MERCEDES-BENZ", "OPEL","PORSCHE","BMW","JEEP","VOLKSWAGEN","AUDI",
                                                     "RENAULT", "NISSAN","SUBARU","DAEWOO","KIA","MITSUBIS","SSANGYONG",
                                                     "MAZDA", "GMC","FIAT","INFINITI","ALFA ROMEO","SUZUKI","ACURA",
                                                     "LINCOLN", "VAZ","GAZ","CITROEN","LAND ROVER","MINI","DODGE",
                                                     "CHRYSLER", "JAGUAR","ISUZU","SKODA","DAIHATSU","BUICK","TESLA",
                                                     "CADILLAC", "PEUGEOT","BENTLEY","VOLVO","HAVAL","HUMMER","SCION",
                                                     "UAZ", "MERCURY","ZAZ","ROVER","SEAT","LANCIA","MOSKVICH",
                                                     "MASERATI", "FERRARI","SAAB","LAMBORGHINI","PONTIAC","SATURN","ASTON MARTIN"]

# list for different catogaries
catagory_options = ["Jeep", "Hatchback","Sedan","Microbus","Goods wagon","Universal","Coupe",
                                             "Minivan", "Cabriolet","Limousine","Pickup"]

# list for different drive wheels options
driveWheels_options = ["4x4", "Front","Rear"]

# list for different leather interior options
leather_interior_options = ["yes", "no"]

# list for different gearBox options
gear_box_options = ['Automatic', 'Tiptronic','Variator', 'Manual']

# list for different fuel types
fuel_type_options = ["Hybrid", "Petrol","Diesel","CNG","Plug-in Hybrid","LPG","Hydrogen"]

# the string vars that are used to save data from the form
manufactuer_var= tk.StringVar()
model_var= tk.StringVar()
production_year_var = tk.StringVar()
catagory_var = tk.StringVar()
Leather_interior_var  = tk.StringVar()
fuel_type_var = tk.StringVar()
milage_var = tk.StringVar()
cylinders_var = tk.StringVar()
gear_box_var = tk.StringVar()
driveWheels_var = tk.StringVar()
doorsNumber_var = tk.StringVar()
airbags_var = tk.StringVar()



# data labels 
manufacturer = Label(window ,text = "car manufacturer").grid(row = 0,column = 0)
model = Label(window ,text = "Model").grid(row = 1,column = 0)
prduction_year = Label(window, text = "production year").grid(row = 2,column = 0)
catagory = Label(window ,text = "catagory").grid(row = 3,column = 0)
Leather_interior = Label(window ,text = "Leather interior").grid(row = 4,column = 0)
fuel_type= Label(window ,text = "fuel type").grid(row = 5,column = 0)
milage= Label(window ,text = "car milage").grid(row = 6,column = 0)
cylinders= Label(window ,text = "number of cylinders").grid(row = 7,column = 0)
gear_box= Label(window ,text = "gear box type").grid(row = 8,column = 0)
driveWheels= Label(window ,text = "Drive wheels").grid(row = 9,column = 0)
doorsNumber= Label(window ,text = "number of doors").grid(row = 10,column = 0)
airbags= Label(window ,text = "airbags").grid(row = 11,column = 0)


# setting the display option
manufactuer_var.set(manufacturer_options[0])
catagory_var.set(catagory_options[0])
driveWheels_var.set(driveWheels_options[0])
Leather_interior_var.set(leather_interior_options[1])
gear_box_var.set(gear_box_options[0])
fuel_type_var.set(fuel_type_options[0])
# data entry forms
manufactuer_dropDown = OptionMenu(window , manufactuer_var, *manufacturer_options).grid(row = 0,column = 1)
model_entry = Entry(window, textvariable= model_var).grid(row = 1,column = 1)
production_year_entry = Entry(window, textvariable= production_year_var).grid(row = 2,column = 1)
catagory_dropDown = OptionMenu(window , catagory_var, *catagory_options).grid(row = 3,column = 1)
Leather_interior_entry = OptionMenu(window,  Leather_interior_var, *leather_interior_options).grid(row = 4,column = 1)
fuel_type_entry = OptionMenu(window, fuel_type_var, *fuel_type_options).grid(row = 5,column = 1)
milage_entry= Entry(window, textvariable= milage_var).grid(row = 6,column = 1)
cylinders_entry= Entry(window, textvariable= cylinders_var).grid(row = 7,column = 1)
gear_box_entry= OptionMenu(window, gear_box_var, *gear_box_options).grid(row = 8,column = 1)
driveWheels_entry= OptionMenu(window, driveWheels_var, *driveWheels_options).grid(row = 9,column = 1)
doorsNumber= Entry(window, textvariable= doorsNumber_var).grid(row = 10,column = 1)
airbags= Entry(window, textvariable= airbags_var).grid(row = 11,column = 1)

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
    list= [manufacturer_data, model_data, production_year_data, catagory_data,
     Leather_interior_data, fuel_type_data, milage_data, cylinders_data, gear_box_data, driveWheels_data, doorsNumber_data, airbags_data]

    print(' '.join(map(str, list)))
     
sub_btn=ttk.Button(window,text = 'submit featuers', command = submit).grid(row=12,column=0)


window.mainloop()

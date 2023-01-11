from tkinter import *
from tkinter import ttk
import tkinter as tk

window = Tk()
window.title("PriceMatch")
window.geometry('1080x1920')
window.configure(background = "gray")

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



manufactuer_entry = Entry(window, textvariable= manufactuer_var).grid(row = 0,column = 1)
model_entry = Entry(window, textvariable= model_var).grid(row = 1,column = 1)
production_year_entry = Entry(window, textvariable= production_year_var).grid(row = 2,column = 1)
catagory_entry = Entry(window , textvariable= catagory_var).grid(row = 3,column = 1)
Leather_interior_entry = Entry(window,  textvariable= Leather_interior_var).grid(row = 4,column = 1)
fuel_type_entry = Entry(window, textvariable= fuel_type_var).grid(row = 5,column = 1)
milage_entry= Entry(window, textvariable= milage_var).grid(row = 6,column = 1)
cylinders_entry= Entry(window, textvariable= cylinders_var).grid(row = 7,column = 1)
gear_box_entry= Entry(window, textvariable= gear_box_var).grid(row = 8,column = 1)
driveWheels_entry= Entry(window, textvariable= driveWheels_var).grid(row = 9,column = 1)
doorsNumber= Entry(window, textvariable= doorsNumber_var).grid(row = 10,column = 1)
airbags= Entry(window, textvariable= airbags_var).grid(row = 11,column = 1)


#btn = ttk.Button(window ,text="Submit").grid(row=12,column=0)


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



    list= [manufacturer_data, model, model_data, production_year_data, catagory_data, Leather_interior_data, fuel_type_data, milage_data, cylinders_data, gear_box_data, driveWheels_data, doorsNumber_data, airbags_data]

    print(' '.join(map(str, list)))
     
sub_btn=ttk.Button(window,text = 'hello', command = submit).grid(row=12,column=0)


window.mainloop()

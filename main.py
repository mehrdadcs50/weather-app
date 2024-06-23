import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
# from timezonefinder import TimezoneFinder
from datetime import datetime
# import pytz
import requests


def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        # obj = TimezoneFinder()
        # result = obj.timezone_at(lng=lng, lat=lat)
        result = f'continent/{city}'
        city_label.config(text=result.split("/")[1])
        
        # home = pytz.timezone(result)
        # local_time = datetime.now(home)
        # current_time = local_time.strftime("%I:%M %P")
        # clock.config(text=current_time)
        # time_label.config(text="LOCAL TIME")
        
        api_key = "abd74cdf6551423d50bf82c0d6af380e"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"
        json_data = requests.get(api).json()
        condition = json_data['weather'][0]['main']
        desciption = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']
        
        temp_label.config(text=f"{temp}°C")
        condition_label.config(text=f"{condition} | FEELS LIKE {temp}°C")
        wind_label.config(text={wind})
        Humidity_label.config(text={humidity})
        description_label.config(text={desciption})
        pressure_label.config(text={pressure})
        
    except Exception as error:
        messagebox.showerror("Weather App", "Invalid Entry ")

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False, False)

# search image
search_image = tk.PhotoImage(file="search.png")
search_image_lable = tk.Label(root, image = search_image)
search_image_lable.pack(pady=20, side=tk.TOP)
textfield = tk.Entry(root, justify="center", width=17,
                     font=("poppins", 25, "bold"),
                     bg="#404040", fg="white", border=0)

textfield.place(x=280, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_buttom = tk.Button(root, image=search_icon, border=0, 
                               cursor="hand2", bg="#404040", command=get_weather)

def func(event):
    get_weather()                               
root.bind('<Return>', func)

search_icon_buttom.place(x=590, y=34)



#logo

logo_image = tk.PhotoImage(file="logo.png")
logo_lable = tk.Label(root, image=logo_image)
logo_lable.pack(side=tk.TOP)

#Bottom box 

frame_image = tk.PhotoImage(file="box.png")
frame_lable = tk.Label(root, image=frame_image)
frame_lable.pack(pady=10,side=tk.BOTTOM)

#city name

city_label = tk.Label(root, font=("arial", 40, "bold"), fg="#e355cd" )
city_label.place(x=120, y=160)

#time
time_label = tk.Label(root, font=("arial", 20, "bold"), fg="#4b4bcc" )
time_label.place(x=120, y=230)


clock = tk.Label(root, font=("Helvetica", 20, "bold"), fg="#e355cd" )
clock.place(x=120, y=278)


label1 = tk.Label(root, text="WIND", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = tk.Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label2.place(x=280, y=400)

label3 = tk.Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label3.place(x=450, y=400)

label4 = tk.Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"),
                  fg="white", bg="#1ab5ef")
label4.place(x=670, y=400)



temp_label = tk.Label(root, font=("arial", 70, "bold"), fg="#e355cd")
temp_label.place(x=590, y=170)

condition_label = tk.Label(root, font=("arial", 15, "bold"), fg="#4b4bcc")
condition_label.place(x=590, y=270)



wind_label = tk.Label(root, text="....", font=("arial", 20, "bold"),bg="#1ab5ef", fg="#404040")
wind_label.place(x=120, y=430)

Humidity_label = tk.Label(root, text="....", font=("arial", 20, "bold"),bg="#1ab5ef", fg="#404040")
Humidity_label.place(x=280, y=430)

description_label = tk.Label(root, text="....", font=("arial", 20, "bold"),bg="#1ab5ef", fg="#404040")
description_label.place(x=450, y=430)

pressure_label = tk.Label(root, text="....", font=("arial", 20, "bold"),bg="#1ab5ef", fg="#404040")
pressure_label.place(x=670, y=430)


root.mainloop()





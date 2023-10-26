from tkinter import*

import random

root = Tk()

root.title("Country Capitals")
root.geometry("500x500")

country_name = Entry(root)
country_name.place(relx=0.5, rely=0.2, anchor=CENTER)

city_name = Entry(root)
city_name.place(relx=0.5, rely=0.3, anchor=CENTER)

country_list = []
city_list = []

country_name_label = Label(root)
city_name_label = Label(root)
 
random_country_label = Label(root)
random_city_label = Label(root)

def addcountry():
    country_name1 = country_name.get()
    city_name1 = city_name.get()
    country_list.append(country_name1)
    city_list.append(city_name1)
    country_name_label["text"]=str(country_list) 
    city_name_label["text"]=str(city_list)
    
def random_number():
    length = len(country_list)
    random_no = random.randint(0, length-1)
    generated_random_country = country_list[random_no]
    generated_random_city = city_list[random_no]
    random_country_label["text"]="Your random country is "+str(generated_random_country)
    random_city_label["text"]="Your random city is "+str(generated_random_city)

btn = Button(root, text="Display Country and City Name", command=addcountry)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)
country_name_label.place(relx=0.5, rely=0.5, anchor=CENTER)
city_name_label.place(relx=0.5, rely=0.6, anchor=CENTER)

btn1 = Button(root, text="Display Country Name and City Name Randomly", command=random_number)
btn1.place(relx=0.5, rely=0.7, anchor=CENTER)
random_country_label.place(relx=0.5, rely=0.8, anchor=CENTER)
random_city_label.place(relx=0.5, rely=0.9, anchor=CENTER)

root.mainloop()
import customtkinter
import tkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()

app.title('Lina first')
app.geometry('500x500')




frame = customtkinter.CTkFrame(master=app,
                               width=200,
                               height=200,
                               corner_radius=10,
                               bg_color='white')
frame.pack(padx=20, pady=20)

def button_function1():
    print('button 1 pressed!')

def button_function2():
    print('button 2 pressed!')

button1 = customtkinter.CTkButton(master=frame, text='CtkButton_1', command=button_function1)
button1.place(relx=0.5, rely=0.4, anchor = tkinter.CENTER)

button2 = customtkinter.CTkButton(master=frame, text='CtkButton_2', command=button_function2)
button2.place(relx=0.5, rely=0.6, anchor = tkinter.CENTER)







def button_function():
    print('My button pressed!')

button = customtkinter.CTkButton(master=app, text='My button', command=button_function)
button.place(relx=0.5, rely=0.5, anchor = tkinter.CENTER)






tabView = customtkinter.CTkTabview(app)
tabView.pack(padx=20, pady=20)

tabView.add('tab-1')
tabView.add('tab-2')
tabView.add('tab-3')

tabView.set('tab-1')

def button_function3():
    print('button 3 pressed!')

def button_function4():
    print('button 4 pressed!')

def button_function5():
    print('button 5 pressed!')

button_3 = customtkinter.CTkButton(tabView.tab('tab-1'), text='Button 3', command=button_function3)
button_3.pack(padx=20, pady=20)

button_4 = customtkinter.CTkButton(tabView.tab('tab-2'), text='Button 4', command=button_function4)
button_4.pack(padx=20, pady=20)

button_5 = customtkinter.CTkButton(tabView.tab('tab-3'), text='Button 5', command=button_function5)
button_5.pack(padx=20, pady=20)




app.mainloop()

import customtkinter
import tkinter

customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')

app = customtkinter.CTk()

app.title('Lina first')
app.geometry('500x500')


textbox =  customtkinter.CTkTextbox(app)
textbox.grid(row = 0, column = 0)
text = 'welcome!'

textbox.insert('0.0', text)
textbox.configure(state='normal')

def my_button():
    print(textbox.get('0.0', 'end'))

button = customtkinter.CTkButton(master=app, text='My Button', command=my_button)
button.place(relx=0.7, rely=0.3, anchor = tkinter.CENTER)



app.mainloop()
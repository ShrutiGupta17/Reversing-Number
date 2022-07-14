import tkinter as tk

def reverse():
  txt = box1.get()
  box2.delete(0,tk.END)
  box2.insert(0,txt[::-1])
  print(txt)
  
def reset():
    box1.delete(0,tk.END)
    box2.delete(0,tk.END)
app =  tk.Tk()
app.title("Reverse Number")
app.geometry("800x300")
app.iconbitmap("WhatsApp-Image-2022-03-30-at-22.20.02.jpg.ico")
app.resizable(False, False)

label1 = tk.Label(app, text = "Number", font = ("segoe",25))
label1.place(x = 20 , y = 20 )

label2 = tk.Label(app, text = "Reversed", font = ("segoe",25))
label2.place(x = 20 , y = 100)

box1 = tk.Entry(app,font = ("segoe",25),bg = "#D3D3D3")
box1.place(x=180 ,y=20)

box2 = tk.Entry(app,font = ("segoe",25),bg = "#D3D3D3")
box2.place(x=180 ,y=100)

button1 = tk.Button(app ,text = "Reverse" ,font=("Arial",12),bg ="red",command = reverse)
button1.place(x=180 , y= 150 , width = 70)

button2 = tk.Button(app ,text = "Reset" ,font=("Arial",12),bg ="red",command = reset)
button2.place(x=280 , y= 150 , width = 70)


img = tk.PhotoImage(file= "reversed.png")
label = tk.Label(image = img )
label.place(x= 575 , y= 20)
app.mainloop()

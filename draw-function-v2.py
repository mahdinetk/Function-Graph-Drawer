import tkinter as tk
from tkinter import messagebox
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from messages import *


#A list to store y and x values
x_num = []
y_num = []
chek_items = 0


# Checking that the entered parameter is correct
def chek_error(a, b, c):
     try:
          a = float(a)
          b = float(b)
          c = float(c)
     except:
          messagebox.showerror("error", "لطفا ورودی  عددی وارد کنید")
     else:
          return True


# a method to To draw a diagram
def draw_graph(x, y):
    # creating a figure
    fig = plt.figure(figsize=(5, 4))

    # draw a diagram
    plt.plot(x, y, "r")
    plt.axhline(y=0, color="blue") #horizontal axis
    plt.axvline(x=0, color="blue") #vertical axis
    plt.grid()

     #showing diagram in canvas
    canvas = FigureCanvasTkAgg(figure=fig, master=frame_2)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=5)


# To save the parameters that the user enters and calculating thoes 
def calculate_linear_function():
     global entry_la, entry_lb, chek_items, x_num, y_num
     
     # Checking that the entered parameter is correct
     a = entry_la.get()
     b = entry_lb.get()
          
     if chek_error(a=a, b=b, c=0):
          
          #Checking that it draws the graph only once at a time
          chek_items += 1
          if chek_items == 1:
               
               # Adjust the range of x based on the values ​​of a and b
               #the value of 'x' should be according to the value of 'a, b'
               x_range = max(abs(float(a)), abs(float(b))) * 2
               x_num = np.linspace(-x_range, x_range, 400)
               #Testing several different numbers as the x value in x_num to calculate the y value
               for x in x_num:
                    y = float(a) * x + float(b)
                    y_num.append(y)

               tk.Label(frame_2, text=f"f(x)={a}X + {b}").pack()
               draw_graph(x_num, y_num)


# To save the parameters that the user enters and calculating thoes 
def calculate_constant_function():
     global entry_ca, chek_items, y_num, x_num

     a = entry_ca.get()
          
     if chek_error(a=a, b=0, c=0):

          #Checking that it draws the graph only once at a time
          chek_items += 1
          if chek_items == 1:

               # Adjust the range of x based on the values ​​of a 
               #the value of 'x' should be according to the value of a
               x_range = float(a)
               x_num = np.linspace(-x_range, x_range, 400)
               
               #using x values in x_num to get the x-points
               for x in x_num:
                    y = float(a)
                    y_num.append(y)

               tk.Label(frame_2, text=f"f(x)={a}").pack()
               draw_graph(x_num, y_num)


# To save the parameters that the user enters and calculating thoes 
def calculate_parabola_function():
     global entry_pa, entry_pb, entry_pc, chek_items, x_num, y_num
     a = entry_pa.get()
     b = entry_pb.get()
     c = entry_pc.get()
          
     if chek_error(a=a, b=b, c=c):
          # in parabola function "a" must not be 0
          try:
               float(b) / float(a)
          except:
               messagebox.showerror("error", "نباید صفر باشد 'a' در تابع سهمی مقدار")   
          else:

               #Checking that it draws the graph only once at a time
               chek_items += 1
               if chek_items == 1:

                    # the value of 'x' should be according to the value of 'a, b, c'
                    # Adjust the range of x based on the values ​​of a and b and c
                    vertex_x = -float(b) / (2 * float(a))
                    # -1 , +1 used so that if b or c were zero, the range of x_value whould not be lost
                    x_num = np.linspace((vertex_x - float(c))-1, (vertex_x + float(c))+1, 400)
                    for x in x_num:
                         y = (float(a) * (x ** 2)) + (float(b) * x) + float(c)
                         y_num.append(float(y))

                    tk.Label(frame_2, text=f"f(x)={a}X^2 + {b}X + {c}").pack()
                    draw_graph(x=x_num, y=y_num)


# To save the parameters that the user enters and calculating thoes 
def calculate_abs_function():
     global entry_aa, entry_ab, chek_items, x_num, y_num
     a = entry_aa.get()
     b = entry_ab.get()
          
     if chek_error(a=a, b=b, c=0):
          #Checking that it draws the graph only once at a time
          chek_items += 1
          if chek_items == 1:
               # Adjust the range of x based on the values ​​of a and b
               #the value of 'x' should be according to the value of 'a, b'
               # -1 , +1 used so that if b or c were zero, the range of x_value whould not be lost
               x_range = max(abs(float(a)), abs(float(b))) * 2
               x_num = np.linspace((-x_range)-1, (x_range)+1, 400)
               for x in x_num:
                    y = abs(float(a)+x) + float(b)
                    y_num.append(y)

               tk.Label(frame_2, text=f"f(x)=|{a}+X| + {b}").pack()
               draw_graph(x_num, y_num)


# showing the part related to the linear funciton
def linear_function():
     global entry_la, entry_lb, chek_items, y_num
     
     # clear and refresh the frame_2
     for widget in frame_2.winfo_children():
          widget.destroy()

     chek_items = 0
     y_num = []


     # to show the linear_message
     tk.Label(frame_2, text=linear_message, font=("", 13), bg="azure").pack(pady=5)

     # showing message for getting a
     tk.Label(frame_2, text="را وارد کنید a مقدار", bg="#77B1AD").pack()

     # getting a parameter from the user
     entry_la = tk.Entry(frame_2, width=20)
     entry_la.pack()
  
     # showing message for getting b
     tk.Label(frame_2, text="را وارد کنید b مقدار", bg="#77B1AD").pack()

     # getting b parameter from the user
     entry_lb = tk.Entry(frame_2, width=20)
     entry_lb.pack()

     # sorting parametrs with get_entry function
     store_btm = tk.Button(frame_2, text="رسم نمودار", width=10, command=calculate_linear_function, bg="#FFDE08")
     store_btm.pack(pady=5)


# showing the part related to the constant funciton
def constant_function():
     global entry_ca, chek_items, y_num

     # clear and refresh the frame_2
     for widget in frame_2.winfo_children():
          widget.destroy()

     chek_items = 0
     y_num = []

     # to show the constant_message
     tk.Label(frame_2, text=constant_message, font=("", 13), bg="azure").pack(pady=5)

     # showing message for getting c
     tk.Label(frame_2, text="را وارد کنید c مقدار", bg="#77B1AD").pack()
  
     # getting a parametr from the user
     entry_ca = tk.Entry(frame_2, width=20)
     entry_ca.pack()

     # sorting parametrs with get_entry function
     store_btm = tk.Button(frame_2, text="رسم نمودار", width=10, command=calculate_constant_function, bg="#FFDE08")
     store_btm.pack(pady=5)


# showing the part related to the identity funciton
def identity_function():
     global chek_items, x_num, y_num

     y_num = []
     x_num = np.linspace(-200, 200, 400)

     # clear and refresh the frame_2
     for widget in frame_2.winfo_children():
          widget.destroy()

     # to show the identity_message
     tk.Label(frame_2, text=identity_message, font=("", 13), bg="azure").pack(pady=5)
     for x in x_num:
          y = x
          y_num.append(y)
     tk.Label(frame_2, text=f"f(x)=X").pack()
     draw_graph(x_num, y_num)


# showing the part related to the parabola funciton          
def parabola_function():
     global entry_pa, entry_pb, entry_pc, chek_items, y_num

     # clear and refresh the frame_2
     for widget in frame_2.winfo_children():
          widget.destroy()

     chek_items = 0
     y_num = []

     # to show the parabola_message
     tk.Label(frame_2, text=parabola_message, font=("", 13), bg="azure").pack(pady=5)

     # showing message for getting a
     tk.Label(frame_2, text="را وارد کنید a مقدار", bg="#77B1AD").pack()

     # getting a parameter from the user
     entry_pa = tk.Entry(frame_2, width=20)
     entry_pa.pack()

     # showing message for getting b
     tk.Label(frame_2, text="را وارد کنید b مقدار", bg="#77B1AD").pack()

     # getting b parameter from the user
     entry_pb = tk.Entry(frame_2, width=20)
     entry_pb.pack()

     # showing message for getting c
     tk.Label(frame_2, text="را وارد کنید c مقدار", bg="#77B1AD").pack()

     # getting c parameter from the user
     entry_pc = tk.Entry(frame_2, width=20)
     entry_pc.pack()

     # sorting parametrs with get_entry function
     store_btm = tk.Button(frame_2, text="رسم نمودار", width=10, command=calculate_parabola_function, bg="#FFDE08")
     store_btm.pack(pady=5)


# showing the part related to the absolute funciton          
def absolute_value_function():
     global entry_aa, entry_ab, chek_items, y_num

     # clear and refresh the frame_2
     for widget in frame_2.winfo_children():
          widget.destroy()

     chek_items = 0
     y_num = []

     # to show the absolute_value_message
     tk.Label(frame_2, text=absolute_value_message, font=("", 13), bg="azure").pack(pady=5)

     # showing message for getting a
     tk.Label(frame_2, text="را وارد کنید a مقدار", bg="#77B1AD").pack()

     # getting a parameter from the user
     entry_aa = tk.Entry(frame_2, width=20)
     entry_aa.pack()

     # showing message for getting b
     tk.Label(frame_2, text="را وارد کنید b مقدار", bg="#77B1AD").pack()

     # getting b parameter from the user
     entry_ab = tk.Entry(frame_2, width=20)
     entry_ab.pack()

     # sorting parametrs with get_entry function
     store_btm = tk.Button(frame_2, text="رسم نمودار", width=10, command=calculate_abs_function, bg="#FFDE08")
     store_btm.pack(pady=5)


#------creating and setting the main window 


window = tk.Tk()
window.title("رسم توابع ریاضی")
window.geometry("1350x680")
window.resizable(height="false", width="false")


# this frame used for managing and designing buttons and welcome_lbl
frame = tk.Frame(window, borderwidth=10, relief="ridge", background="#689EB8")
frame.pack(side="right", fill="y")

# this frame used for drawing diagrams
frame_2 = tk.Frame(window, background="#689EB8", borderwidth=10, relief="ridge")
frame_2.pack(side="left",fill="both", expand=True)

#showing welcome_message
welcome_lbl = tk.Label(frame, text=welcome_message, font=("", 13), background="#E9F7F8")
welcome_lbl.pack(padx=10, pady=20)

# creating buttons (for each function we make one button)
linear_btm = tk.Button(frame , text="تابع خطی", width=25, height=2, command=linear_function, background="#FFDE08")
constant_btm = tk.Button(frame, text="تابع ثابت", width=25, height=2, command=constant_function, background="#FFDE08")
identity_btm = tk.Button(frame, text="تابع همانی", width=25, height=2, command=identity_function, background="#FFDE08")
parabola_btm = tk.Button(frame, text="تابع سهمی", width=25, height=2, command=parabola_function, background="#FFDE08")
absolute_value_btm = tk.Button(frame, text="تابع قدر مطلق", width=25, height=2, command=absolute_value_function, background="#FFDE08")

#showing buttons
constant_btm.place(x=265, y=535)
linear_btm.place(x=50, y=480)
identity_btm.place(x=480, y=480)
parabola_btm.place(x=50, y=580)
absolute_value_btm.place(x=480, y=580)


window.mainloop()

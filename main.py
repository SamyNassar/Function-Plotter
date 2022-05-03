from tkinter import *
from tkinter import messagebox
import plotter
import validate

## GUI Windows. 

window = Tk()
window.title("Function Plotter")

window_height = 120
window_width = 340

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

window.resizable(False, False)



## GUI Widgets.

# Equation.
equation_txt = Entry(window, width=50, borderwidth=4)
equation_txt.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
equation_txt.insert(0, "Equation ex: (5*x^3 + x**2 - 8/x)")

def clear_equation_placeholder(event):
    equation_txt.delete(0, END)
    equation_txt.unbind('<Button-1>', clear_equation_placeholder_id)
clear_equation_placeholder_id = equation_txt.bind('<Button-1>', clear_equation_placeholder)


# Min value.
min_value_txt = Entry(window, borderwidth=2)
min_value_txt.grid(row=1, column=0)
min_value_txt.insert(0, "Min value")

def clear_min_placeholder(event):
    min_value_txt.delete(0, END)
    min_value_txt.unbind('<Button-1>', clear_min_placeholder_id)
clear_min_placeholder_id = min_value_txt.bind('<Button-1>', clear_min_placeholder)


# Max value.
max_value_txt = Entry(window, borderwidth=2)
max_value_txt.grid(row=1, column=1)
max_value_txt.insert(0, "Max value")

def clear_max_placeholder(event):
    max_value_txt.delete(0, END)
    max_value_txt.unbind('<Button-1>', clear_max_placeholder_id)
clear_max_placeholder_id = max_value_txt.bind('<Button-1>', clear_max_placeholder)



# Plot btn.

def plot():
    
    try:
        equation = equation_txt.get().replace('^', '**')


        if(not validate.is_equation(equation)):
            raise ValueError("Invalid Equation expression!")
        

        if(not validate.is_number(min_value_txt.get())):
            raise ValueError("Min Value is NOT a number!")
        

        if(not validate.is_number(max_value_txt.get())):
            raise ValueError("Max Value is NOT a number!")


        min_value = int(min_value_txt.get())
        max_value = int(max_value_txt.get())

        if(not validate.is_min_less_max(min_value, max_value)):
            raise ValueError("Min Value must be less than max value!")

        
        plotter.function_plot(equation=equation, min=min_value, max=max_value)

    except ValueError as err:
        messagebox.showinfo("INVALID INPUT!!",  err)
        print(err)




plot_btn = Button(window, text="Plot", command= plot, padx=50, pady=5)
plot_btn.grid(row=3, column=0, padx=10, pady=10, columnspan=2)



def on_closing():
    plotter.plt.close('all')
    window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

window.mainloop()
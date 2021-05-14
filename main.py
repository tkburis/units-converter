import tkinter
from tkinter import ttk
import functions

# window setup
root = tkinter.Tk()
root.resizable(False, False)

# input frame
input_frame = ttk.Frame(root)
input_frame.grid(row=0)

input_label = ttk.Label(input_frame, text='Enter value: ')
input_label.grid(row=0, column=0)

input_entry = ttk.Entry(input_frame)
input_entry.grid(row=0, column=1)

# output frame
output_frame = ttk.Frame(root)
output_frame.grid(row=2)

output_label = ttk.Label(output_frame, text='Result: ')
output_label.grid(row=0, column=0)
output_entry = ttk.Entry(output_frame)
output_entry.grid(row=0, column=1)

funcs = functions.Functions(input_entry, output_entry)

# button frame
button_frame = ttk.Frame(root)
button_frame.grid(row=1)

ttk.Button(button_frame, text='kg to lb', command=lambda: funcs.conv("kg_to_lb")).grid(row=0, column=0)
ttk.Button(button_frame, text='lb to kg', command=lambda: funcs.conv("lb_to_kg")).grid(row=1, column=0)
ttk.Button(button_frame, text='cm to in', command=lambda: funcs.conv("cm_to_in")).grid(row=0, column=1)
ttk.Button(button_frame, text='in to cm', command=lambda: funcs.conv("in_to_cm")).grid(row=1, column=1)
ttk.Button(button_frame, text='ms to mph', command=lambda: funcs.conv("ms_to_mph")).grid(row=0, column=2)
ttk.Button(button_frame, text='mph to ms', command=lambda: funcs.conv("mph_to_ms")).grid(row=1, column=2)

# main loop
root.mainloop()

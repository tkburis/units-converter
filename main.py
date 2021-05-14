import tkinter
from tkinter import ttk
import functions

# window setup
root = tkinter.Tk()
root.resizable(False, False)
root.title('Units converter')
root.grid_propagate(0)
root.geometry('600x300')

# input frame
input_frame = ttk.Frame(root)
input_frame.grid(row=0)

input_label = ttk.Label(input_frame, text='Enter value: ')
input_label.grid(row=0, column=0)

input_var = tkinter.StringVar()

input_entry = ttk.Entry(input_frame, textvariable=input_var, font=('Arial', 15))
input_entry.grid(row=0, column=1)

# output frame
output_frame = ttk.Frame(root)
output_frame.grid(row=2)

output_label = ttk.Label(output_frame, text='Result: ')
output_label.grid(row=0, column=0)
output_entry = ttk.Entry(output_frame, font=('Arial', 15))
output_entry.grid(row=0, column=1)

# initialise Functions object
funcs = functions.Functions(input_entry, output_entry)
input_var.trace_add('write', funcs.input_tracer)

# button frame
button_frame = ttk.Frame(root)
button_frame.grid(row=1)

unit_outputs = dict()

ttk.Button(button_frame, text='kg to lb', command=lambda: funcs.conv("kg_to_lb")).grid(row=0, column=0, ipady=10)
unit_outputs['kg_to_lb'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['kg_to_lb'].grid(row=1, column=0, ipady=10)
ttk.Button(button_frame, text='lb to kg', command=lambda: funcs.conv("lb_to_kg")).grid(row=2, column=0, ipady=10)
unit_outputs['lb_to_kg'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['lb_to_kg'].grid(row=3, column=0, ipady=10)

ttk.Button(button_frame, text='cm to in', command=lambda: funcs.conv("cm_to_in")).grid(row=0, column=1, ipady=10)
unit_outputs['cm_to_in'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['cm_to_in'].grid(row=1, column=1, ipady=10)
ttk.Button(button_frame, text='in to cm', command=lambda: funcs.conv("in_to_cm")).grid(row=2, column=1, ipady=10)
unit_outputs['in_to_cm'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['in_to_cm'].grid(row=3, column=1, ipady=10)

ttk.Button(button_frame, text='ms to mph', command=lambda: funcs.conv("ms_to_mph")).grid(row=0, column=2,ipady=10)
unit_outputs['ms_to_mph'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['ms_to_mph'].grid(row=1, column=2, ipady=10)
ttk.Button(button_frame, text='mph to ms', command=lambda: funcs.conv("mph_to_ms")).grid(row=2, column=2,ipady=10)
unit_outputs['mph_to_ms'] = ttk.Entry(button_frame, font=('Arial', 13))
unit_outputs['mph_to_ms'].grid(row=3, column=2, ipady=10)

setattr(funcs, 'unit_outputs', unit_outputs)

# live? checkbox
hide_unit_outputs = tkinter.IntVar()


def toggle_show_hide():
    global hide_unit_outputs
    if hide_unit_outputs:
        for unit_output in unit_outputs.values():
            unit_output.grid()
        output_frame.grid_remove()
    else:
        for unit_output in unit_outputs.values():
            unit_output.grid_remove()
        output_frame.grid()
    hide_unit_outputs = not hide_unit_outputs


for _ in range(2):
    toggle_show_hide()
live_checkbox = ttk.Checkbutton(input_frame, text='Live?', command=toggle_show_hide,
                                variable=hide_unit_outputs, onvalue=True, offvalue=False)
live_checkbox.grid(row=0, column=2)

# main loop
root.mainloop()

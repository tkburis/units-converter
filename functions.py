from tkinter import END


class Functions:
    conv_factors = {
        'kg_to_lb': 2.2046,
        'lb_to_kg': 1 / 2.2046,
        'cm_to_in': 0.3937,
        'in_to_cm': 1 / 0.3937,
        'ms_to_mph': 2.2369,
        'mph_to_ms': 1 / 2.2369
    }

    def __init__(self, inputentry, outputentry):
        self.unit_outputs = None
        self.inputentry = inputentry
        self.outputentry = outputentry

    def get_arg(self):
        try:
            arg = float(self.inputentry.get())
        except ValueError:
            arg = 0
        return arg

    def update_output(self, arg, output):
        output.delete(0, END)
        output.insert(0, arg)

    def conv(self, units, output=None):
        output = output if output is not None else self.outputentry
        self.update_output(round(self.get_arg() * self.conv_factors[units], 2), output)

    def input_tracer(self, var, idx, mode):
        if self.unit_outputs is None:
            print("Something's gone terribly wrong...")
            return
        for units, unit_output in self.unit_outputs.items():
            self.conv(units, unit_output)

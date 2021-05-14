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
        self.inputentry = inputentry
        self.outputentry = outputentry

    def get_arg(self):
        try:
            arg = int(self.inputentry.get())
        except ValueError:
            arg = 0
        return arg

    def update_output(self, arg):
        self.outputentry.delete(0, END)
        self.outputentry.insert(0, arg)

    def conv(self, units):
        self.update_output(round(self.get_arg() * self.conv_factors[units], 2))

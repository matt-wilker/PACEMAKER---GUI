import tkinter as tk
import json


class parameter_page:
    def __init__(self, root, user, parameter_database):
        # Intialize Current User
        self.user = user

        # Intialize database
        self.DB = parameter_database

        # Intialize parameter limits
        self.limits = {
            "lrl": {
                "column": 2,
                "row": 1
            },
            "url": {
                "column": 2,
                "row": 2
            },
            "aa": {
                "column": 2,
                "row": 3
            },
            "apw": {
                "column": 2,
                "row": 4
            },
            "va": {
                "column": 6,
                "row": 1
            },
            "vpw": {
                "column": 6,
                "row": 2
            },
            "VRP": {
                "column": 6,
                "row": 3
            },
            "ARP": {
                "column": 6,
                "row": 4
            }
        }

        # Build canvas
        self.root = root
        #self.window = tk.Toplevel(self.root)
        self.root.destroy()

        self.window = tk.Tk()
        self.window.title("Parameters")
        self.canvas = tk.Canvas(self.window, width=1000, height=500)
        self.canvas.grid(columnspan=8, rowspan=6)

        self.title_label = tk.Label(self.window, text="Parameters", font=("Raleway", 18))
        self.title_label.grid(column=0, row=0)

        # Initialize all Entry fields
        self.lrl = tk.Entry(self.window)
        self.lrl.grid(column=1, row=1)
        self.url = tk.Entry(self.window)
        self.url.grid(column=1, row=2)
        self.aa = tk.Entry(self.window)
        self.aa.grid(column=1, row=3)
        self.apw = tk.Entry(self.window)
        self.apw.grid(column=1, row=4)
        self.va = tk.Entry(self.window)
        self.va.grid(column=5, row=1)
        self.vpw = tk.Entry(self.window)
        self.vpw.grid(column=5, row=2)
        self.VRP = tk.Entry(self.window)
        self.VRP.grid(column=5, row=3)
        self.ARP = tk.Entry(self.window)
        self.ARP.grid(column=5, row=4)

        # Initialize Labels
        self.lrl_label = tk.Label(self.window, text="Lower Rate Limit", font=("Raleway", 12))
        self.lrl_label.grid(column=0, row=1)
        self.url_label = tk.Label(self.window, text="Upper Rate Limit", font=("Raleway", 12))
        self.url_label.grid(column=0, row=2)
        self.aa_label = tk.Label(self.window, text="Atrial Amplitude", font=("Raleway", 12))
        self.aa_label.grid(column=0, row=3)
        self.apw_label = tk.Label(self.window, text="Atrial Pulse Width", font=("Raleway", 12))
        self.apw_label.grid(column=0, row=4)
        self.va_label = tk.Label(self.window, text="Ventricular Amplitude", font=("Raleway", 12))
        self.va_label.grid(column=4, row=1)
        self.vpw_label = tk.Label(self.window, text="Ventricular Pulse Width", font=("Raleway", 12))
        self.vpw_label.grid(column=4, row=2)
        self.VRP_label = tk.Label(self.window, text="VRP", font=("Raleway", 12))
        self.VRP_label.grid(column=4, row=3)
        self.ARP_label = tk.Label(self.window, text="ARP", font=("Raleway", 12))
        self.ARP_label.grid(column=4, row=4)

        # Intialize "invalid" label
        self.invalid_label = tk.Label(self.window, text="Invalid", font=("Raleway", 6))

        # Initialize Save Button
        save_btn_text = tk.StringVar()
        self.save_btn = tk.Button(self.window, textvariable=save_btn_text, command=self.check_validity,
                                    font="Raleway", bg="#20bebe", fg="white", height=1, width=60)
        save_btn_text.set("Save")
        self.save_btn.grid(columnspan=4, column=1, row=6)

    def check_lrl(self, lrl_input):
        # Check which range the lrl input falls in
        if 30 <= lrl_input <= 50 and lrl_input % 5 == 0:
            return True
        elif 90 <= lrl_input <= 175 and lrl_input % 5 == 0:
            return True
        else:
            self.invalid_label.grid(column=self.limits["lrl"]["column"], row=self.limits["lrl"]["row"])
            return False


    def check_url(self, url_input):
        # Check which range the lrl input falls in
        if 50 <= url_input <= 175 and lrl_input % 5 == 0:
            return True
        else:
            self.invalid_label.grid(column=self.limits["url"]["column"], row=self.limits["url"]["row"])
            return False


    def check_atrial_amplitude(self, amplitude_input):
        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input,1) == amplitude_input:
            return True
        else:
            self.invalid_label.grid(column=self.limits["aa"]["column"], row=self.limits["aa"]["row"])
            return False

    def check_ventrical_amplitude(self, amplitude_input):
        if 0.0 <= amplitude_input <= 5.0 and round(amplitude_input,1) == amplitude_input:
            return True
        else:
            self.invalid_label.grid(column=self.limits["va"]["column"], row=self.limits["va"]["row"])
            return False

    def check_apw(self, pw_input):
        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label.grid(column=self.limits["apw"]["column"], row=self.limits["apw"]["row"])
            return False

    def check_vpw(self, pw_input):
        if pw_input == 1 or pw_input == 2:
            return True
        else:
            self.invalid_label.grid(column=self.limits["vpw"]["column"], row=self.limits["vpw"]["row"])
            return False

    def check_atrial_refractory_period(self, RP_input):
        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label.grid(column=self.limits["ARP"]["column"], row=self.limits["ARP"]["row"])
            return False

    def check_ventricle_refractory_period(self, RP_input):
        if 150 <= RP_input <= 500 and RP_input % 10 == 0:
            return True
        else:
            self.invalid_label.grid(column=self.limits["VRP"]["column"], row=self.limits["VRP"]["row"])
            return False

    def check_validity(self):
        valid_params = [self.check_lrl(self.lrl.get()), self.check_url(self.url.get()),
                        self.check_atrial_amplitude(self.aa.get()), self.check_ventrical_amplitude(self.va.get()),
                        self.check_apw(self.apw.get()), self.check_vpw(self.vpw.get()),
                        self.check_atrial_refractory_period(self.ARP.get()), self.check_ventricle_refractory_period(self.VRP.get())]

        input_params = {
            "lrl": self.lrl.get(),
            "url": self.url.get(),
            "aa": self.aa.get(),
            "apw": self.apw.get(),
            "va": self.va.get(),
            "vpw": self.vpw.get(),
            "VRP": self.VRP.get(),
            "ARP": self.ARP.get()
        }
        # Checking lrl separately due to increment differences

        if False in valid_params:
            return
        else: self.save_parameters(input_params)


    def save_parameters(self, inputs):
        self.DB[self.user] = inputs
        print(self.DB)
        with open("database/parameters.json", "w") as destination:
            json.dump(self.DB, destination)
        self.window.destroy()

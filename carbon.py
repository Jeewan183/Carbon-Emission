import tkinter as tk
import psutil
import time

class CarbonEmissionsCalculator(tk.Frame):
    def _init_(self, master=None):
        super()._init_(master)
        self.master = master
        self.master.title('Carbon Emissions Calculator')
        self.master.geometry('500x400')

        # Create the Code input section
        self.create_code_input()

        # Create the Carbon Intensity input section
        self.create_carbon_intensity_input()

        # Create the Calculate button
        self.create_calculate_button()

        # Create the Result section
        self.create_result_section()

        self.pack()

    def create_code_input(self):
        code_label = tk.Label(self, text='Enter Code:', font=('Arial', 14))
        code_label.pack(side=tk.TOP, padx=20, pady=20, anchor=tk.W)

        self.code_text = tk.Text(self, width=50, height=10, font=('Arial', 12))
        self.code_text.pack(side=tk.TOP, padx=20, pady=10)

    def create_carbon_intensity_input(self):
        carbon_intensity_label = tk.Label(self, text='Enter Carbon Intensity (kgCO2e/kWh):', font=('Arial', 14))
        carbon_intensity_label.pack(side=tk.TOP, padx=20, pady=20, anchor=tk.W)

        self.carbon_intensity_entry = tk.Entry(self, font=('Arial', 12))
        self.carbon_intensity_entry.insert(0, '0.475')
        self.carbon_intensity_entry.pack(side=tk.TOP, padx=20, pady=10)

    def create_calculate_button(self):
        calculate_button = tk.Button(self, text='Calculate', font=('Arial', 14), bg='#007FFF', fg='white', activebackground='#007FFF', activeforeground='white', command=self.calculate_emissions)
        calculate_button.pack(side=tk.TOP, padx=20, pady=20)

    def create_result_section(self):
        result_frame = tk.Frame(self)
        result_frame.pack(side=tk.TOP, padx=20, pady=20)

        result_label_text = tk.Label(result_frame, text='Carbon emissions:', font=('Arial', 14))
        result_label_text.pack(side=tk.LEFT)

        self.result_label = tk.Label(result_frame, text='', font=('Arial', 14, 'bold'))
        self.result_label.pack(side=tk.LEFT)

    def calculate_emissions(self):
        code = self.code_text.get('1.0', 'end-1c')
        carbon_intensity = float(self.carbon_intensity_entry.get())

        energy_consumed = self.measure_energy_consumption(lambda: exec(code))
        carbon_emissions = self.calculate_carbon_emissions(energy_consumed, carbon_intensity)

        self.result_label.config(text=f'{carbon_emissions:.3f} kgCO2e')

    def measure_energy_consumption(self, code_func):
        start_time = time.time()
        code_func()
        end_time = time.time()

        energy_consumed = psutil.cpu_percent() * (end_time - start_time)
        return energy_consumed

    def calculate_carbon_emissions(self, energy_consumed, carbon_intensity):
        energy_consumed_kwh = energy_consumed / (1000 * 3600)
        carbon_emissions = energy_consumed_kwh * carbon_intensity
        return carbon_emissions

root = tk.Tk()
app = CarbonEmissionsCalculator(master=root)
app.mainloop()
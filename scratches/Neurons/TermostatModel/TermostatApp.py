import tkinter as tk
from tkinter import ttk
import random


class TermostatAgent:
    def __init__(self, setpoint):
        self.setpoint = setpoint

    def perceive(self, current_temperature):
        return current_temperature

    def decide(self, current_temperature):
        if current_temperature <= self.setpoint:
            return 'heating_on'
        else:
            return 'heating_off'

    def act(self, decision):
        return "Azioni: 🔥 Riscaldamento acceso" if decision == 'heating_on' else "Azioni: ❄️ Riscaldamento spento"


class ThermostatApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulatore Termostato Intelligente")

        self.setpoint = tk.DoubleVar(value=20.0)
        self.temperature = tk.DoubleVar(value=18.0)
        self.status = tk.StringVar(value="In attesa...")

        self.agent = TermostatAgent(self.setpoint.get())

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Setpoint (°C):").grid(column=0, row=0, sticky="w")
        ttk.Entry(self.root, textvariable=self.setpoint).grid(column=1, row=0)

        ttk.Label(self.root, text="Temperatura iniziale (°C):").grid(column=0, row=1, sticky="w")
        ttk.Entry(self.root, textvariable=self.temperature).grid(column=1, row=1)

        self.start_button = ttk.Button(self.root, text="Avvia Simulazione", command=self.start_simulation)
        self.start_button.grid(column=0, row=2, columnspan=2, pady=10)

        ttk.Label(self.root, text="Temperatura Attuale:").grid(column=0, row=3, sticky="w")
        self.temp_label = ttk.Label(self.root, textvariable=self.temperature)
        self.temp_label.grid(column=1, row=3, sticky="w")

        ttk.Label(self.root, text="Stato Riscaldamento:").grid(column=0, row=4, sticky="w")
        self.status_label = ttk.Label(self.root, textvariable=self.status)
        self.status_label.grid(column=1, row=4, sticky="w")

    def start_simulation(self):
        self.agent.setpoint = self.setpoint.get()
        self.simulate_step(0)

    def simulate_step(self, step):
        if step >= 10:
            self.status.set("Simulazione completata.")
            return

        current_temp = self.temperature.get()
        decision = self.agent.decide(current_temp)
        status_text = self.agent.act(decision)
        self.status.set(status_text)

        if decision == 'heating_on':
            new_temp = current_temp + random.uniform(0.2, 0.5)
        else:
            new_temp = current_temp - random.uniform(0.1, 0.3)

        self.temperature.set(round(new_temp, 1))
        self.root.after(500, lambda: self.simulate_step(step + 1))

if __name__ == "__main__":
    root = tk.Tk()
    app = ThermostatApp(root)
    root.mainloop()



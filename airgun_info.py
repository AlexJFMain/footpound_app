# Creator       : Alex Fedok
# Updated as of : 2021-07-22

# Dependencies.
import tkinter as tk
import tkinter.ttk as ttk

# Variables.
width = 132
height = 225
primaryColor = "#454545"
secondaryColor = "#454545"
buttonHeight = 2
buttonWidth = 14

# Helper Functions.
#--------------------------------------------------------------
# Converts grain and fps-velocity to footpound and joule.
def footPound(grainMass, velocity):
    return round((1/450240) * grainMass * velocity * velocity, 2), round((1/450240) * grainMass * velocity * velocity * 1.35582, 2)
#--------------------------------------------------------------

# Create window.
class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.grainMassText = tk.Label(self, text="Mass (Grains): ")
        self.grainMassText.pack(side="top")

        self.grainMassInput = tk.Entry(self, bd=5)
        self.grainMassInput.pack(side="top")

        self.velocityText = tk.Label(self, text="Velocity (FPS): ")
        self.velocityText.pack(side="top")

        self.velocityInput = tk.Entry(self, bd=5)   
        self.velocityInput.pack(side="top")

        self.energyText = tk.Label(self, text="Energy (FPE, Joules): ")
        self.energyText.pack(side="top")

        self.energyInput = tk.Entry(self, bd=5)
        self.energyInput.config(state="readonly")
        self.energyInput.pack(side="top")

        self.calculate_energy = tk.Button(self, text="Calculate Energy",  bg = secondaryColor, fg="#04FF00", width = buttonWidth, height = buttonHeight, font="Helvetica 10 bold", command=self.calculateEnergy)
        self.calculate_energy.pack(side="top")

        self.quit = tk.Button(self, text="Exit", bg = secondaryColor, fg="#FF3600", width = buttonWidth, height = buttonHeight, font="Helvetica 10 bold", command=self.master.destroy)
        self.quit.pack(side="bottom")

    def calculateEnergy(self):
        self.energyInput.config(state="normal")
        try:
            energyCalculation = footPound(float(self.grainMassInput.get()), float(self.velocityInput.get()))
            self.energyInput.delete(0, "end")
            self.energyInput.insert(0, str(energyCalculation[0]) + ", " + str(energyCalculation[1])) 
        except:
            self.energyInput.delete(0, "end")
            self.energyInput.insert(0, "Invalid input(s)")
        self.energyInput.config(state="readonly")

# Main portion.
root = tk.Tk()
app = App(root)

root.configure(background=primaryColor)
root.resizable(False, False)

root.title("Simple Airgun App")
root.geometry("%dx%d" % (width, height))

app.mainloop()




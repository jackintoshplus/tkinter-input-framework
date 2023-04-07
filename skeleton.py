import sys
import tkinter as tk
import tkinter.ttk as ttk


#Data Storage
statusLabelText = "Ready"


#Window Building
root = tk.Tk()
root.title("Input Framework") #Program Title
frame = ttk.Frame(root, padding=5)
frame.grid()


#Input Process Command
def processInputBox():
        dataFromInputBox = inputBox.get()

        if(dataFromInputBox == ""): #No Data Entered
                #Play System Bell
                root.bell()

                statusLabelText = "No Data Entered."
                statusText.config(text = statusLabelText)
                print("No Data Recieved.")
        else:
                print("Processing")
                statusLabelText = "Processing..."
                statusText.config(text = statusLabelText)
                processData(dataFromInputBox)


#Data Processing Function
def processData(data):
        print("Data Recieved: " + data)


#Main UI
ttk.Label(frame, text="Input Data:").grid(column=0, row=0) #Input Data Label
runEntry = ttk.Button(frame, text="Enter", command=processInputBox).grid(column=0, row=1) #Enter Button

statusText = ttk.Label(frame, text="Ready") #Status Text
statusText.grid(column=1, row=1)

inputBox = tk.Entry(frame) #Input Box
inputBox.grid(column=1, row=0)


#Cleanup and Run
root.mainloop()

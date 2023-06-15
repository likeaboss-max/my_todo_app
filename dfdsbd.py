import PySimpleGUI as sg

def km_to_miles(km):
    return km/1.6

label = sg.Text("Kilometres: ")
input_box = sg.InputText(tooltip="Enter todo", key="kms")
miles_button = sg.Button("Convert")

output = sg.Text(key="output")

window = sg.Window('Km to miles convertor',
                   layout=[[label,input_box],[miles_button,output]],
                   font=('Helvetica',20))

while True:
    event,values = window.read()
    match event:
         case "Convert":
             km = float(values["kms"])
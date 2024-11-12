
from pathlib import Path
import re
from tkinter import *
import customtkinter
import tkinter as tk
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, ttk, messagebox
from PIL import Image, ImageTk
from openpyxl import load_workbook
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd
from datetime import datetime


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"path")

def calcular_tiempo_esperado(informesRealizados):
    tiempo_esperado = 0
    informes = informesRealizados.split()
    #Definición de tiempos objetivo:
    objetivo_por_tipo={
        'a':1,
        'b':3,
        'c':6
        }
    
    for grupo in informes:
        valor_numerico = float(grupo[:-1]) if grupo[:-1].replace('.', '').isdigit() else 1.0
        letra = grupo[-1]
        tiempo_esperado += valor_numerico * objetivo_por_tipo[letra]
    
    return tiempo_esperado

def guardar_datos():

    if not validar_datos():
        return
    iniciales = entry_iniciales.get()
    fecha = entry_fecha.get()

    if not iniciales or not fecha:
        tk.messagebox.showerror("Error", "Los campos de 'Iniciales' y 'Fecha' no pueden estar vacíos.")
        return

    informesRealizados = entry_informes2.get()
    if informesRealizados:
        tiempo_esperado = calcular_tiempo_esperado(informesRealizados)
    else:
        tiempo_esperado=""

    tiempo_real = entry_informes.get()
    if tiempo_real:
        tiempo_real = float(tiempo_real)
        eficiencia = (tiempo_esperado / tiempo_real) * 100
    else:
        eficiencia = ""
    
    datos_filas = [
        {
            "Iniciales": iniciales,
            "Fecha": fecha,
            "Tipo": "Informes",
            "Detalle": entry_informes.get(),
            "Informes2": entry_informes2.get(),
            "TiempoEsperado":tiempo_esperado,
            "Eficiencia":eficiencia,
            "Observaciones": entry_informes3.get()
         },
        {
            "Iniciales": iniciales,
            "Fecha": fecha,
            "Tipo": "ocupacion1",
            "Detalle": entry_ocupacion1.get(),
            "Informes2": "",
            "TiempoEsperado":"",
            "Eficiencia":"",
            "Observaciones": entry_ocupacion13.get()
        },
        {
            "Iniciales": iniciales,
            "Fecha": fecha,
            "Tipo": "Almacén",
            "Detalle": entry_ocupacion2.get(),
            "Informes2": "",
            "TiempoEsperado":"",
            "Eficiencia":"",
            "Observaciones": entry_ocupacion23.get()
        },
        {
            "Iniciales": iniciales,
            "Fecha": fecha,
            "Tipo": "ocupacion3",
            "Detalle": entry_ocupacion3.get(),
            "Informes2": "",
            "TiempoEsperado":"",
            "Eficiencia":"",
            "Observaciones": entry_ocupacion33.get()
        },
        {
            "Iniciales": iniciales,
            "Fecha": fecha,
            "Tipo": "Otros",
            "Detalle": entry_otros.get(),
            "Informes2": "",
            "TiempoEsperado":"",
            "Eficiencia":"",
            "Observaciones": entry_otros3.get()
        }
    ]

    datos_filas_filtradas = [fila for fila in datos_filas if (fila["Detalle"] and fila["Detalle"]!="0")]

    if not datos_filas_filtradas:
        tk.messagebox.showinfo("Información", "No hay datos para guardar.")
        return
    
    df = pd.DataFrame(datos_filas_filtradas)

    archivo_excel = Path('path').resolve()

    book = load_workbook(archivo_excel)
    sheet = book['Hoja1']

    rows = dataframe_to_rows(df, index=False, header=False)
    for r_idx, row in enumerate(rows, start=sheet.max_row+1):
        for c_idx, value in enumerate(row, start=1):
            cell = sheet.cell(row=r_idx, column=c_idx)
            if c_idx == 2:
                date_obj = datetime.strptime(value, '%d/%m/%Y')
                cell.value = date_obj
                cell.number_format = 'DD/MM/YYYY'
            elif c_idx == 4:
                try:
                    numeric_value = float(value)
                    cell.value = numeric_value
                    cell.number_format = '0.00'
                except ValueError:
                    cell.value = value
                    cell.number_format = '0.00'
            else:
                cell.value = value
    book.save(archivo_excel)

    if eficiencia:
        tk.messagebox.showinfo("¡GRACIAS!", f"¡Hoy has tenido una eficiencia del {round(eficiencia)}%!.\nEl registro se ha guardado con éxito.")
    else:
        tk.messagebox.showinfo("¡GRACIAS!", "El registro se ha guardado con éxito.")
    cancelar()

def validar_datos():
    for entry in [entry_informes, entry_ocupacion1, entry_ocupacion2, entry_ocupacion3, entry_otros]:
        try:
            if entry.get() != "":
                float(entry.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Hay texto en la columna de tiempos.")
            return False

    if not all(re.match(r"^\d*\.?\d+[abc]$", grupo) or grupo in ["a", "b", "c"] for grupo in entry_informes2.get().split()):
        tk.messagebox.showerror("Error", "El campo de informes realizados debe contener solo las letras a, b, c (o múltiplos de ellas).Además deben estar separadas por un espacio.")
        return False

    if entry_iniciales.get() == "":
        tk.messagebox.showerror("Error", "El campo 'Iniciales' debe estar cubierto.")
        return False
    
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", entry_fecha.get()):
        tk.messagebox.showerror("Error", "El formato de la fecha debe ser DD/MM/AAAA.")
        return False
    try:
        fecha=datetime.strptime(entry_fecha.get(), "%d/%m/%Y")
    except ValueError:
        tk.messagebox.showerror("Error", "Esa fecha no existe.")
        return False
    if fecha > datetime.today():
        tk.messagebox.showerror("Error", "No puedes introducir datos futuros.")
        return False
    
    return True

def cancelar():
    window.destroy()

def borrar_campos():
    entry_iniciales.set("None")
    entry_fecha.delete(0, tk.END)
    entry_informes.delete(0, tk.END)
    entry_informes2.delete(0, tk.END)
    entry_informes3.delete(0, tk.END)
    entry_ocupacion1.delete(0, tk.END)
    entry_ocupacion13.delete(0, tk.END)
    entry_ocupacion2.delete(0, tk.END)
    entry_ocupacion23.delete(0, tk.END)
    entry_ocupacion3.delete(0, tk.END)
    entry_ocupacion33.delete(0, tk.END)
    entry_otros.delete(0, tk.END)
    entry_otros3.delete(0, tk.END)

def ruta_absoluta(relative_path):
    #---------- Descomentar antes de convertir en ejecutable ----------#
    #try:
    #    base_path = sys._MEIPASS
    #except Exception:
    #    base_path = os.path.abspath(".")
    #return os.path.join(base_path, relative_path)
    #---------- Comentar antes de convertir en ejecutable ----------#
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, relative_path)

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def load_image(file_path):
                image = Image.open(file_path)
                photo_image=ImageTk.PhotoImage(image)
                return photo_image
            
def main():
    global window, entry_iniciales, entry_fecha, entry_informes, entry_informes2, entry_informes3, entry_ocupacion1, entry_ocupacion13, entry_ocupacion2, entry_ocupacion23, entry_ocupacion3, entry_ocupacion33, entry_otros, entry_otros3
#Ventana principal
    window = customtkinter.CTk()
    window.title("Titulo")
    window.iconbitmap(r"path")
    window.geometry("700x550")
    window.configure(bg = "#FFFF")


    lista_empleados = ['nombre1', 'nombre2', 'nombre3', 'nombre4', 'nombre5', 'nombre6'] 

    canvas = Canvas(
        window,
        bg = "white",
        height = 550,
        width = 700,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

#Cargar imagen

    image = Image.open(r"path")
    image = image.resize( (205,82), Image.LANCZOS)

    img = ImageTk.PhotoImage(image)
    lbl_img = Label(window, 
                    image = img,
                    background=  "white")
    lbl_img.place(x=400, y=100)


#Titulo dentro de ventana
    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        0.0,
        0.0,
        700.0,
        85.0,
        fill="#0E2E5E",
        outline="")


    canvas.create_text(
        33.0,
        25.0,
        anchor="nw",
        text="Titulo",
        fill="#FFFFFF",
        font=("JockeyOne Regular", 24 * -1)
    )

#INICIALES

    combobox_var = customtkinter.StringVar(value="None")  # set initial value

    def combobox_callback(choice):
        print("combobox dropdown clicked:", choice)

    entry_iniciales =  customtkinter.CTkComboBox(window,
                                          height=23,
                                          width=93,
                                          font=("KleeOne Regular", 13 * -1),
                                          corner_radius=10,
                                          border_color= "#0E2E5E",
                                          bg_color= "white",
                                          fg_color= "#D9D9D9",
                                          button_color= "#9E9E9E",
                                          dropdown_fg_color= "#0E2E5E",
                                          text_color= "#0E2E5E",
                                          text_color_disabled= "#D9D9D9",
                                          values=['I01', 'I02', 'I03', 'I04', 'I05', 'I06'],
                                          command=combobox_callback,
                                          variable=combobox_var
                                          )
    entry_iniciales.place_configure(x=234, y=123, anchor=tk.CENTER)

    canvas.create_text(
        33.0,
        112.0,
        anchor="nw",
        text="Iniciales:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

#FECHA

    canvas.create_text(
        33.0,
        162.0,
        anchor="nw",
        text="Fecha (DD/MM/AAA):",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

    fecha_hoy = datetime.today().strftime('%d/%m/%Y')
    entry_fecha = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_fecha.place(x=234, y=170, anchor=tk.CENTER)
    entry_fecha.insert(0, fecha_hoy)


# TIEMPO [H]
    canvas.create_text(
        199.0,
        214.0,
        anchor="nw",
        text="Tiempo [h]:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

#TIPOS DE INFORMES
    canvas.create_text(
        372.0,
        214.0,
        anchor="nw",
        text="Tipo informes:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )


#OBSERVACIONES
    canvas.create_text(
        545.0,
        214.0,
        anchor="nw",
        text="Observaciones:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )


#INFORMES
    canvas.create_text(
        33.0,
        256.0,
        anchor="nw",
        text="Informes:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

    # -- Tiempo [H]
    entry_informes = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_informes.place(x=234, y=266, anchor=tk.CENTER)
    entry_informes.get()

    # -- Tipo de Informe
    entry_informes2 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_informes2.place(x=415, y=266, anchor=tk.CENTER)
    entry_informes2.get()

    #--Observaciones
    entry_informes3 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_informes3.place(x=590, y=266, anchor=tk.CENTER)
    entry_informes3.get()

#Ocupacion 1
    canvas.create_text(
        33.0,
        301.0,
        anchor="nw",
        text="Ocupacion 1:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

    #--Tiempo
    entry_ocupacion1 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion1.place(x=234, y=309, anchor=tk.CENTER)
    entry_ocupacion1.get()

    #--observaciones
    entry_ocupacion13 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion13.place(x=590, y=307, anchor=tk.CENTER)
    entry_ocupacion13.get()

#Ocupacion 2
    canvas.create_text(
        33.0,
        346.0,
        anchor="nw",
        text="Ocupación 2",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )
    #--Tiempo[h]
    entry_ocupacion2 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion2.place(x=234, y=353, anchor=tk.CENTER)
    entry_ocupacion2.get()

    #--Observaciones
    entry_ocupacion23 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion23.place(x=590, y=353, anchor=tk.CENTER)
    entry_ocupacion23.get()

#Ocupacion 3
    canvas.create_text(
        33.0,
        391.0,
        anchor="nw",
        text="ocupacion3:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )

    #--tiempo[h]
    entry_ocupacion3 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion3.place(x=234, y=397, anchor=tk.CENTER)
    entry_ocupacion3.get()

    #--observaciones
    entry_ocupacion33 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_ocupacion33.place(x=590, y=397, anchor=tk.CENTER)
    entry_ocupacion33.get()

#OTROS
    canvas.create_text(
        33.0,
        436.0,
        anchor="nw",
        text="Ocupación 3:",
        fill="#0E2E5E",
        font=("KleeOne Regular", 13 * -1)
    )
    #--tiempo[h]
    entry_otros = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_otros.place(x=234, y=445, anchor=tk.CENTER)
    entry_otros.get()

    #--observaciones
    entry_otros3 = customtkinter.CTkEntry(window,
                                height=23,
                                width=93,
                                font=("KleeOne Regular", 13 * -1),
                                corner_radius=10,
                                border_color= "#0E2E5E",
                                bg_color= "white",
                                fg_color= "#D9D9D9",
                                text_color= "#0E2E5E",
                                )
    entry_otros3.place(x=590, y=445, anchor=tk.CENTER)
    entry_otros3.get()


    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    btn_cancelar = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=cancelar,
        #command=lambda: print("btn_cancelar clicked"),
        relief="flat"
    )
    btn_cancelar.place(
        x=79.0,
        y=486.0,
        width=109.0,
        height=41.0
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    btn_borrar = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=borrar_campos,
        #command=lambda: print("btn_borrar clicked"),
        relief="flat"
    )
    btn_borrar.place(
        x=313.0,
        y=486.0,
        width=107.0,
        height=38.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    btn_guardar = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=guardar_datos,
        #command=lambda: print("btn_guardar clicked"),
        relief="flat"
    )
    btn_guardar.place(
        x=538.0,
        y=486.0,
        width=109.0,
        height=41.0
    )


    window.resizable(False, False)
    window.mainloop()

if __name__ == "__main__":
    main()

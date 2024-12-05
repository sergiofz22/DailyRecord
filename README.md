# Registro Diario de Actividades con Tkinter

Esta es una aplicación de escritorio desarrollada en Python que permite a los usuarios registrar actividades diarias, calcular tiempos esperados y eficiencias, y guardar los datos en un archivo Excel. Está diseñada para facilitar el seguimiento y la organización de tareas.

---

## 📝 Descripción

El programa proporciona una interfaz gráfica intuitiva para gestionar registros diarios, con campos específicos para iniciales, fecha, detalles de tareas, tiempo esperado y observaciones. Los datos se validan automáticamente antes de guardarse en un archivo Excel para su análisis posterior.

---

## 🚀 Características

- **Interfaz gráfica moderna:** Construida con `Tkinter` y `CustomTkinter`.
- **Cálculo de eficiencia:** Basado en el tiempo real comparado con el tiempo esperado.
- **Validación de datos:** Verificación de formatos de tiempo, iniciales y fechas.
- **Almacenamiento en Excel:** Guarda automáticamente los datos en una hoja de cálculo.
- **Cálculo automático:** Genera tiempos esperados y evalúa la eficiencia.
- **Fácil uso:** Ideal para mantener registros laborales diarios.

---

## 📂 Estructura del Proyecto

Asegúrate de que los recursos (imágenes y archivo Excel) estén organizados como se muestra a continuación:

proyecto/
├── main.py
├── requirements.txt
├── assets/
│   ├── images/
│   │   ├── image.ico
│   │   ├── image2.png
│   ├── frame0/
│       ├── button_1.png
│       ├── button_2.png
│       ├── button_3.png
├── data/
│   └── registro.xlsx

---

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/sergiofz22/DailyRecord.git
   cd DailyRecord

Instala las dependencias: Asegúrate de tener Python 3.8 o superior instalado. Luego, instala las dependencias:

pip install -r requirements.txt

---

## ⚙️ Uso

1. **Ejecuta el programa:**
   ```bash
   python main.py
   
Interfaz gráfica:

Ingresa tus iniciales y la fecha.
Completa los campos de actividades con tiempos y observaciones.
Verifica que las horas totales sumen correctamente.
Haz clic en "Guardar" para almacenar los datos en un archivo Excel.

Resultados:

Si los datos son válidos, se calculará la eficiencia y se mostrarán mensajes de confirmación.

---

##  📊 Funcionalidades Clave
1. Registro de Actividades
Permite registrar:

Iniciales del usuario.
Fecha en formato DD/MM/AAAA.
Tareas diarias divididas en categorías (informes, ocupación, otros).
Observaciones para cada actividad.
2. Validación
Tiempo: Los campos de tiempo deben ser valores numéricos.
Fecha: Validación del formato y que no sean fechas futuras.
Tareas: Solo se permiten valores específicos como `a`, `b`, `c`, `an` (o sus múltiplos).
3. Cálculo de Eficiencia
Compara el tiempo esperado con el tiempo real para calcular la eficiencia en porcentaje.

4. Almacenamiento en Excel
Guarda automáticamente los datos en un archivo Excel en la carpeta data.

---

##  🧩 Dependencias
Bibliotecas necesarias:
pathlib
tkinter
customtkinter
pandas
openpyxl
Pillow
Instala todas las dependencias ejecutando:

pip install -r requirements.txt



Aquí tienes un archivo README.md completo con toda la información detallada de tu proyecto:

markdown

# Registro Diario de Actividades con Tkinter

Esta es una aplicación de escritorio desarrollada en Python que permite a los usuarios registrar actividades diarias, calcular tiempos esperados y eficiencias, y guardar los datos en un archivo Excel. Está diseñada para facilitar el seguimiento y la organización de tareas laborales.

---

✨ Personalización
Puedes personalizar:

Diseño de la interfaz: Modifica colores, fuentes y diseño en el código.
Recursos gráficos: Reemplaza las imágenes en la carpeta assets/.

---

🛠️ Generación del Ejecutable
Instala PyInstaller:

pyinstaller --onefile --noconsole main.py

El archivo ejecutable estará en la carpeta dist.

---

🛡️ Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.



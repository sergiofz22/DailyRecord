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

![Sin título](https://github.com/user-attachments/assets/08dc5989-6ab6-4e0e-8c55-0dda1ecb667d)

---

## 🛠️ Instalación

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/sergiofz22/DailyRecord.git
   cd DailyRecord

Instala las dependencias: 

Asegúrate de tener Python 3.8 o superior instalado

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

---

##   ✨ Personalización
Puedes personalizar:

Diseño de la interfaz: Modifica colores, fuentes y diseño en el código.
Recursos gráficos: Reemplaza las imágenes en la carpeta assets/.

---

##   🛠️ Generación del Ejecutable
Instala PyInstaller:

pyinstaller --onefile --noconsole main.py

El archivo ejecutable estará en la carpeta dist.

---

## 🤝 Contribuciones y Soporte

Este proyecto está disponible gratuitamente bajo la licencia MIT. Si quieres contribuir, ¡eres bienvenido! También ofrezco los siguientes servicios adicionales:

- **Soporte técnico**: Ayuda para implementar o solucionar problemas.
- **Personalización**: Funcionalidades específicas adaptadas a tus necesidades.
- **Consultoría**: Asistencia para integrar este software en sistemas complejos.

📧 **Contáctame**: [sergiofz22@outlook.com](mailto:sergiofz22@outlook.com)

---

### 💖 ¿Te gusta este proyecto?
Si este proyecto te resulta útil, considera apoyarme con una donación para seguir mejorándolo:

[![Donate](https://img.shields.io/badge/Donate-PayPal-blue.svg)](https://paypal.me/sergiofz22)

---

##   🛡️ Licencia
Este proyecto está bajo la Licencia MIT.



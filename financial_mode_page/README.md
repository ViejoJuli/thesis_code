# Modelo Financiero: Comparación Alternativas Tradicionales (Call Center) vs Modelos Largos de Lenguaje para Servicio al Cliente

Este proyecto presenta un modelo financiero que permite comparar alternativas tradicionales de call center con modelos de lenguaje largo para servicio al cliente. La aplicación incluye un gráfico interactivo que se actualiza según varios parámetros ingresados por el usuario.

## Descripción

La aplicación web permite a los usuarios ingresar diferentes parámetros, como el rango de meses para la proyección, la tasa de interés, el número total de usuarios y el ratio de uso del servicio. Basándose en estos parámetros, el sistema generará una proyección visual que ayuda a entender el impacto financiero de cada modelo.

## Funcionalidades

- Interfaz gráfica interactiva basada en Plotly para visualizar datos financieros.
- Permite la entrada de parámetros que afectan la proyección financiera.
- Actualiza el gráfico dinámicamente en función de los parámetros ingresados.
- Presenta información sobre el costo por sesión de diferentes modelos de lenguaje.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

financial_mode_page/ ├── static/ │ └── styles.css # Estilos para la aplicación ├── templates/ │ └── index.html # Plantilla HTML para la aplicación ├── app.py # Código principal de la aplicación Flask └── requirements.txt # Dependencias del proyecto


### Archivos principales

- **`app.py`**: Archivo principal que contiene la lógica de la aplicación y gestiona las solicitudes del usuario.
- **`templates/index.html`**: Plantilla HTML que contiene la estructura y el contenido de la aplicación web.
- **`static/styles.css`**: Archivo CSS que define los estilos visuales de la aplicación.

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/ViejoJuli/thesis_code.git
cd thesis_code/financial_mode_page
```

2.Crea un entorno virtual (opcional pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:
```bash
Copy code
pip install -r requirements.txt
```

4. Ejecuta la aplicación:

```bash
Copy code
python app.py
```

5. Abre el navegador y accede a http://127.0.0.1:5000.

Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Agradecimientos
Plotly por proporcionar la biblioteca de gráficos interactivos.
Flask por ser un marco ligero y potente para construir aplicaciones web en Python.

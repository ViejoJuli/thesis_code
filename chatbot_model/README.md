# Modelo de Chatbot

Este repositorio contiene el código para un modelo de chatbot que utiliza técnicas de procesamiento de lenguaje natural (NLP) para interactuar con los usuarios de manera efectiva. El objetivo es ofrecer un servicio de atención al cliente automatizado y mejorar la experiencia del usuario a través de un sistema de conversación inteligente.

## Descripción

El modelo de chatbot implementa un flujo de conversación basado en las entradas del usuario y responde utilizando un modelo de lenguaje preentrenado. Está diseñado para manejar diversas consultas y proporcionar respuestas relevantes y coherentes.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

chatbot_model/ ├── src/ │ ├── chatbot.py # Lógica principal del chatbot │ ├── nlp_model.py # Carga y gestión del modelo NLP │ └── utils.py # Funciones utilitarias ├── requirements.txt # Dependencias del proyecto └── .env.example # Ejemplo de archivo de configuración de entorno

bash
Copy code

### Archivos principales

- **`src/chatbot.py`**: Archivo principal que contiene la implementación del chatbot y su lógica de interacción.
- **`src/nlp_model.py`**: Archivo que gestiona la carga y el uso del modelo de lenguaje.
- **`src/utils.py`**: Funciones auxiliares utilizadas en el proyecto.
- **`.env.example`**: Un archivo de ejemplo para las variables de entorno. Este archivo debe ser renombrado a `.env` y personalizado según tus necesidades.

## Instalación

1. Clona este repositorio:
 ```bash
 git clone https://github.com/ViejoJuli/thesis_code.git
 cd thesis_code/chatbot_model
```

2. Crea un entorno virtual (opcional pero recomendado):
```bash
Copy code
python -m venv venv
source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
```

3. Instala las dependencias:
```bash
Copy code
pip install -r requirements.txt
```

4. Configura tu archivo de entorno: Renombra el archivo .env.example a .env y completa las variables requeridas para tu entorno.
5. Ejecuta el chatbot:
```bash
streamlit run app.py
```

Uso
Una vez que hayas configurado el entorno y ejecutado el archivo app.py, podrás interactuar con el chatbot a través de la consola o mediante cualquier interfaz que hayas implementado.
Recuerda que es necesario tener una base de datos vectorial en Pinecone con la información que alimentara al chatbot

Contribuciones
Las contribuciones son bienvenidas. Si deseas colaborar, por favor sigue estos pasos:

Haz un fork del repositorio.
Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
Realiza tus cambios y haz commit (git commit -m 'Añadir nueva funcionalidad').
Sube tus cambios (git push origin feature/nueva-funcionalidad).
Abre un Pull Request.
Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

Agradecimientos
Hugging Face por proporcionar modelos de lenguaje preentrenados y herramientas de NLP.
Flask por ser un marco ligero y potente para construir aplicaciones web en Python (si corresponde al uso del chatbot en un contexto web).

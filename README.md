# Dashboard de Ventas - Streamlit

Una aplicación web simple desarrollada con Streamlit que muestra un dashboard de ventas con gráficos interactivos.

## Configuración del Entorno Virtual

### 1. Crear entorno virtual
```bash
python -m venv venv
```

### 2. Activar entorno virtual

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## Ejecutar la Aplicación

```bash
streamlit run app.py
```

La aplicación se ejecutará en `http://localhost:8501` con tema oscuro configurado.

## Características

- 📊 Gráfico de barras interactivo de ventas por producto
- 🌙 Tema oscuro configurado por defecto
- 📱 Interfaz responsive
- 📈 Datos de ventas ficticios para demostración

## Estructura del Proyecto

```
├── app.py                    # Aplicación principal
├── requirements.txt          # Dependencias del proyecto
├── .streamlit/
│   └── config.toml          # Configuración de Streamlit
└── README.md                # Este archivo
```
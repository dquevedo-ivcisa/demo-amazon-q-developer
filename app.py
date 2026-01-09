import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas", page_icon="📊")

# Título de bienvenida
st.title("¡Bienvenido al Dashboard de Ventas! 📊")
st.markdown("---")

# Datos ficticios de ventas
datos_ventas = {
    'Producto': ['Laptops', 'Smartphones', 'Tablets', 'Auriculares', 'Monitores'],
    'Ventas': [45000, 78000, 32000, 15000, 28000]
}

# Crear DataFrame
df = pd.DataFrame(datos_ventas)

# Mostrar los datos
st.subheader("Datos de Ventas")
st.dataframe(df)

# Crear gráfico de barras
st.subheader("Gráfico de Ventas por Producto")

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(df['Producto'], df['Ventas'], color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7'])

# Personalizar el gráfico
ax.set_xlabel('Productos')
ax.set_ylabel('Ventas ($)')
ax.set_title('Ventas por Producto')
plt.xticks(rotation=45)

# Agregar valores en las barras
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'${height:,.0f}',
            ha='center', va='bottom')

plt.tight_layout()
st.pyplot(fig)

# Información adicional
st.markdown("---")
st.info("💡 Esta es una aplicación de demostración con datos ficticios de ventas.")
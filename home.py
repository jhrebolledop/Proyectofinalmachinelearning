import streamlit as st



st.set_page_config(
    page_title="Identificación de pacientes diabéticos",
    page_icon="",
)

st.write("# Prioriza tu bienestar mediante la detección temprana de la diabetes 👋")

st.sidebar.success("Select a demo above.")
st.markdown(
    """
    ## Descripción de una base de datos sobre las variables predictoras para el diagnóstico de la diabetes.   🧢  

    Este conjunto de datos proviene originalmente del Instituto Nacional de Diabetes y Enfermedades Digestivas y Renales. El objetivo del conjunto de datos es predecir de manera diagnóstica si un paciente tiene o no diabetes, en función de ciertas medidas de diagnóstico incluidas en el conjunto de datos. Se impusieron varias restricciones a la selección de estas instancias de una base de datos más grande. En particular, todos los pacientes aquí son mujeres de al menos 21 años de herencia indígena:

    | Sigla       | Descripción |
    |-------      |-------------|
    |Pregnancies | Número de veces embarazada. |
    |Glucose     | Concentración de glucosa en plasma a las 2 horas en una prueba de tolerancia oral a la glucosa. |
    |BloodPressure| Presión arterial diastólica (mm Hg). |
    |SkinThickness| Grosor del pliegue cutáneo del tríceps (mm). |
    |Insulin      | Insulina sérica de 2 horas (mu U/ml). |
    |BMI          | Índice de masa corporal (peso en kg/(altura en m)^2). |
    |DiabetesPedig| Función de pedigrí de diabetes. |
    |Age          | Años de edad. |

    Los conjuntos de datos consisten en varias variables predictoras médicas y una variable objetivo, Outcome. Las variables predictoras incluyen el número de embarazos que ha tenido la paciente, su IMC, nivel de insulina, edad, etc.

    La base de datos permite realizar consultas, análisis y visualización de los datos, facilitando el diagnóstico oportuno de los pacientes diabéticos.
    
    

    """
)

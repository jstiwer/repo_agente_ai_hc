import streamlit as st
import requests

# API_URL = "https://api.langflow.astra.datastax.com/lf/741d247a-5163-49d3-9175-9450dff46b93/api/v1/run/0791cbe2-437c-4d5d-9df0-23cbad666ca0"  # Replace with your API URL

col1, col2 = st.columns([3,1])


with col1:
    st.markdown("")  # Espacio vacío para dejar la imagen sola en la fila

with col2:
    st.image("logo_hc.png", width=120)

# Ahora crea otra fila para centrar el texto debajo
st.markdown("<h1 style='text-align: center; margin-top: 20px;'>Agente Habicredit</h1>", unsafe_allow_html=True)


st.markdown("""
    <style>
    .stform_submit_button>button:hover {
        background-color: #7cdb91; /* Green */
        color: #7cdb91;
    }


/* New CSS for changing the shadow color of the text input when hovered */
.stTextInput>div>div>input:hover {
    box-shadow: 2px 2px 5px rgba(0,255,0,0.75); /* Green shadow when hovered */
}

    .stButton button:focus {
        border: 2px solid #7cdb91; /* Green border color when focused */
        color: #7cdb91; /* Green text color when focused */
    }

    /* CSS for changing the border color and shadow of the text input box */
    .stTextInput>div>div>input {
        border: 2px solid #7C01FF; /* Blue border color */
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Default shadow */
    }

    /* New CSS for changing the shadow color of the text input when hovered */
    .stTextInput>div>div>input:hover {
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Red shadow when hovered */
    }

    /* CSS for changing the border color and shadow of the text input box when focused */
    .stTextInput>div>div>input:focus {
        border: 2px solid #7C01FF; /* Red border color when focused */
        box-shadow: 2px 2px 5px rgba(124,1,255,1.000); /* Red shadow when focused */
    }
    </style>
    """, unsafe_allow_html=True)

def connect_api(query):
    BASE_API_URL = "https://api.langflow.astra.datastax.com"
    LANGFLOW_ID = "741d247a-5163-49d3-9175-9450dff46b93"
    FLOW_ID = "0791cbe2-437c-4d5d-9df0-23cbad666ca0" 
    APPLICATION_TOKEN  = "AstraCS:UByPvhxWgxaObuiRdHYkwNMl:cc45f1eeb9a640236415222c6d65eeef6937fca25f6276653ec8fdd9b324b16d"
    headers = {
        "Authorization": f"Bearer {APPLICATION_TOKEN}",
        "Content-Type": "application/json"
    }

    payload = {
        "input_value": query,
        "output_type": "chat",
        "input_type": "chat"
    }

    responses = requests.post(f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{FLOW_ID}", json=payload, headers=headers, timeout=90) 
    return responses
    
    
with st.expander("¿Cómo realizar una preguntar?"):
    st.markdown("""
    Para hacer una pregunta correcta al agente usa la siguiente estructura\nPara obtener la mejor respuesta sobre políticas y reglas de crédito, estructura tu pregunta indicando claramente la acción que deseas que realice nuestro Agente de Habicredit (ej. "explica", "enumera", "dime"), \nel tema específico (ej. "requisitos para radicar", "políticas de desembolso", "documentos necesarios") y cualquier condición o detalle adicional \n(ej. "para crédito hipotecario", "si ya tengo un crédito", "paso a paso"). \nSé lo más directo y específico posible para una respuesta precisa.
    \n\nPor último, mo olvides calificar la respuesta obtenida.
    """)
    
# Usa st.form para agrupar el input y botón
with st.form(key='chat_form'):
    query = st.text_input("Realiza las preguntas que hacen tus brokers:")
    submit_button = st.form_submit_button(label='Responder')

if submit_button and query:
    response_api = connect_api(query)
    
    if response_api.status_code != 200:
        st.write("⚠️ No 'response' key found in JSON.", response_api)
    else:
        data = response_api.json()
        data = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
        st.write(data)

if submit_button and query:
    response_api = connect_api(query)
    
if response_api.status_code != 200:
    st.write("⚠️ No 'response' key found in JSON.", response_api)
else:
    data = response_api.json()
    data = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    st.write(data)
    
    # Botones de Like y Dislike
    col_like, col_dislike = st.columns([1, 1])
    with col_like:
        if st.button("👍 Me gusta", key="like"):
            st.success("¡Gracias por tu feedback positivo!")
    with col_dislike:
        if st.button("👎 No me gusta", key="dislike"):
            st.warning("¡Gracias por tu feedback!")

import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

# Variables desde .env
twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_from = os.getenv("TWILIO_WHATSAPP_FROM")
whatsapp_to = os.getenv("WHATSAPP_TO")
gold_api_key = os.getenv("GOLD_API_KEY")

# Obtener precios desde GoldAPI
def obtener_precio_oro():
    url = "https://www.goldapi.io/api/XAU/USD"
    headers = {
        "x-access-token": gold_api_key,
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Error en la API:", response.text)
        return None, None

    data = response.json()
    precio_onza = data.get("price")
    precio_gramo_24k = data.get("price_gram_24k")
    return round(precio_gramo_24k, 2), round(precio_onza, 2)

# Enviar mensaje por WhatsApp
# Enviar mensaje por WhatsApp
def enviar_mensaje(precio_gramo, precio_onza):
    mensaje = f"💰 *Precio del Oro Actualizado*\n\n🟡 Gramo 24k: {precio_gramo} USD\n🟡 Onza Troy: {precio_onza} USD"
    client = Client(twilio_sid, twilio_token)

    destinatarios = whatsapp_to.split(",")  # <- esta línea debe ir dentro de la función

    for numero in destinatarios:
        client.messages.create(
            body=mensaje,
            from_=whatsapp_from,
            to=numero.strip()
        )
        print(f"✅ Mensaje enviado a {numero.strip()}")


# Ejecutar
if __name__ == "__main__":
    gramo, onza = obtener_precio_oro()
    if gramo and onza:
        enviar_mensaje(gramo, onza)

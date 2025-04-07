import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Cargar variables del archivo .env
load_dotenv()
print("🔍 GOLD_API_KEY =", repr(os.getenv("GOLD_API_KEY")))
print("📡 GOLD_API_URL =", repr(os.getenv("GOLD_API_URL")))


# Variables desde .env
twilio_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_token = os.getenv("TWILIO_AUTH_TOKEN")
whatsapp_from = os.getenv("TWILIO_PHONE_NUMBER")
whatsapp_to = os.getenv("TWILIO_TARGET_NUMBER")
gold_api_key = os.getenv("GOLD_API_KEY")
gold_api_url = os.getenv("GOLD_API_URL")

# Obtener precios desde GoldAPI
def obtener_precio_oro():
    url = gold_api_url
    headers = {
        "x-access-token": gold_api_key,
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("❌ Error en la API:", response.status_code, response.text)
            return None, None

        data = response.json()
        precio_onza = data.get("price")
        precio_gramo_24k = data.get("price_gram_24k")

        if precio_gramo_24k and precio_onza:
            return round(precio_gramo_24k, 2), round(precio_onza, 2)
        else:
            print("⚠️ La API respondió, pero faltan datos.")
            return None, None

    except requests.exceptions.Timeout:
        print("⏳ La API tardó demasiado en responder.")
        return None, None

    except requests.exceptions.RequestException as e:
        print("❌ Error al conectar con la API:", str(e))
        return None, None


    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print("❌ Error en la API:", response.status_code, response.text)
            return None, None

        data = response.json()
        precio_onza = data.get("price")
        precio_gramo_24k = data.get("price_gram_24k")

        if precio_gramo_24k and precio_onza:
            return round(precio_gramo_24k, 2), round(precio_onza, 2)
        else:
            print("⚠️ La API respondió, pero faltan datos.")
            return None, None

    except requests.exceptions.Timeout:
        print("⏳ La API tardó demasiado en responder.")
        return None, None

    except requests.exceptions.RequestException as e:
        print("❌ Error al conectar con la API:", str(e))
        return None, None

# Enviar mensaje por WhatsApp
def enviar_mensaje(precio_gramo, precio_onza):
    mensaje = f"💰 *Precio del Oro Actualizado*\n\n🟡 Gramo 24k: {precio_gramo} USD\n🟡 Onza Troy: {precio_onza} USD"
    client = Client(twilio_sid, twilio_token)

    destinatarios = whatsapp_to.split(",")

    for numero in destinatarios:
        try:
            client.messages.create(
                body=mensaje,
                from_=f"whatsapp:{whatsapp_from}",
                to=f"whatsapp:{numero.strip()}"
            )
            print(f"✅ WhatsApp enviado a {numero.strip()}")
        except Exception as e:
            print(f"❌ Error al enviar a {numero.strip()}: {e}")

# Ejecutar script
if __name__ == "__main__":
    gramo, onza = obtener_precio_oro()
    if gramo and onza:
        enviar_mensaje(gramo, onza)
    else:
        print("❌ No se pudo obtener el precio del oro.")

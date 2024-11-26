import requests

# Tu token de acceso de página
access_token = "EAAIV3OZAIVZBgBOwznR2jw0zI7QIO04y8R7rqZBlaJcu6DjtLWZB734X6b9t5ZAFSnL1Dj0l9ROiW1KGTqDRKnS9nK4KeUQF2XBVER2jSL2fpXNfAOHVLF7m3AkldXxJuAx67oCgDbuBIFowZC35sRjrneuHdxxXNMgbWOtJhrdEjAy31F0PXxn0RCiUafZA5yN1vxHdRS3KzpGBiyZCUfmCnKFK"

# ID de la página donde deseas publicar
page_id = "506237299237584"

# URL del endpoint para publicar
url = f"https://graph.facebook.com/v21.0/{page_id}/feed"

# Datos de la publicación
data = {
    "message": "Aqui se pone el mensaje de la publicacion: hola",
    "access_token": access_token
}

# Realizar la solicitud POST
response = requests.post(url, data=data)

# Manejo de la respuesta
if response.status_code == 200:
    print("¡Publicación realizada con éxito!")
    print(response.json())
else:
    print("Error al realizar la publicación.")
    print(response.json())

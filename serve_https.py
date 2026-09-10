"""
Servidor HTTPS simple para probar la PWA en la red local.

Uso:
  1) Generá el certificado una sola vez (necesita mkcert instalado):
       mkcert -install
       mkcert 192.168.x.x localhost
     (reemplazá 192.168.x.x por la IP real de tu notebook en la Wi-Fi)
     Esto crea dos archivos: 192.168.x.x+1.pem y 192.168.x.x+1-key.pem

  2) Editá CERT_FILE y KEY_FILE abajo con esos nombres exactos.

  3) Corré este script desde la carpeta que tiene index.html:
       python3 serve_https.py

  4) Desde el teléfono (conectado a la misma Wi-Fi), entrá a:
       https://192.168.x.x:4443
"""

import http.server
import ssl

HOST = "0.0.0.0"
PORT = 4443

CERT_FILE = "192.168.x.x+1.pem"        # <- cambiá esto por tu archivo generado
KEY_FILE = "192.168.x.x+1-key.pem"     # <- cambiá esto por tu archivo generado

httpd = http.server.HTTPServer((HOST, PORT), http.server.SimpleHTTPRequestHandler)

ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(certfile=CERT_FILE, keyfile=KEY_FILE)
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on https://{HOST}:{PORT} (usá tu IP de LAN desde el teléfono)")
httpd.serve_forever()

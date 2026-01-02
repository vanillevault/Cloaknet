# CloakNet Live Chat — NodoSpectre

CloakNet es un chat cifrado punto a punto, minimalista y experimental,
pensado **exclusivamente para redes locales o VPN privadas**.

No hay servidores centrales.
No hay logs persistentes.
No hay cloud.
Solo sockets, AES y TTL.

---

## 🛰️ Características

- 🔐 Cifrado AES (CFB) con clave derivada por SHA-256
- ⏳ Mensajes con TTL (caducan automáticamente)
- 🧵 Comunicación bidireccional con threads
- 🌐 Funciona en LAN o VPN (Tailscale, ZeroTier, WireGuard…)
- ⚙️ Sin dependencias pesadas
- 🧪 Proyecto educativo / experimental

---

## ⚠️ Advertencia

Este proyecto **NO está diseñado para Internet público**.
Úsalo únicamente en:

- Redes locales
- VPN privadas
- Entornos de laboratorio

No se garantiza anonimato, resistencia forense ni seguridad avanzada.

---

## 📦 Requisitos

- Python 3.9+
- pycryptodome

Instalación:

```bash
pip install -r requirements.txt


---

📂 Archivos

cloacknet.py        # Script principal
requirements.txt   # Dependencias
README.md
LICENSE


---

🚀 Uso

Iniciar como servidor

python3 cloacknet.py

Selecciona opción 1
Define alias y TTL
Espera conexión

Conectarse como cliente

python3 cloacknet.py

Selecciona opción 2
Introduce IP o hostname del servidor


---

🧠 Concepto

CloakNet nace como una prueba de canal efímero: los mensajes existen solo durante un tiempo definido y después mueren.

No se guarda historial. No se puede recuperar el pasado.


---

🧪 Estado del proyecto

Experimental

Sin auditoría

En evolución


Pull requests y forks permitidos bajo la misma filosofía.


---

🧾 Licencia

MIT License — uso libre bajo tu responsabilidad.

---

## 📦 requirements.txt

```txt
pycryptodome

> ⚠️ IMPORTANTE
NO uses Crypto (está roto/obsoleto).
El módulo correcto es pycryptodome, que expone Crypto.*.



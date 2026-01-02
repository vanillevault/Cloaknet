import socket
import threading
import time
import base64
import hashlib

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


# === CONFIGURACIÓN AES ===
KEY = hashlib.sha256(b'spectre_channel').digest()


def encrypt_msg(msg, ttl):
    iv = get_random_bytes(16)
    data = str({
        "msg": msg,
        "exp": int(time.time()) + ttl
    }).encode()

    cipher = AES.new(KEY, AES.MODE_CFB, iv)
    ct = cipher.encrypt(data)

    return base64.b64encode(iv + ct)


def decrypt_msg(token):
    try:
        raw = base64.b64decode(token)
        iv, ct = raw[:16], raw[16:]

        cipher = AES.new(KEY, AES.MODE_CFB, iv)
        data = eval(cipher.decrypt(ct).decode())

        if time.time() > data["exp"]:
            return "[💀 Expirado]"

        return data["msg"]
    except Exception:
        return "[❌ Error de descifrado]"


# === CHAT ===
def handle_recv(conn, alias):
    while True:
        try:
            data = conn.recv(2048)
            if not data:
                break
            print(f"\n📨 {alias} >> {decrypt_msg(data)}\n> ", end="", flush=True)
        except:
            break


def start_server(host="0.0.0.0", port=9999):
    alias = input("👤 Tu alias (servidor): ")
    ttl = int(input("⏳ TTL en segundos: "))

    s = socket.socket()
    s.bind((host, port))
    s.listen(1)

    print(f"🛰️ Esperando conexión en {host}:{port} ...")
    conn, addr = s.accept()
    print(f"🔗 Conectado con {addr[0]}")

    threading.Thread(
        target=handle_recv,
        args=(conn, "Cliente"),
        daemon=True
    ).start()

    while True:
        msg = input("> ")
        conn.send(encrypt_msg(msg, ttl))


def start_client(host, port=9999):
    alias = input("👤 Tu alias (cliente): ")
    ttl = int(input("⏳ TTL en segundos: "))

    s = socket.socket()
    s.connect((host, port))

    print(f"🛰️ Conectado con {host}:{port}")

    threading.Thread(
        target=handle_recv,
        args=(s, "Servidor"),
        daemon=True
    ).start()

    while True:
        msg = input("> ")
        s.send(encrypt_msg(msg, ttl))


# === MAIN ===
def main():
    print("🛰️ CloakNet Live Chat — NodeSpectre v1.0\n")
    print("1. Iniciar como servidor")
    print("2. Conectarse como cliente")
    print("0. Salir")

    opt = input("\nSelecciona modo: ")

    if opt == "1":
        start_server()
    elif opt == "2":
        host = input("🌐 IP/Hostname del servidor: ")
        start_client(host)
    else:
        print("👋 Saliste del chat.")


if __name__ == "__main__":
    main()

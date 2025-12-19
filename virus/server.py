import socket, json, time

IP_ADDRESS = '127.0.0.1' ## Local Server (Can be replaced with your Private IP)
PORT = 5678
print("[+] Starting server...")
with socket.socket() as s:
    s.bind((IP_ADDRESS, PORT))
    s.listen(1)
    print(f"[+] Listening on {IP_ADDRESS}:{PORT}")
    conn, addr = s.accept()
    print(f"[+] Connection from {addr}")
    data = b''.join(iter(lambda: conn.recv(4096), b''))
    conn.close()
    try:
        payload = json.loads(data.decode())
        hostname = payload.get('hostname', 'unknown')
        filename = f"{hostname}_{int(time.time())}_payload.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent=4)
        print(f"[+] Payload saved as {filename}")
    except Exception as e:
        print("[!] Failed to process payload:", e)
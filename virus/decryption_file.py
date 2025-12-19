from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os, platform, getpass, shutil, socket, ssl, json, base64, uuid, time

def decrypt_message(encrypted_data, key):
    nonce = encrypted_data[:12]
    ciphertext = encrypted_data[12:]
    
    aesgcm = AESGCM(key)
    
    return aesgcm.decrypt(nonce, ciphertext, None)

def decrypting_file(path, key):
    with open(path, "rb") as f:
        encrypted_file = f.read()

    decrypted_file = decrypt_message(encrypted_file, key)
    print(decrypted_file)

    with open(path, "wb") as f:
        f.write(decrypted_file)

def decrypt_folder(folder_path, b64_key):
    key = base64.b64decode(b64_key)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            decrypting_file(file_path, key)

def main():
    folder_path = input("Enter the folder path to decrypt: ").strip()
    b64_key = input("Enter the base64-encoded decryption key: ").strip()
    if folder_path == "":
        folder_path = "/Users/kacperwrobel/Documents/cyber_tools/virus/victim"
    decrypt_folder(folder_path, b64_key)
    print("Decryption completed.")

if __name__ == "__main__":
    main()
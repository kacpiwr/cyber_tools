import hashlib

def inputPassword():
    print("Enter your password:")
    password_to_guess = input().strip()
    return hashlib.sha256(password_to_guess.encode('utf-8')).hexdigest()

def findPassword(file,password_to_guess_hash):
    guessed_passwords = []
    for current_password in file.readlines():
        cleaned_password = current_password.strip() 
        current_password_hash = hashlib.sha256(cleaned_password.encode('utf-8')).hexdigest()   
        if(current_password_hash == password_to_guess_hash):
            guessed_passwords.append(current_password)
    return guessed_passwords

def main():
    password_to_guess = ""
    guessed_passwords = []
    password_to_guess_hash = inputPassword()
    file_with_passwords = open('/Users/kacperwrobel/Documents/cyber_tools/password_files/passlist.txt', 'r', encoding='latin-1')

    print("=============================\nDecrypting password ")

    guessed_passwords = findPassword(file_with_passwords, password_to_guess_hash)
    if guessed_passwords == []:
        file_with_passwords = open('/Users/kacperwrobel/Documents/cyber_tools/password_files/100k_passwords.txt', 'r', encoding='latin-1')
        guessed_passwords = findPassword(file_with_passwords, password_to_guess_hash)
    
    print("=============================\nFinished decrypting passwords \n=============================\n")

    if(guessed_passwords == []):
        print("No passwords found")
    else:
        print("Here are your passwords in quantity "+ str(len(guessed_passwords)) +" :")
        for password in guessed_passwords:
            print(password)

if __name__ == "__main__":
    main()
    

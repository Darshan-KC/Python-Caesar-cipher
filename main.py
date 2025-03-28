# main.py
from caeser import Caeser

def main():
    # try:
        caeser = Caeser(9) # you can use shift value from user also
        choice = int(input("Choose mode: \n1. Encrypt \n2. Decrypt\n: "))
        if choice == 1:
            message = input("Enter the message to encrypt: ")
            result = caeser.encrypt(message)
            print(f"Encryption of '{message}' is '{result}'")
            
        elif choice == 2:
            message = input("Enter the encypted message to decrypt: ")
            result = caeser.decrypt(message)
            print(f"Decryption of '{message}' is '{result}'")
        else:
            print("Invalid choice")
        
    # except:
    #     print("Exception occurs")

if __name__ == "__main__":
    main()
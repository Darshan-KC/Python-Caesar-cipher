class Caeser:
    def __init__(self, shift) -> None:
        self.shift = shift
        
    def encrypt(self,message) ->str:
        shift = self.shift % 26
        result = ''
        for char in message:
            if 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            elif 'a' <= char <='z':
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += char
        return result
    
    def decrypt(self,message) -> str:
        shift = self.shift % 26
        result = ''
        for char in message:
            if 'A' <= char <= 'Z':
                result += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif 'a' <= char <= 'z':
                result += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                result += char
        return result

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
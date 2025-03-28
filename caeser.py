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
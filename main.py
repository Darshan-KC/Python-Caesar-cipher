class Caeser:
    def __init__(self, shift) -> None:
        self.shift = shift
        
    def encrypt() ->str:
        pass
    
    def decrypt() -> str:
        pass

def main():
    try:
        caeser = Caeser(9) # you can use shift value from user also
        choice = int(input("Choose mode: 1. Encrypt 2. Decrypt"))
        if choice == 1:
            pass
        elif choice == 2:
            pass
        else:
            print("Invalid choice")
    except:
        print("Exception occurs")

if __name__ == "__main__":
    main()
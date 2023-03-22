
def menu(): #menu function
    print("\nMenu\n------------\n1. Encode\n2. Decode\n3. Quit\n")

def encode(password): #pass encoder
    encoded = ""
    for i in password:
        encoded = encoded + str((int(i) + 3) % 10) #shifts number and makes sure each number stays single diget
    return encoded

def decode(password): #pass decoder
    decoded = ""
    for i in password:
        decoded = decoded + str((int(i) - 3) % 10) #shifts number and makes sure each number stays single diget
    return decoded

def main():
    decoder = True
    while decoder:
        menu()
        option = int(input("Please enter an option: ")) #makes it integer so if statement can run
        if option == 1:
            user_password = input("Please enter your password to encode: ")
            encoded_password = encode(user_password)
            print("Your password has been encoded and stored!")
        elif option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
        elif option == 3:
            decoder = False
            break


if __name__ == '__main__':
    main()

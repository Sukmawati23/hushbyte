from encoder import encode_message
from decoder import decode_message


def show_banner():
    print()
    print("╔══════════════════════════════╗")
    print("║          HUSHBYTE            ║")
    print("║       Keep it lowkey!        ║")
    print("╚══════════════════════════════╝")
    print()


def encode_menu():
    print("\n ENCODE MESSAGE ")
    message = input("Enter your secret message: ")

    if not message.strip():
        print("Message cannot be empty!")
        return

    encoded = encode_message(message)

    print("\nEncoded message:")
    print(encoded)


def decode_menu():
    print("\n DECODE MESSAGE ")
    encoded_message = input("Enter your encoded message: ")

    if not encoded_message.strip():
        print("Encoded message cannot be empty!")
        return

    try:
        decoded = decode_message(encoded_message)

        print("\nDecoded message:")
        print(decoded)

    except Exception:
        print("\nInvalid encoded message.")


def main():
    while True:
        show_banner()

        print("[1] Encode Message")
        print("[2] Decode Message")
        print("[3] Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            encode_menu()

        elif choice == "2":
            decode_menu()

        elif choice == "3":
            print("\nHushbyte says: stay lowkey!")
            break

        else:
            print("\nInvalid choice. Please choose 1, 2, or 3.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
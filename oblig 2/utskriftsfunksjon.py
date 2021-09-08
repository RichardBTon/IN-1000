def samtalestart():
    navn = input("Skriv inn navn: ")
    sted = input("Hvor kommer du fra? ")
    print(f"Hei, {navn}! Du er fra {sted}.")
    print()


def main():
    for i in range(3):
        samtalestart()


if __name__ == "__main__":
    main()

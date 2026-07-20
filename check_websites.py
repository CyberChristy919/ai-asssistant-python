import requests

def check_website(address):
    address = address.strip()

    if not address:
        return

    if not address.startswith("http://") and not address.startswith("https://"):
        address = "https://" + address

    try:
        response = requests.get(address, timeout=5)

        if response.status_code == 200:
            print(f"{address} up")
        else:
            print(f"{address} down")

    except requests.exceptions.RequestException:
        print(f"{address} down")


def main():
    try:
        with open("addresses.txt", "r") as file:
            for line in file:
                check_website(line)
    except FileNotFoundError:
        print("The file addresses.txt was not found.")


if __name__ == "__main__":
    main()

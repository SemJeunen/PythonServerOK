import sys, servers

while True:
    print("\nKies een actie:")
    print("1. Voeg een server toe")
    print("2. Verwijder een server")
    print("3. Toon servers")
    print("4. Stop de toepassing")
    keuze = input("Voer het nummer van de gewenste actie in: ")
    
    if keuze == "1":
        servers.voeg_server_toe(input("geef het domein of het ip adres van de server: "))
    elif keuze == "2":
        servers.verwijder_server(input("geef het domein of het ip adres van de server die je wil verwijderen: "))
    elif keuze == "3":
        servers.toon_servers()
    elif keuze == "4":
        print("Toepassing gestopt.")
        break
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
import json

def voeg_server_toe(server):
    servers = load_file()

    servers.append(server)

    write_file(server)


def verwijder_server(server):
    servers = load_file()
    if server in servers:
        servers.remove(server)
        print(f"{server} is verwijderd")
    else:
        print(f"{server} is niet gevonden in de lijst")

# Functie om de lijst met servers weer te geven
def toon_servers():
    servers = load_file()
    for server in servers:
        print(server)


def load_file():
     with open("servers.json", "r") as f:
        return json.load(f)
     
def write_file(servers):
    with open("servers.json", "w") as f:
        json.dumps(servers, f)
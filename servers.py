import json

def voeg_server_toe(server):
    servers_list = load_file()

    server_waarde ={
        "domein": server
    }

    servers_list.append(server_waarde)

    write_file(servers_list)


def verwijder_server(server):
    servers = load_file()
    for domain in servers:
        if domain["domein"] == server:
            servers.remove(domain)
            print(f"{server} is verwijderd")
    write_file(servers)

# Functie om de lijst met servers weer te geven
def toon_servers():
    servers = load_file()
    for server in servers:
        print(server["domein"])


def load_file():
     with open("servers.json", "r") as f:
        return json.load(f)
     
def write_file(servers):
    with open("servers.json", "w") as f:
        json.dump(servers, f)
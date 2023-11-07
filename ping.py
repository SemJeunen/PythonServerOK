import os, json
def is_server_online(server):
    response = os.system(f"ping {server}")
    return response == 0

def report(server):
    servers = []
    with open("servers_status.json", "r") as f:
        servers = json.load(f)

    data = {
        "domain": server,
        "online": is_server_online(server)
    }

    servers.append(data)

    with open("servers_status.json", "w") as f:
        json.dump(servers, f)
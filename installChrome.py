from fabric import Connection
from fabric import ThreadingGroup

nodes = [
    "pi@192.168.137.106",
    "pi@192.168.137.105",
    "pi@192.168.137.103",
    "pi@192.168.137.104"
]

user = "pi"

nodeConnections = [Connection(node, connect_kwargs = {"password":"raspberry"}) for node in nodes]
node = ThreadingGroup.from_connections(nodeConnections)
node.run("hostname")
node.run("sudo apt update")
node.run("sudo apt install -y chromium-chromedriver")
print("done")
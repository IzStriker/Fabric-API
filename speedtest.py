from fabric import Connection
from fabric import ThreadingGroup

nodes = [
    "pi@192.168.0.81",
    "pi@192.168.0.82",
    "pi@192.168.0.83",
    "pi@192.168.0.84"
]

user = "pi"

nodeConnections = [Connection(node, connect_kwargs = {"password":"raspberry"}) for node in nodes]
node = ThreadingGroup.from_connections(nodeConnections)
node.run("sudo apt update", hide=True)
node.run("sudo apt install python3-pip -y", hide=True)
node.run("sudo pip3 install speedtest-cli", hide=False)

for node in nodeConnections:
    print("=======================================")
    node.run("hostname")
    print("=======================================")
    node.run("speedtest-cli")
    print("=======================================")
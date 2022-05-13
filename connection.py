from fabric import Connection

node1 = Connection("pi@192.168.137.106", connect_kwargs = {"password":"raspberry"})
node1.run("uname -s")
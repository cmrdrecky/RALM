# RALM
Checking host's opened ports for remote administration software like RAdmin and LiteManager and connecting in full control mode.
Works only on OS Windows.
You'll need installed clients of LiteManager/RAdmin in succed to connect to host.
# Explanation
These both softwares having the limited adress-book of ~15 hosts, so if you need to connect the new one, youll have to delete some of previous hosts.
But if you're connecting through command line - this rule doesnt accure.
# How to use
By default it's IPv4 subnet (192.168.1.* ) - you can change it in code.
Type last octet of host's adress and script will check his status online and try to connect through default RAdmin and LM opened sockets. 

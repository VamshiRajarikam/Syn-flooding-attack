# Syn-flooding-attack
Syn flooding (DoS) attack in which client/attacker repeatedly send SYN (synchronization) packets to a server/target’s system in an attempt to consume enough server resources to make the system unresponsive to other client’s/users.

TCP three-way handshake, series of steps are:

1.	Client/user sends a SYN (synchronize) message to the server/machine.

2.	Server/machine acknowledges the request and sends SYN-ACK to the client.

3.	Client will respond with an ACK and the connection is established.

A SYN flood attack works by not responding the server/machine with ACK. If server does not get the respond from the client/user, it will send the SYN-ACK again. 

Languages: Python
IDE:Sublime text
Libraries: Scapy

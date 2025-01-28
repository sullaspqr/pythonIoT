# SR-201:
# ip 192.168.1.100
# port 6722 TCP VAGY 6723 UDP
ch1 on 11-> 10000000 válasz
ch1 off 21 -> 00000000 válasz
ch2 on 12 -> 01000000 válasz
ch2 off 22 -> 00000000 válasz

Ha mindkét relé felkapcsolva akkor:
-> válasz 11000000

állapotok vannak, a 1. bit jelenti a ch1-es port 0-nál a zárt állapotát, 1-nél azt ha nyitott
a 2.bitnél a ch2 port nyitottságát vagy zártságát jelzi

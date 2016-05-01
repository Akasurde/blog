Title: Netem
Date: 2016-05-01 12:03
Modified: 2016-05-01 12:03
Category: netem
Tags: linux, command line, networking, netem
Slug: netem-command
Authors: Abhijeet Kasurde
Summary: Netem command examples

Netem provides Network Emulation functionality for testing protocols by emulating the properties of wide area networks.


* Adding fixed amount of delay to packets going out of the Ethernet

    <pre>$ tc qdisc add dev eth0 root netem delay 100ms</pre>

* Adding random amount of variation in delay to packets going out of the Ethernet

    <pre>$ tc qdisc add dev eth0 root netem delay 100ms 10ms</pre>

* Adding random amount of variation in delay with correlation to packets going out of the Ethernet

    <pre>$ tc qdisc add dev eth0 root netem delay 100ms 10ms 25%</pre>

    This causes the added delay to be 100ms ± 10ms with the next random element depending 25% on the last one.

* Specify non-uniform distribution in delay

    <pre>$ tc qdisc add dev eth0 root netem delay 100ms 20ms distribution normal</pre>

    distribution value : (normal, pareto, paretonormal)


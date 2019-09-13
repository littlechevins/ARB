# About

Thesis for energy trading in blockchain using Secure Private Blockchain paper, focusing specifically on the routing protocol between two trading nodes.


# Technical

A standard internet routing protocol (OSPF) is used for broadcasting and general routing of communication between nodes. We build a **backbone** system for better propagation of messages while maintaining a relatively light network load.

- Dijkstra's is used in the calculation of shortest path to any given node on the map
- Since end nodes are an 1 way street extension of backbone nodes, we only use backbone nodes for the OSPF calculation. 

A DHT is used to map public addresses to IP addresses. This DHT is expandable and uses a **routing byte** index to lessen the load by auto balancing the DHT when it deems necessary 

# Framework
Built on the Python Flask framework for fast reliable network functionality.

## How to

The current scripts are built on a **macOS** system using the Appla OSA script. This script allows the user to spawn multiple nodes (backbone/end + custom ip)

1. Run using 'osascript start_scpt.scpt'
2. This should spawn a secondary window where the nodes are initialized. 
3. Using **Postman** or any other service, inject to the desired node IP

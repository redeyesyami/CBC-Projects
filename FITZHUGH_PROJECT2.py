#! /usr/bin/python3

'''
!!!!
NOTE THE FORMATTING OF THE HEADER AND THE OUTPUTS FROM EACH PROBLEM!!!
!!!!
'''

'''
Kia Fitzhugh
CSIA 450
Spring 2020
Project 2
'''

# LIBRARIES HERE
# import socket
# import scipt

#1. 
# Calculate the number of potential connections 
# and the network density in a fixed-size network of 800 nodes 
# with 2000 actual connections.

# total nodes in the network
n = 800
# actual connections
actual_connections = 2000
# the formula for potential connections
potential_connections = int((n*(n-1))/2)
# the formula for network density
network_density = (actual_connections/potential_connections)
# print the results
print("#1.")
print("Potential Connections:", potential_connections)
print("Network Density:", round(network_density,2))
print(" ")

#2.	
# Create an updated SNMP Community String starting 
# with "public_" and adding a location of "CBC_WIRELESS".

# this is the default SNMP Community String
snmp_community_string = "public_"
# update it to include the organization location
location = "CBC_WIRELESS"\
# concatenate strings
snmp_community_string += location
# print the results
print("#2.")
print("Updated SNMP Community String:", snmp_community_string)
print(" ")

#3. 
# Print the LENGTH of this updated SNMP Community String.
# print the results
print("#3.")
print("Length:", len(snmp_community_string))
print(" ")

#4. 
# Create a list of OSI model layers and return the 
# "Presentation" layer by indexing the list.
# create a OSI list
OSI_Model = ["Physical", "DataLink", "Network", "Transport", 
             "Session", "Presentation", "Application"]
# print the results
print("#4.")
# print the "Presentation" layer
print("Layer *6* in the OSI Model:", OSI_Model[5])
print(" ")

#5. 
# Create two set data structures, one for the OSI model and 
# one for the TCP/IP model
# create two sets for OSI and TCP/IP models
set1_OSI = {"Physical", "DataLink", "Network", "Transport", 
             "Session", "Presentation", "Application"}
set2_TCP_IP = {"Network Access", "Internet", "Transport", "Application"}
# print the results
print("#5.")
# print sets
print("OSI Model layers:", set1_OSI)
print("TCP/IP Model layers:", set2_TCP_IP)
print(" ")

#6. 
# Print the intersection set of the OSI and TCP/IP sets.
# print the results
print("#6.")
# find the intersection
intersection_layers = set1_OSI & set2_TCP_IP
#print the results
print("Intersection Layers:", intersection_layers)
print(" ")

#7. 
# Create a function that returns a random IPv4 octet.
# This is just the random library for Python.  Use this!
from random import randint
# This is the function
def getRandom():
    min_random_value = 0
    max_random_value = 255
    return randint(min_random_value, max_random_value)
# This gets the value
random_value = getRandom()
# print the results
print("#7.")
print("Random IPv4 octet:", random_value)
print(" ")

#8. 
# Create a dictionary object that contains the following 
# protocols and ports:Telnet:23, SMTP:25, HTTP:80, 
# HTTPS:443, where the protocol is the key.
# Create the dictionary.
ports_dictionary = {"Telnet":23, "SMTP":25, "HTTP":80,
                    "HTTPS":443}
print("#8.")
# print the results
print("Ports Dictionary:", ports_dictionary)
print(" ")

#9. 
# List your localhost's IPv4 IP address, version, 
# and is_private flag.
ip_str = '192.168.1.19'
# use the ipaddress module
import ipaddress
my_ip = ipaddress.ip_address(ip_str)
# print some results
print("#9.")
print('IP address:', my_ip)
print('IP version:', my_ip.version)
print('IP address is private:', my_ip.is_private)
print(" ")


#10. 
# List the following about your network.
# A.	Network is private?
# B.	Network is broadcast?
# C.	Network is compressed?
# D.	Network with netmask?
# E.	Network with hostmask?
# F.	Network address count?
network_str = '192.168.1.0/24'
# use the ipaddress module
import ipaddress
my_net = ipaddress.ip_network(network_str)
# print the results
print("#10.")
print('Network is private:', my_net.is_private)
print('Network is broadcast:', my_net.broadcast_address)
print('Network is compressed:', my_net.compressed)
print('Network with netmask:', my_net.with_netmask)
print('Network with hostmask:', my_net.with_hostmask)
print('Network address count:', my_net.num_addresses)
print(" ")

#11. 
# The network_IPv4.py file has some sample iteration code
#  for listing all the "usable" hosts.  Why is "usable" in quotes?
# print the results
print("#11.")
print("Usable is in quotes because the network address (ending in .0) " 
   "and broadcast address (ending in .255) are not usable as host addresses.")
print(" ")

#12. 
#
# print the results
print("#12.")
print("?????")
print(" ")

#13. 
# Why is port 8500 used and not port 80?
# print the results
print("#13.")
print("Port 8500 is used and not port 80 because port 80 is for HTTP"
   " while port 8500 is for TCP, which is needed to transmit messages.")
print(" ")

#14. 
# Use the 'math' module to calculate the number of bits needed to 
# represent the following number: 128.
import math
# 1 MB?
my_number = 128

# print the results
print("#14.")
# This is one way.
print("Generic:", math.log(my_number, 2))
# This is more accurate.
print("Binary Log:", math.log2(my_number))
print(" ")

#15. 
# Use the 'random' module to select a random set of 10 PRIVATE Class A IPv4 addresses.
import random
# Use the 'random' module to select a random set of 10 PRIVATE Class A IPv4 addresses.
classA = '10.0.0.'
IPs = random.sample(range(255), 10)
# print the results
print("#15.")
print("Hosts:")
for IP in IPs:
    print(classA+str(IP))

print(" ")
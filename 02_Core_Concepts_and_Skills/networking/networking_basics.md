# Networking Basics

## Introduction

Networking is the communication of devices and systems over a network.
Cybersecurity professionals need networking knowledge to understand
communication, identify suspicious traffic, and investigate security
incidents.

## IP Address

An IP address identifies a device or network interface for communication
using the Internet Protocol.

### IPv4

An IPv4 address consists of four decimal numbers separated by dots.

Example:

192.168.1.25

### Private IPv4 Address Ranges

The commonly used private IPv4 ranges are:

- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

Example:

192.168.1.25 is a private IPv4 address.

## Port

A network port helps identify a particular service or application
endpoint on a host.

### Common Ports

| Port | Service/Protocol |
|---|---|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 25 | SMTP |
| 3389 | RDP |

Example:

192.168.1.25:443

This represents communication with the host on port 443, which is
commonly associated with HTTPS.

## Network Protocol

A network protocol is a defined set of rules used for communication
between systems.

Examples:

- TCP
- UDP
- HTTP
- HTTPS
- DNS
- SSH

## TCP and UDP

### TCP

TCP is connection-oriented and provides reliable and ordered delivery
of data.

### UDP

UDP is connectionless and generally has lower protocol overhead.
It does not provide TCP's built-in reliable and ordered delivery.

## DNS

DNS stands for Domain Name System.

DNS primarily translates domain names into IP addresses.

Example:

google.com
    ↓
   DNS
    ↓
IP address

## HTTP and HTTPS

HTTP is used for web communication.

HTTPS is HTTP protected using TLS.

Common ports:

- HTTP: 80
- HTTPS: 443

HTTPS protects data in transit, but HTTPS alone does not guarantee that
a website itself is trustworthy.

## Learning Outcome

I learned the basic concepts of IP addresses, private IPv4 ranges,
network ports, protocols, TCP, UDP, DNS, HTTP, and HTTPS.
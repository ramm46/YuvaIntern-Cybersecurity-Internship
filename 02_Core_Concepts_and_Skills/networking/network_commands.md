# Network Commands

## Introduction

Network commands are useful for checking network configuration,
testing network connectivity, resolving domain names, and examining
network paths.

These commands are useful for basic network troubleshooting and
cybersecurity analysis.

---

## 1. ipconfig

### Command

```powershell
ipconfig
```

### Purpose

The `ipconfig` command displays the basic network configuration of a
Windows computer.

### Common Information

- IPv4 address
- IPv6 address
- Default gateway
- Network adapter information

### Practical

I executed the `ipconfig` command on my Windows computer and observed
the network configuration.

### Security Relevance

`ipconfig` can help a security professional understand the basic
network configuration of a system during troubleshooting or analysis.

---

## 2. ipconfig /all

### Command

```powershell
ipconfig /all
```

### Purpose

The `ipconfig /all` command displays detailed network configuration
information.

### Common Information

- IPv4 address
- IPv6 address
- Physical/MAC address
- DHCP information
- DNS servers
- Default gateway
- Network adapter details

### Practical

I executed the `ipconfig /all` command to view detailed network
configuration information.

### Security Note

The output may contain sensitive network information such as MAC
addresses and DNS server details. This information should not be
shared publicly without appropriate redaction.

---

## 3. ping

### Command

```powershell
ping 8.8.8.8
```

### Purpose

The `ping` command is used to test basic network connectivity to a
destination using ICMP echo requests.

### Practical

I executed the following command:

```powershell
ping 8.8.8.8
```

The command returned responses from the destination.

### Important Information

The response may include:

- Bytes
- Response time
- TTL

A response indicates that the destination responded to the ICMP
request.

### Security Relevance

Ping can be useful for basic network troubleshooting and connectivity
testing.

A failed ping does not always mean that the destination is offline.
ICMP traffic may be blocked or filtered by a firewall or network
configuration.

---

## 4. nslookup

### Command

```powershell
nslookup google.com
```

### Purpose

The `nslookup` command is used to query DNS information and resolve a
domain name.

### Practical

I executed the following command:

```powershell
nslookup google.com
```

The command returned DNS resolution information for the domain.

### Security Relevance

DNS lookup can be useful for:

- Troubleshooting DNS problems
- Checking domain resolution
- Basic domain investigation
- Understanding which IP address a domain resolves to

---

## 5. tracert

### Command

```powershell
tracert google.com
```

### Purpose

The `tracert` command displays the network path and intermediate hops
between the local computer and the destination.

### Practical

I executed the following command:

```powershell
tracert google.com
```

The command displayed the network hops towards the destination.

### Security Relevance

Traceroute can help with:

- Network troubleshooting
- Understanding network paths
- Identifying possible connectivity problems
- Basic network investigation

Some hops may display `*`. This can happen when a network device does
not respond to the traceroute probe or filters the relevant traffic.

---

# Network Command Summary

| Command | Purpose |
|---|---|
| `ipconfig` | View basic network configuration |
| `ipconfig /all` | View detailed network configuration |
| `ping` | Test basic network connectivity |
| `nslookup` | Perform DNS resolution |
| `tracert` | View network path and intermediate hops |

---

# Practical Exercises Completed

The following Windows networking commands were practised:

1. `ipconfig`
2. `ipconfig /all`
3. `ping 8.8.8.8`
4. `nslookup google.com`
5. `tracert google.com`

These practical exercises provided experience with:

- Network configuration
- Connectivity testing
- DNS resolution
- Network path analysis
- Basic network troubleshooting

---

# Cybersecurity Relevance

Network commands are useful for cybersecurity professionals because
they provide basic visibility into network configuration and
communication.

During troubleshooting or security investigation:

- `ipconfig` can help identify the local system's network settings.
- `ipconfig /all` can provide detailed adapter and DNS information.
- `ping` can help test basic connectivity.
- `nslookup` can help investigate DNS resolution.
- `tracert` can help understand the network path to a destination.

These commands are useful starting points for network troubleshooting
and basic security analysis.

---

# Learning Outcome

Through this practical exercise, I learned how to use common Windows
network commands and understood their purpose in networking and
cybersecurity.

I gained practical experience with network configuration inspection,
connectivity testing, DNS resolution, and network path analysis.

I also learned that network command output can contain sensitive
information and should be handled carefully when sharing or
documenting results.
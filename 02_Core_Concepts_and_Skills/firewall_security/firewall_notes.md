
# Firewall Security

## 1. Introduction

A firewall monitors network traffic and applies security rules to allow or block connections. It helps protect computers and networks from unauthorized network access.

## 2. Types of Firewalls

### Hardware Firewall
A physical security device that filters traffic between networks.

### Software Firewall
A firewall application or operating-system feature that protects an individual computer.

Example: Windows Defender Firewall.

### Next-Generation Firewall (NGFW)
A firewall that may provide advanced capabilities such as application awareness and intrusion prevention.

## 3. Important Firewall Concepts

- Inbound traffic: Traffic entering a computer or network.
- Outbound traffic: Traffic leaving a computer or network.
- Allow rule: Permits traffic when the rule conditions match.
- Block rule: Blocks traffic when the rule conditions match.
- Firewall profile: A set of rules associated with a network profile, such as Domain, Private, or Public.
- Default action: The action applied to traffic that does not match a more specific applicable rule, subject to the effective firewall policy.

## 4. Practical 1: Check Firewall Profiles

### Command

```powershell
Get-NetFirewallProfile |
Select-Object Name, Enabled, DefaultInboundAction, DefaultOutboundAction
```

### Observed Results

| Profile | Enabled |
|---|---|
| Domain | True |
| Private | True |
| Public | True |

Observation: All three reported firewall profiles were enabled.

The default inbound and outbound actions displayed `NotConfigured`. This does not, by itself, establish the effective traffic-handling behavior.

## 5. Practical 2: Inspect Enabled Firewall Rules

### Command

```powershell
Get-NetFirewallRule -Enabled True |
Select-Object -First 10 DisplayName, Direction, Action, Profile
```

### Observations

- The command displayed the first 10 enabled firewall rules.
- The output included inbound and outbound rules.
- The displayed rules included Allow actions.
- Rules were associated with Public, Private, Domain, and Any profiles.

These results describe the displayed rules only; they do not establish the behavior of every firewall rule or connection.

## 6. Cybersecurity Best Practices

- Keep the firewall enabled.
- Allow only necessary network traffic.
- Review firewall rules periodically.
- Avoid exposing unnecessary services to public networks.
- Do not disable security protections without authorization.
- Test firewall changes carefully and maintain a recovery plan.

## 7. Learning Outcome

I learned the purpose of firewalls, the difference between inbound and outbound traffic, and how to inspect Windows Firewall profiles and enabled rules using PowerShell.

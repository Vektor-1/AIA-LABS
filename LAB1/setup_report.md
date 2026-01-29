# Environment Setup Report for LAB 1

## Overview

This report details the setup of the Python agent development environment using SPADE and ejabberd XMPP server for LAB 1.

## Components Installed

- **Python**: Version 3.10.13 installed, meeting the 3.9+ requirement.
- **SPADE**: Installed in a virtual environment via pip.
- **XMPP Server**: ejabberd installed via Homebrew, configured with localhost as the domain.
- **Prometheus**: Installed for monitoring purposes.

## Configuration Steps

1. Created Python virtual environment in `/Users/admin/Projects/Class/AIA/AIA-LABS/venv`.
2. Activated the environment and installed SPADE.
3. Installed ejabberd XMPP server.
4. Started ejabberd server.
5. Registered agent user 'agent1@localhost' with password 'password'.

## Verification

- Python and SPADE verified by importing in the environment.
- XMPP server running and accepting connections on port 5222.
- Basic agent implemented and executed successfully.

## Challenges

- ejabberd service start failed initially due to permissions; resolved by running manually.
- PDT (Prometheus Design Tool) assumed to be Prometheus; if different, needs clarification.

## Conclusion

The environment is ready for agent development. The basic agent runs without errors, indicating successful setup.

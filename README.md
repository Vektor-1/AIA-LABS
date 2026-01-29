# AI Agent Environment Setup

This folder is set up for developing AI agents using SPADE (Smart Python Agent Development Environment).

## Installed Components

- **Python 3.10.13**: Version 3.10.13 is installed and meets the requirement of Python 3.9 or higher.
- **SPADE**: Installed via pip in the virtual environment.
- **ejabberd XMPP Server**: Installed via Homebrew. (Prosody was not available in Homebrew.)
- **Prometheus**: Installed via Homebrew for monitoring.

## Virtual Environment

A Python virtual environment is created in `venv/`.

To activate: `source venv/bin/activate`

To deactivate: `deactivate`

## Starting Services

### XMPP Server (ejabberd)

To start ejabberd:

```bash
brew services start ejabberd
```

Or manually:

```bash
HOME="/usr/local/var/lib/ejabberd" /usr/local/opt/ejabberd/sbin/ejabberdctl start
```

Note: You may need to configure ejabberd first. The config file is at `/usr/local/etc/ejabberd/ejabberd.yml`.

### Prometheus

To start Prometheus:

```bash
brew services start prometheus
```

## PDT (Prometheus Design Tool)

PDT was not clearly identified. Assuming it's Prometheus for monitoring. If it's a specific tool, please provide more details.

## Usage

Activate the virtual environment and start developing agents with SPADE.

Example SPADE agent code:

```python
import spade

class MyAgent(spade.agent.Agent):
    async def setup(self):
        print("Agent starting")

if __name__ == "__main__":
    agent = MyAgent("agent@domain", "password")
    await agent.start()
```

## Requirements

- requirements.txt: Contains `spade`

To install additional packages: `pip install -r requirements.txt`

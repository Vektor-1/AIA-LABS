import logging
import spade

# Use INFO level for normal console output (reduces protocol-level noise)
logging.basicConfig(level=logging.INFO)

class BasicAgent(spade.agent.Agent):
    async def setup(self):
        logging.info("Basic Agent started")

async def main():
    agent = BasicAgent("agent1@localhost", "password", verify_security=False)
    await agent.start(auto_register=True)
    logging.info("Agent running")
    logging.info(" Agent is up and running")
    await spade.wait_until_finished(agent)

if __name__ == "__main__":
    spade.run(main())
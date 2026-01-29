import asyncio
import logging
import spade

logging.basicConfig(level=logging.INFO)


class BasicAgent(spade.agent.Agent):
    async def setup(self):
        logging.info("Basic Agent started")


async def main():
    agent = BasicAgent("agent1@localhost", "password", verify_security=False)
    await agent.start(auto_register=True)
    logging.info("Agent running")
    logging.info("Agent is up and running")
    
    try:
        await asyncio.sleep(10)  
    finally:
        logging.info("Stopping agent...")
        await agent.stop()
        logging.info("Agent stopped")


if __name__ == "__main__":
    spade.run(main())
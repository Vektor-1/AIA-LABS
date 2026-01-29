import spade

class BasicAgent(spade.agent.Agent):
    async def setup(self):
        print("Basic Agent started")

async def main():
    agent = BasicAgent("agent1@localhost", "password")
    await agent.start()
    print("Agent running")
    await spade.wait_until_finished(agent)

if __name__ == "__main__":
    spade.run(main())
from oncoflow.agent import OncoFlowAgent
import config

def main():
    agent = OncoFlowAgent(config)
    report = agent.run()
    print(report)

if __name__ == "__main__":
    main()

from dotenv import load_dotenv
load_dotenv()

from importlib.metadata import version 
core_version=version("langchain")
lg_version = version("langgraph")

from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic


print(f"langchain-core: {core_version}")
print(f"langgraph-version: {lg_version}")


def main():

    llm = ChatAnthropic(model="claude-sonnet-4-5-20250929",temperature=0)
    claudeResponse=llm.invoke("Say 'Environment Setup' in one word")

    print(f"Response from Claude: {claudeResponse}")



if __name__ == "__main__":
    main()

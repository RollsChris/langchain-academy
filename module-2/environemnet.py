from dotenv import load_dotenv
import os
print("Setting up environment variables")
load_dotenv()

print(os.environ["OPENAI_API_KEY"])
print(os.environ["TAVILY_API_KEY"])
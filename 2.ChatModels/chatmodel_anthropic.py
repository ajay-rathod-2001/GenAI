from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model_name="claude-opus-5",
    api_key="YOUR_ANTHROPIC_API_KEY"
)
result=model.invoke("What is capital of india")

print(result)


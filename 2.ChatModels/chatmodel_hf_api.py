from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
import os


llm = HuggingFaceEndpoint(
    model="Qwen/Qwen3.8-27B",
    task="text-generation",
    
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India?")

print(result.content)
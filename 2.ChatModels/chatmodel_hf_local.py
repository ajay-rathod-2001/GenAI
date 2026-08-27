from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm =HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen3.8-27B",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_token=100
    )
)

model= ChatHuggingFace(llm=llm)

result=model.invoke("what is capital of india and fianacial capital of india")

print(result.content)

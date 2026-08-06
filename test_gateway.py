from app.llms.gateway import call_llm


messages = [
    {
        "role": "user",
        "content": "Explain RAG in one sentence."
    }
]


response = call_llm(messages)
response2 = call_llm(messages)
response3 = call_llm(messages)
response4 = call_llm(messages)
response5 = call_llm(messages)

print(response)
print(response2)
print(response3)
print(response4)
print(response5)
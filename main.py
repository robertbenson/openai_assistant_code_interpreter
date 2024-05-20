from openai import OpenAI

client = OpenAI()

# method 1, Wrong Answer, hallucination
# method 1, Wrong Answer, hallucination
# method 1, Wrong Answer, hallucination


response = client.chat.completions.create(
    model='gpt-4o',
    messages=[
        {'role': 'system',
         'content': 'You help solve math problems. Answer only, no commentary'},
        {'role': 'user', 'content': 'What is 3.141593 times 7899324?'}
    ]

)
print("Asking Chatgpt directly - wrong answer - hallucination")
# print(response.choices[0].message.content)
number = float(response.choices[0].message.content)
formatted_number = f"{number:,.2f}"
print("\nChatGpt answer: ", formatted_number)
print("This is a wrong answer !!!!!!!!")

# method 2 using an assistant, correct answer
# method 2 using an assistant, correct answer
# method 2 using an assistant, correct answer


assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You can solve math problems written in text",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
)

thread = client.beta.threads.create()

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="What is 3.141593 times 7899324?"
)

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="show 6 decimal places of pi in numbers in answer. format answer with commas and 2 dp. Remove back slash's"
)

if run.status == 'completed':
    messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
    # print(messages)
    print("\nCorrect answer using openai assistant")
    print("Assistant response:   ", messages.data[0].content[0].text.value)

    number = 3.141593 * 7899324
    formatted_number = f"{number:,.2f}"
    print("\nPython calculated answer, accurate answer expected: ", formatted_number)

else:
    print(run.status)

# Assistant 
## Code Interpreter
```Python 
assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="You can solve math problems written in text",
    tools=[{"type": "code_interpreter"}],
    model="gpt-4o",
)
```

## Thread 
## Run

The run connects the assistant.id with the thread.id, they are now logically connected.

```Python 
run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant.id,
    instructions="show 6 decimal places of pi in numbers in answer. format answer with commas and 2 dp. Remove back slash's"
)
```
This will keep polling until finished.

```Python
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
  ```
## Hallucination 

While ChatGPT can handle simple arithmetic and algebraic expressions reasonably well, it is prone to hallucination when faced with complex mathematical problems. 
This is due to its design as a language model rather than a computational engine. 
For accurate and reliable results in advanced mathematics, the use of an assistant is advised.

## Output


```
Asking Chatgpt directly - wrong answer - hallucination
24792890.920892
This is a wrong answer !!!!!!!!

Correct answer using openai assistant
Assistant response:    The product of 3.141593 and 7,899,324 is 24,816,460.98.

Python calculated answer, accurate answer expected:  24,816,460.98
```
The python generated answer and the assistant generated answer are the same.

Sum to calculate is: `3.141593 * 7,899,324`

| Origin                           | Result        | Customisation                                                                                                                                     |
|----------------------------------|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ChatGpt   <br/>(Asking directly) | 24,733,643.87<br/>24,797,744.10<br/>24,743,699.36<br/>24,775,139.39 | LLM's are prone to hallucination.   <br/>This answer may vary with reruns.                                                                        |
| assistant                        | 24,816,460.98 | Requested a custom formatted output:<br/>show 6 decimal places of pi in numbers in answer. format answer with commas and 2 dp. Remove back slashs |
| python generated answer          | 24,816,460.98 | Formatted:      f"{number:,.2f}"                                                                                                                  |


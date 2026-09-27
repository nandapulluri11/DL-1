# Rule-Based AI Chatbot

A simple, deterministic rule-based chatbot built with Python that demonstrates basic AI decision-making using dictionary lookup.

## Project Objective

This project demonstrates **deterministic, rule-based decision-making** using programming logic. The chatbot simulates basic human-like interaction using explicitly defined rules and predefined responses—no machine learning, AI APIs, or complex frameworks.

## Features

- **Input Sanitization**: Converts input to lowercase and removes extra whitespace
- **Continuous Interaction**: Keeps running until user explicitly exits
- **Dictionary-Based Knowledge Base**: Uses Python dictionary for efficient response lookup
- **5+ Intents**: Greets, answers questions about itself, handles help, farewells, and more
- **Fallback Response**: Handles unknown inputs gracefully
- **Clean Exit**: Exit command works in any case (exit, EXIT, Exit, etc.)

## How It Works

The chatbot follows a simple pipeline:

1. **User Input**:接收用户消息
2. **Sanitization**: Convert to lowercase + remove whitespace
3. **Exit Check**: Check if user wants to quit
4. **Dictionary Lookup**: Find matching response in knowledge base
5. **Fallback**: Return default response if no match found
6. **Output**: Display chatbot response
7. **Repeat**: Continue loop

### Architecture

```
USER INPUT
     ↓
SANITIZATION (lower() + strip())
     ↓
EXIT CHECK → Yes → TERMINATE
     ↓ No
DICTIONARY LOOKUP
     ↓
MATCH FOUND? → Yes → RESPONSE
     ↓ No
FALLBACK RESPONSE
     ↓
DISPLAY OUTPUT
     ↓
REPEAT LOOP
```

## Technologies Used

- **Python 3**: Pure Python implementation
- **Dictionary**: Hash map for O(1) response lookup
- **No external dependencies**: Built-in Python only

## How to Run

1. Navigate to the project directory:
   ```bash
   cd rule-based-ai-chatbot
   ```

2. Run the chatbot:
   ```bash
   python chatbot.py
   ```

3. Type messages and press Enter to chat

4. Type `exit` to quit

## Example Interaction

```
====================================
     RULE-BASED AI CHATBOT
====================================
Bot: Hello! How can I help you?
Bot: Type 'exit' to quit.

You: hello
Bot: Hi there! How can I help you?
You: what is your name
Bot: I'm RuleBot, a simple rule-based chatbot.
You: tell me a joke
Bot: Why do programmers prefer dark mode? Because light attracts bugs!
You: exit
Bot: Goodbye!
```

## Test Cases

| Test Case         | Input                | Expected Result                    |
|-------------------|---------------------|-------------------------------------|
| Greeting          | hello               | Greeting response                   |
| Greeting case     | HELLO               | Same greeting response              |
| Whitespace        |   hello             | Greeting response                   |
| Second intent     | hi                  | Greeting response                   |
| Known intent      | help                | Help response                       |
| Unknown input     | xyz123              | Fallback response                   |
| Exit              | exit                | Goodbye + program termination       |
| Exit case         | EXIT                | Goodbye + program termination       |
| Empty input       | (empty string)      | Fallback response                   |
| Multiple messages | Several valid inputs| Loop continues correctly            |

## Why Dictionary Lookup Over If-Elif?

Dictionary lookup (`responses.get()`) is preferred over long if-elif chains because:

- **Cleaner code**: No repetitive conditional statements
- **Easier maintenance**: Add new responses by simply adding key-value pairs
- **Better performance**: O(1) hash table lookup vs O(n) sequential checks
- **Scalable**: Easy to expand the knowledge base without changing logic

## Future Improvements (Optional)

- Add more vocabulary and intents
- Support multiple phrases for the same intent
- Add a unique chatbot personality
- Implement nested conditions for more complex matching
- Add input validation and error handling

## Project Structure

```
rule-based-ai-chatbot/
├── chatbot.py    # Main implementation
└── README.md     # This file
```

---

*Built as part of the DecodeLabs Industrial Training Kit - Project 1*
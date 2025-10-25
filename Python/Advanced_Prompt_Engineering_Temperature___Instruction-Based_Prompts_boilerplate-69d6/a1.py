import os
import time
from google import genai
from google.genai import types
import config  # Make sure config.py has API_KEY = "your_gemini_api_key"

# 1. Function to generate a response from Gemini
def generate_response(prompt, temperature=0.5):
    """
    Generates a response from Google's Gemini API.
    """
    client = genai.Client(api_key=config.API_KEY)

    contents = [
        types.Content(
            parts=[types.Part.from_text(prompt)],
            role="user"
        )
    ]

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(temperature=temperature)
    )

    return response.text.strip() if response and response.text else "No response generated."

# 2. Temperature & Instruction Activity
def temperature_prompt_activity():
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)
    print("\nIn this activity, we'll explore:")
    print("1. How temperature affects AI creativity and randomness")
    print("2. How instruction-based prompts can control AI outputs")

    # Part 1: Temperature Exploration
    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    creative_prompt = input("Enter a creative prompt for the AI: ")

    for temp in [0.2, 0.5, 0.9]:
        print(f"\n--- Temperature: {temp} ---")
        print(generate_response(creative_prompt, temperature=temp))

    # Part 2: Instruction-Based Prompts
    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    topic = input("Enter a topic (e.g., climate change, space exploration): ")

    instructions = [
        f"Explain {topic} in simple terms for a 10-year-old.",
        f"Write a persuasive argument about {topic}.",
        f"List five surprising facts about {topic}."
    ]

    for instr in instructions:
        print(f"\nInstruction: {instr}")
        print(generate_response(instr, temperature=0.5))

    # Part 3: Create Your Own Instruction-Based Prompt
    print("\n" + "-" * 40)
    print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    custom_prompt = input("Enter your own instruction-based prompt: ")
    custom_temp = float(input("Enter a temperature value (0.1 to 1.0): "))

    print("\nAI Response:")
    print(generate_response(custom_prompt, temperature=custom_temp))

    # Reflection Questions
    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did changing the temperature affect the creativity and variety in the AI's responses?")
    print("2. Which instruction-based prompt produced the most useful or interesting result? Why?")
    print("3. How might you combine specific instructions and temperature settings in real applications?")
    print("4. What patterns did you notice in how the AI responds to different types of instructions?")

    # Challenge Activity
    print("\n" + "-" * 40)
    print("CHALLENGE ACTIVITY")
    print("-" * 40)
    print("Try creating a 'chain' of prompts where:")
    print("1. First, ask the AI to generate content about a topic")
    print("2. Then, use an instruction-based prompt to modify or build upon that content")
    print("3. Experiment with different temperature settings at each step")

# 3. Streaming Response Function
def generate_streaming_response(prompt, temperature=0.5):
    """
    Generates a streaming response from Gemini API.
    """
    client = genai.Client(api_key=config.API_KEY)

    contents = [
        types.Content(
            parts=[types.Part.from_text(prompt)],
            role="user"
        )
    ]

    for event in client.models.generate_content_stream(
        model="gemini-1.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(temperature=temperature)
    ):
        if event.candidates and event.candidates[0].content.parts:
            print(event.candidates[0].content.parts[0].text, end="", flush=True)
    print()

# Main Execution
if __name__ == "__main__":
    temperature_prompt_activity()

    see_stream = input("\nDo you want to see streaming responses? (yes/no): ").strip().lower()
    if see_stream == "yes":
        stream_prompt = input("Enter a prompt for streaming: ")
        temp = float(input("Enter a temperature value (0.1 to 1.0): "))
        generate_streaming_response(stream_prompt, temperature=temp)

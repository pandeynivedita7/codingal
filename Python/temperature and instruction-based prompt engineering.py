import os
import time
from google import genai
from google.genai import types
import config

def generate_response(prompt, temperature=0.5):
    client = genai.Client(api_key=config.API_KEY)
    contents = [types.Content(role="user", parts=[types.Part.from_text(prompt)])]
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(temperature=temperature)
    )
    return response.candidates[0].content.parts[0].text

def temperature_prompt_activity():
    print("=" * 80)
    print("ADVANCED PROMPT ENGINEERING: TEMPERATURE & INSTRUCTION-BASED PROMPTS")
    print("=" * 80)
    print("\nIn this activity, we'll explore:")
    print("1. How temperature affects AI creativity and randomness")
    print("2. How instruction-based prompts can control AI outputs")

    print("\n" + "-" * 40)
    print("PART 1: TEMPERATURE EXPLORATION")
    print("-" * 40)

    user_prompt = input("Enter a creative prompt: ")

    for temp in [0.2, 0.5, 0.9]:
        print(f"\nTemperature {temp}:")
        print(generate_response(user_prompt, temperature=temp))

    print("\n" + "-" * 40)
    print("PART 2: INSTRUCTION-BASED PROMPTS")
    print("-" * 40)

    topic = input("Enter a topic: ")
    instructions = [
        f"Explain {topic} in simple terms for a 10-year-old.",
        f"Write a poem about {topic}.",
        f"List 5 surprising facts about {topic}."
    ]

    for instr in instructions:
        print(f"\nInstruction: {instr}")
        print(generate_response(instr, temperature=0.5))

    print("\n" + "-" * 40)
    print("PART 3: CREATING YOUR OWN INSTRUCTION-BASED PROMPTS")
    print("-" * 40)
    custom_prompt = input("Enter your own instruction-based prompt: ")
    custom_temp = float(input("Enter a temperature (0.1 to 1.0): "))
    print(generate_response(custom_prompt, temperature=custom_temp))

    print("\n" + "-" * 40)
    print("REFLECTION QUESTIONS")
    print("-" * 40)
    print("1. How did changing the temperature affect the creativity and variety in the AI's responses?")
    print("2. Which instruction-based prompt produced the most useful or interesting result? Why?")
    print("3. How might you combine specific instructions and temperature settings in real applications?")
    print("4. What patterns did you notice in how the AI responds to different types of instructions?")

    print("\n" + "-" * 40)
    print("CHALLENGE ACTIVITY")
    print("-" * 40)
    print("Try creating a 'chain' of prompts where:")
    print("1. First, ask the AI to generate content about a topic")
    print("2. Then, use an instruction-based prompt to modify or build upon that content")
    print("3. Experiment with different temperature settings at each step")

def generate_streaming_response(prompt, temperature=0.5):
    client = genai.Client(api_key=config.API_KEY)
    contents = [types.Content(role="user", parts=[types.Part.from_text(prompt)])]
    response = client.models.generate_content_stream(
        model="gemini-1.5-flash",
        contents=contents,
        config=types.GenerateContentConfig(temperature=temperature)
    )
    for chunk in response:
        print(chunk.text, end="", flush=True)

if __name__ == "__main__":
    temperature_prompt_activity()
    see_streaming = input("\nDo you want to see a streaming response? (y/n): ")
    if see_streaming.lower() == "y":
        streaming_prompt = input("Enter a prompt for streaming: ")
        generate_streaming_response(streaming_prompt, temperature=0.5)

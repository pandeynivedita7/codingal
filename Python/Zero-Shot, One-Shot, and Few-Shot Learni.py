# Install required library (run once)
# !pip install transformers torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to generate response
def get_response(prompt, max_length=80):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
zero_shot_prompt = "What are the benefits of exercise?"
print("Zero-Shot Response:\n", get_response(zero_shot_prompt))
one_shot_prompt = """
Q: What are the benefits of reading?
A: Reading improves knowledge, vocabulary, and concentration.

Q: What are the benefits of exercise?
A:
"""
print("One-Shot Response:\n", get_response(one_shot_prompt))

few_shot_prompt = """
Q: What are the benefits of reading?
A: Reading improves knowledge, vocabulary, and concentration.

Q: What are the benefits of meditation?
A: Meditation helps reduce stress and improves focus.

Q: What are the benefits of exercise?
A:
"""
print("Few-Shot Response:\n", get_response(few_shot_prompt))



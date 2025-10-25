from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Function to get response
def get_response(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    outputs = model.generate(
        inputs,
        max_length=max_length,
        num_return_sequences=1,
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

# Question form
question_prompt = "What are the benefits of exercise?"
print(f"Question Prompt Response: {get_response(question_prompt)}\n")

# Command form
command_prompt = "List five benefits of exercise."
print(f"Command Prompt Response: {get_response(command_prompt)}")

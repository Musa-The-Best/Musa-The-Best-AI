from transformers import GPT2LMHeadModel, GPT2Tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')
def get_response(prompt, max_length=50):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response
question_prompt = "What are the benfits of excersize?"
print(f"Question Prompt Response: {get_response(question_prompt)}\n")
command_prompt = "List five benefits of excersize."
print(f"Command prompt Response: {get_response(command_prompt)}")
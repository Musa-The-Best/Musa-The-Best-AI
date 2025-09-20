from google import genai
import Config
client =  genai.client.Client(api_key=Config.MUSA_API_KEY)
def generate_response(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
def silly_prompt():
    print("Welcome to the AI Prompt Engineering Tutorial")
    print("In this activity, we will learn about \"Clarity and Specificity\"* and \"Contextual Information\"* in crafting prompts for AI.")
    print("\nLet's start by crafting a vague prompt, making it more specific, and then adding context.")
    vague_prompt = input("\nPlease enter a vague prompt (e.g., 'Tell me about technology'): ")
    print(f"\nYour vague prompt: {vague_prompt}")
    vague_response = generate_response(vague_prompt)
    print("\nAI's response to the vague prompt:")
    print(vague_response)
    specific_prompt = input("\nNow, make the prompt more specific (e.g., 'Explain how AI works in self-driving cars'): ")
print(f"\nYour specific prompt: {"specific_prompt"}")
specific_response = generate_response("specific_prompt")
print("\nAI's response to the specific prompt:")
print(specific_response)
contextual_prompt = input("\nNow, add context to your specific prompt (e.g., 'Given the advancements in autonomous vehicles, explain how AI is used in self-driving cars to make real-time driving decisions'): ")
print(f"\nYour contextual prompt: {contextual_prompt}")
contextual_response = generate_response(contextual_prompt)
print("\nAI's response to the contextual prompt:")
print(contextual_response)
print("\n--- Reflection ---")
print("1. How did the AI's response change when the prompt was made more specific?")
print("2. How did the AI's response improve with the added context?")
print("3. Which prompt produced the most relevant and tailored response? Why?")
silly_prompt()
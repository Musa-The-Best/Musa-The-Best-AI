import os
from google import genai
from google.genai import types
import Config
client = genai.Client(api_key=Config.MUSA_API_KEY)
def generate_response(prompt, temperature=0.3):
    """Generate a response from Gemini API."""
    try:
        contents = [types.Content(role="user", parts=[
            types.Part.from_text(text=prompt)
        ])]
        Config_params = types.GenerateContentConfig(temperature=temperature)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=contents, Config=Config_params
        )
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
def reinforcement_learning_activity():
    """Conducts the reinforcement learning activity."""
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ===\n")
    prompt = input( "Enter a prompt for the AI model (e.g., 'Describe the lion'): ")
    intial_response = generate_response(prompt)
    print(f"\nIn initial AI Response: {initial_response}")
    rating = int(input("Rate the response from 1 (bad) to 5 (good)")
    feedback = input("Provide feedback for improvement: ")
    improved_response = f"{initial_response} (Improved with your feedback: {feedback})"
    print(f"\nImproved AI Response: {improved_response}")
    print("\nReflection:")
    print("1. How did the model's response improve with feedback?")
    print("2. How does reinforcement learning help AI to improve its performance over time?")

    def role_based_prompt_activity():
    """Conducts the role-based prompts activity."""
    print("\n=== ROLE-BASED PROMPTS ACTIVITY ===\n")
    category = input("Enter a category (e.g., science, history, math): ")
    item = input(f"Enter a specific {category} topic (e.g., 'photosynthesis' for science): ")
    teacher_prompt = f"You are a teacher. Explain {item} in simple terms."
    expert_prompt = f"You are an expert in {category}. Explain {item} in a detailed, technical manner."
    teacher_response = generate_response(teacher_prompt)
    expert_response = generate_response(expert_prompt)
    print(f"\n--- Teacher's Perspective ---\n{teacher_response}")
    print(f"\n--- Expert's Perspective ---\n{expert_response}")
    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher's and expert's perspectives?")
    print("2. How can  role based prompts help tailor AI responses for different contexts?")
    def run_activity():
        """"Runs the entire activity for the user."""
        print("\n=== AI Learning Activity ==== ")
        activity_choice = input ("Which actitivy would you like to run? (1:Reinforcement Learning, 2: Role-Based Prompts): ")
        if actrivity_choice = "1":
            reinforcement_learning_activity()
        elif activity_choice == "2":
            role_based_prompt_activity()
        else:
            print("Invalid choice. Please choose either 1 or 2.")
if __name__ == "__main__":
run_activity()
# 1. IMPORT necessary libraries:
#    - google.genai (for interacting with the Gemini API)
#    - config (for managing API key)

# 2. DEFINE function generate_response(prompt, temperature=0.3):
#    - Initialize genai client using the API key from config
#    - Create the content structure based on the user's prompt
#    - Send the prompt to Gemini API and return the generated response text

# 3. DEFINE function reinforcement_learning_activity():
#    - Print introductory message for reinforcement learning
#    - Get user input for a prompt (e.g., "Describe the lion")
#    - Generate initial AI response using generate_response
#    - Get user feedback (rating and improvement suggestions)
#    - Simulate model improvement with the feedback (combine initial response with feedback)
#    - Display the improved AI response
#    - Ask reflection questions about how feedback affects AI performance

# 4. DEFINE function role_based_prompt_activity():
#    - Print introductory message for role-based prompts
#    - Get user input for a category (e.g., science) and specific topic (e.g., "photosynthesis")
#    - Generate two prompts: one for a teacher's explanation and one for an expert's explanation
#    - Generate and display responses from both perspectives
#    - Ask reflection questions on how role-based prompts affect the AI's responses

# 5. DEFINE function run_activity():
#    - Print introductory message for the AI Learning Activity
#    - Prompt the user to choose between the reinforcement learning activity or role-based prompts
#    - If the user chooses "1", run reinforcement_learning_activity()
#    - If the user chooses "2", run role_based_prompt_activity()
#    - If the user enters an invalid choice, prompt them again

# 6. IF __name__ == "__main__":
#    - Call run_activity() to initiate the activity

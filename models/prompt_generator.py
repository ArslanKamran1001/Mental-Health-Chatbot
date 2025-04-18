class PromptGenerator:
    def __init__(self):
        self.emotion_prompts = {
            "anger": "I notice you're feeling angry. Would you like to talk about what's causing this anger? It's completely normal to feel this way, and I'm here to listen.",
            "disgust": "I sense that you're feeling disgusted. This can be a challenging emotion to deal with. Would you like to explore what triggered this feeling?",
            "fear": "I can see that you're feeling afraid. Fear is a natural response to perceived threats. Would you like to discuss what's making you feel this way?",
            "happiness": "I'm glad to see you're feeling happy! Would you like to share what's bringing you joy? Celebrating positive moments can help build resilience.",
            "neutral": "I notice you seem neutral right now. How are you feeling about things in general? Sometimes taking a moment to reflect can be helpful.",
            "sadness": "I can see that you're feeling sad. It's okay to feel this way, and you don't have to go through it alone. Would you like to talk about what's troubling you?",
            "surprise": "I notice you seem surprised. This can be both positive and challenging. Would you like to talk about what caught you off guard?"
        }

    def generate_prompt(self, emotion, user_input=""):
        """
        Generate a prompt that includes emotion context and user input.
        
        Args:
            emotion (str): The detected emotion
            user_input (str): The user's message
            
        Returns:
            str: A formatted prompt for the LLM
        """
        # Get the base prompt for the detected emotion
        base_prompt = self.emotion_prompts.get(emotion, self.emotion_prompts["neutral"])
        
        if user_input:
            # For LangChain, we'll format the prompt to include the emotion context
            # but let the conversation memory handle the actual dialogue flow
            return f"{base_prompt}\n\nUser: {user_input}"
        
        return base_prompt

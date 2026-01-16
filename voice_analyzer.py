"""
Voice Analysis Engine
Logic for Gender, Age, and Emotion detection
"""
import numpy as np

def analyze_voice(file_path):
    """
    Analyzes the audio file for gender, age, and emotion.
    This is the core logic required by the GUI.
    """
    try:
        # In a production environment, this is where you would load 
        # your trained models and process the audio features.
        
        # MOCK LOGIC FOR DEMONSTRATION:
        # 1. Randomly decide if it's male or female for testing
        is_male = np.random.choice([True, False], p=[0.7, 0.3])
        
        if not is_male:
            return {"status": "rejected", "message": "Upload male voice"}
            
        # 2. If male, estimate age (18 to 80)
        estimated_age = int(np.random.randint(18, 85))
        
        # 3. Check for Senior Citizen status (>60)
        is_senior = estimated_age > 60
        emotion = None
        
        if is_senior:
            emotions = ['Happy', 'Sad', 'Angry', 'Neutral']
            emotion = np.random.choice(emotions)
            
        return {
            "status": "success",
            "age": estimated_age,
            "is_senior": is_senior,
            "emotion": emotion
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
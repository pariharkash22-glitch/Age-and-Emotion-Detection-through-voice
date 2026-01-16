import librosa
import numpy as np
import soundfile as sf

def analyze_voice(file_path):
    """
    Main logic: Detects gender, then age, then emotion if senior.
    """
    try:
        y, sr = librosa.load(file_path, sr=None)
        
        # 1. Feature Extraction (Logic for Gender Detection)
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        pitch = np.mean(pitches[pitches > 0]) if np.any(pitches > 0) else 0
        
        # 2. Gender Check (Female voices typically > 165Hz)
        if pitch > 165:
            return {"status": "rejected", "message": "Upload male voice"}
        
        # 3. Age Estimation Logic (Simulation of ML Model Output)
        # In a full ML version, this would be: age_model.predict(features)
        estimated_age = _mock_age_predictor(y)
        
        result = {
            "status": "success",
            "age": estimated_age,
            "is_senior": estimated_age > 60,
            "emotion": None
        }
        
        # 4. Emotion Detection (Only for Seniors > 60)
        if result["is_senior"]:
            result["emotion"] = _mock_emotion_predictor(y)
            
        return result
    except Exception as e:
        return {"status": "error", "message": str(e)}

def _mock_age_predictor(audio_data):
    # Placeholder for logic: maps audio characteristics to age
    return int(np.random.normal(45, 20)) # For demo purposes

def _mock_emotion_predictor(audio_data):
    emotions = ['Happy', 'Sad', 'Angry', 'Neutral']
    return np.random.choice(emotions)
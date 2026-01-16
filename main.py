"""
Voice Age & Emotion Detection System
Main Entry Point

Author: ML Developer
Date: January 2026
Description: Detects age from male voices and emotions for senior citizens
"""

from gui_interface import start_gui

if __name__ == "__main__":
    print("=" * 60)
    print("  Voice Age & Emotion Detection System")
    print("=" * 60)
    print("Starting GUI...")
    print("\nInstructions:")
    print("1. Click 'Select Audio File' to choose a voice recording")
    print("2. Click 'Analyze Voice' to process the audio")
    print("3. View the results on screen")
    print("\nNote: Only male voices are processed.")
    print("=" * 60)
    
    try:
        start_gui()
    except KeyboardInterrupt:
        print("\n\nApplication closed by user.")
    except Exception as e:
        print(f"\n\nError starting application: {e}")
        print("Please ensure all dependencies are installed:")
        print("pip install -r requirements.txt")

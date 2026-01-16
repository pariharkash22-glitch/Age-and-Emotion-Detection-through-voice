"""
Setup Script for Voice Age & Emotion Detection System
Automates installation and verification
"""

import subprocess
import sys
import os

def print_header(text):
    """Print formatted header"""
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")

def check_python_version():
    """Check if Python version is adequate"""
    print_header("Checking Python Version")
    
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ ERROR: Python 3.8 or higher is required!")
        print("Please upgrade Python from https://www.python.org/downloads/")
        return False
    
    print("✅ Python version is compatible")
    return True

def install_dependencies():
    """Install required packages"""
    print_header("Installing Dependencies")
    
    requirements = [
        "numpy==1.24.3",
        "librosa==0.10.1",
        "soundfile==0.12.1",
        "scipy==1.11.4",
        "matplotlib==3.7.1"
    ]
    
    print("Installing packages:")
    for package in requirements:
        print(f"  • {package}")
    
    try:
        subprocess.check_call([
            sys.executable, 
            "-m", 
            "pip", 
            "install",
            "--upgrade",
            "pip"
        ])
        
        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            "-r",
            "requirements.txt"
        ])
        
        print("\n✅ All dependencies installed successfully")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing dependencies: {e}")
        print("\nTry installing manually:")
        print("  pip install -r requirements.txt")
        return False

def verify_installation():
    """Verify that all packages are correctly installed"""
    print_header("Verifying Installation")
    
    packages = [
        ("numpy", "np"),
        ("librosa", "librosa"),
        ("soundfile", "soundfile"),
        ("scipy", "scipy"),
        ("tkinter", "tk")
    ]
    
    all_good = True
    
    for package_name, import_name in packages:
        try:
            __import__(import_name)
            print(f"✅ {package_name} - OK")
        except ImportError:
            print(f"❌ {package_name} - FAILED")
            all_good = False
    
    if all_good:
        print("\n✅ All packages verified successfully")
    else:
        print("\n❌ Some packages failed to import")
        print("Try reinstalling: pip install -r requirements.txt")
    
    return all_good

def check_files():
    """Check if all required files are present"""
    print_header("Checking Project Files")
    
    required_files = [
        "main.py",
        "voice_analyzer.py",
        "gui_interface.py",
        "train_models.py",
        "requirements.txt"
    ]
    
    all_present = True
    
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✅ {filename} - Found")
        else:
            print(f"❌ {filename} - Missing")
            all_present = False
    
    if not all_present:
        print("\n⚠️  Some files are missing!")
        print("Please ensure all project files are in the same folder")
    else:
        print("\n✅ All required files present")
    
    return all_present

def create_test_audio_info():
    """Provide information about test audio files"""
    print_header("Test Audio Files")
    
    print("To test the application, you need audio files.")
    print("\nOptions:")
    print("1. Record using Windows Voice Recorder or macOS QuickTime")
    print("2. Download free samples from https://freesound.org/")
    print("3. Use online voice recorder: https://online-voice-recorder.com/")
    print("\nSupported formats: WAV, MP3, FLAC, OGG")
    print("Recommended: Clear, noise-free recordings, 5-15 seconds long")

def run_application():
    """Ask user if they want to run the application"""
    print_header("Launch Application")
    
    response = input("Would you like to launch the application now? (y/n): ").strip().lower()
    
    if response == 'y':
        print("\n🚀 Launching Voice Age & Emotion Detector...\n")
        try:
            subprocess.call([sys.executable, "main.py"])
        except Exception as e:
            print(f"❌ Error launching application: {e}")
            print("\nTry running manually: python main.py")
    else:
        print("\nYou can run the application later with:")
        print("  python main.py")

def main():
    """Main setup process"""
    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     Voice Age & Emotion Detection System                  ║
║            Setup & Installation                            ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    # Step 1: Check Python version
    if not check_python_version():
        input("\nPress Enter to exit...")
        return
    
    # Step 2: Check files
    if not check_files():
        input("\nPress Enter to exit...")
        return
    
    # Step 3: Install dependencies
    if not install_dependencies():
        input("\nPress Enter to exit...")
        return
    
    # Step 4: Verify installation
    if not verify_installation():
        input("\nPress Enter to exit...")
        return
    
    # Step 5: Provide test audio info
    create_test_audio_info()
    
    # Step 6: Success message
    print_header("Setup Complete!")
    print("✅ Installation successful!")
    print("✅ All dependencies installed")
    print("✅ All files verified")
    print("\nThe application is ready to use!")
    
    # Step 7: Offer to launch
    print()
    run_application()
    
    print("\n" + "=" * 60)
    print("Thank you for installing Voice Age & Emotion Detector!")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup interrupted by user.")
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        print("Please report this issue.")
    finally:
        input("\nPress Enter to exit...")

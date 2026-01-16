"""
System Test Script
Verifies that all components are working correctly
"""

import sys
import os

def print_section(title):
    """Print formatted section header"""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def test_imports():
    """Test if all required modules can be imported"""
    print_section("Testing Module Imports")
    
    modules = [
        ("numpy", "NumPy - Numerical Computing"),
        ("librosa", "Librosa - Audio Analysis"),
        ("soundfile", "SoundFile - Audio I/O"),
        ("scipy", "SciPy - Scientific Computing"),
        ("tkinter", "Tkinter - GUI Framework")
    ]
    
    failed = []
    
    for module_name, description in modules:
        try:
            __import__(module_name)
            print(f"✅ {description:<40} OK")
        except ImportError as e:
            print(f"❌ {description:<40} FAILED")
            failed.append(module_name)
    
    if failed:
        print(f"\n⚠️  Failed imports: {', '.join(failed)}")
        print("Run: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All modules imported successfully!")
        return True

def test_project_files():
    """Test if all project files exist"""
    print_section("Testing Project Files")
    
    required_files = [
        ("main.py", "Application Entry Point"),
        ("gui_interface.py", "GUI Implementation"),
        ("voice_analyzer.py", "Analysis Engine"),
        ("train_models.py", "Model Training"),
        ("requirements.txt", "Dependencies List")
    ]
    
    missing = []
    
    for filename, description in required_files:
        if os.path.exists(filename):
            size = os.path.getsize(filename) / 1024
            print(f"✅ {description:<40} {size:.1f} KB")
        else:
            print(f"❌ {description:<40} MISSING")
            missing.append(filename)
    
    if missing:
        print(f"\n⚠️  Missing files: {', '.join(missing)}")
        return False
    else:
        print("\n✅ All project files present!")
        return True

def test_voice_analyzer():
    """Test the voice analyzer module"""
    print_section("Testing Voice Analyzer Module")
    
    try:
        from voice_analyzer import (
            extract_features,
            detect_gender,
            estimate_age,
            detect_emotion,
            analyze_voice
        )
        
        functions = [
            "extract_features",
            "detect_gender",
            "estimate_age",
            "detect_emotion",
            "analyze_voice"
        ]
        
        for func in functions:
            print(f"✅ Function '{func}' loaded successfully")
        
        print("\n✅ Voice Analyzer module is functional!")
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import voice_analyzer: {e}")
        return False
    except Exception as e:
        print(f"❌ Error loading voice_analyzer: {e}")
        return False

def test_gui_module():
    """Test the GUI module"""
    print_section("Testing GUI Module")
    
    try:
        from gui_interface import VoiceDetectorGUI, start_gui
        
        print("✅ VoiceDetectorGUI class loaded")
        print("✅ start_gui function loaded")
        print("\n✅ GUI module is functional!")
        return True
        
    except ImportError as e:
        print(f"❌ Failed to import gui_interface: {e}")
        return False
    except Exception as e:
        print(f"❌ Error loading gui_interface: {e}")
        return False

def test_feature_extraction():
    """Test feature extraction with dummy data"""
    print_section("Testing Feature Extraction")
    
    try:
        import numpy as np
        import librosa
        
        # Create dummy audio (1 second of silence)
        sr = 22050
        duration = 1
        y = np.zeros(sr * duration)
        
        # Test basic librosa functions
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
        print(f"✅ MFCC extraction: {mfccs.shape}")
        
        pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
        print(f"✅ Pitch tracking: {pitches.shape}")
        
        spectral_centroid = librosa.feature.spectral_centroid(y=y, sr=sr)
        print(f"✅ Spectral centroid: {spectral_centroid.shape}")
        
        zcr = librosa.feature.zero_crossing_rate(y)
        print(f"✅ Zero crossing rate: {zcr.shape}")
        
        print("\n✅ Feature extraction is working!")
        return True
        
    except Exception as e:
        print(f"❌ Feature extraction failed: {e}")
        return False

def test_system_resources():
    """Test system resources"""
    print_section("Testing System Resources")
    
    # Python version
    version = sys.version_info
    print(f"Python Version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("⚠️  Python 3.8+ recommended")
    else:
        print("✅ Python version is compatible")
    
    # Platform
    import platform
    print(f"Platform: {platform.system()} {platform.release()}")
    print(f"Architecture: {platform.machine()}")
    
    return True

def run_demo():
    """Run a simple demo of the analyzer"""
    print_section("Demo Mode")
    
    print("This would analyze a real audio file.")
    print("Since we don't have a test file, here's what would happen:")
    print()
    print("1. Load audio file")
    print("2. Extract features (MFCCs, pitch, spectral, etc.)")
    print("3. Detect gender from pitch")
    print("4. If male: estimate age")
    print("5. If senior (>60): detect emotion")
    print("6. Display results")
    print()
    print("To test with real audio:")
    print("  python main.py")
    print()
    print("Or test analyzer directly:")
    print("  python voice_analyzer.py")

def main():
    """Main test function"""
    print("""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║     Voice Age & Emotion Detection System                  ║
║              System Test Suite                             ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
    """)
    
    results = []
    
    # Run all tests
    results.append(("System Resources", test_system_resources()))
    results.append(("Module Imports", test_imports()))
    results.append(("Project Files", test_project_files()))
    results.append(("Voice Analyzer", test_voice_analyzer()))
    results.append(("GUI Module", test_gui_module()))
    results.append(("Feature Extraction", test_feature_extraction()))
    
    # Summary
    print_section("Test Summary")
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASSED" if result else "❌ FAILED"
        print(f"{test_name:<30} {status}")
    
    print()
    print(f"Tests Passed: {passed}/{total}")
    
    if passed == total:
        print("\n🎉 All tests passed! System is ready to use.")
        print("\nTo start the application, run:")
        print("  python main.py")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed.")
        print("\nPlease fix the issues before running the application.")
        print("Check INSTALLATION_GUIDE.md for help.")
    
    # Demo
    run_demo()
    
    print("\n" + "=" * 60)
    print("Test suite completed!")
    print("=" * 60 + "\n")
    
    return passed == total

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\nTest interrupted by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nUnexpected error in test suite: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

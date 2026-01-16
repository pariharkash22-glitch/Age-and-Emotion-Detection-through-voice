"""
GUI Interface Module
Provides the graphical user interface for voice analysis
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from voice_analyzer import analyze_voice
import threading
import os

class VoiceDetectorGUI:
    """Main GUI Application Class"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Age & Emotion Detector")
        self.root.geometry("650x550")
        self.root.resizable(False, False)
        
        # Configure colors
        self.colors = {
            'primary': '#2c3e50',
            'success': '#27ae60',
            'danger': '#e74c3c',
            'senior': '#9b59b6',
            'info': '#3498db',
            'light': '#ecf0f1',
            'dark': '#34495e',
            'bg': '#f0f0f0'
        }
        
        self.root.configure(bg=self.colors['bg'])
        
        # Audio file path
        self.audio_path = None
        
        # Build the UI
        self.setup_ui()
        
    def setup_ui(self):
        """Setup all UI components"""
        
        # Header Section
        self.create_header()
        
        # Main Content
        self.create_content()
        
        # Footer
        self.create_footer()
        
    def create_header(self):
        """Create header with title"""
        header_frame = tk.Frame(self.root, bg=self.colors['primary'], height=90)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Title
        title_label = tk.Label(
            header_frame,
            text="🎤 Voice Age & Emotion Detector",
            font=('Arial', 22, 'bold'),
            fg='white',
            bg=self.colors['primary']
        )
        title_label.pack(pady=15)
        
        # Subtitle
        subtitle_label = tk.Label(
            header_frame,
            text="AI-Powered Voice Analysis System",
            font=('Arial', 10),
            fg='#bdc3c7',
            bg=self.colors['primary']
        )
        subtitle_label.pack()
        
    def create_content(self):
        """Create main content area"""
        content_frame = tk.Frame(self.root, bg=self.colors['bg'])
        content_frame.pack(pady=20, padx=30, fill='both', expand=True)
        
        # Instructions Section
        self.create_instructions(content_frame)
        
        # File Selection Section
        self.create_file_section(content_frame)
        
        # Action Buttons Section
        self.create_action_section(content_frame)
        
        # Results Section
        self.result_frame = tk.Frame(content_frame, bg=self.colors['bg'])
        self.result_frame.pack(pady=15, fill='both', expand=True)
        
    def create_instructions(self, parent):
        """Create instructions panel"""
        instruction_frame = tk.Frame(parent, bg='white', relief='solid', borderwidth=1)
        instruction_frame.pack(pady=10, fill='x')
        
        title = tk.Label(
            instruction_frame,
            text="📋 Instructions",
            font=('Arial', 11, 'bold'),
            bg='white',
            fg=self.colors['dark']
        )
        title.pack(anchor='w', padx=15, pady=(10, 5))
        
        instructions = [
            "• Upload a male voice audio file (WAV, MP3, FLAC, OGG)",
            "• System detects age for all male voices",
            "• Senior citizens (>60) get emotion analysis",
            "• Female voices will be rejected automatically"
        ]
        
        for instruction in instructions:
            label = tk.Label(
                instruction_frame,
                text=instruction,
                font=('Arial', 9),
                bg='white',
                fg='#555',
                justify='left'
            )
            label.pack(anchor='w', padx=15, pady=2)
        
        tk.Label(instruction_frame, text="", bg='white', height=1).pack()
        
    def create_file_section(self, parent):
        """Create file selection section"""
        file_frame = tk.Frame(parent, bg=self.colors['bg'])
        file_frame.pack(pady=15)
        
        # File display label
        self.file_label = tk.Label(
            file_frame,
            text="📁 No file selected",
            font=('Arial', 10),
            bg=self.colors['light'],
            fg='#7f8c8d',
            width=50,
            height=2,
            relief='groove',
            borderwidth=2
        )
        self.file_label.pack(pady=5)
        
        # Select file button
        select_btn = tk.Button(
            file_frame,
            text="📂 Select Audio File",
            font=('Arial', 11, 'bold'),
            bg=self.colors['info'],
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            cursor='hand2',
            width=22,
            height=2,
            relief='raised',
            borderwidth=2,
            command=self.select_file
        )
        select_btn.pack(pady=10)
        
    def create_action_section(self, parent):
        """Create action buttons section"""
        action_frame = tk.Frame(parent, bg=self.colors['bg'])
        action_frame.pack(pady=10)
        
        # Analyze button
        self.analyze_btn = tk.Button(
            action_frame,
            text="🎯 Analyze Voice",
            font=('Arial', 14, 'bold'),
            bg=self.colors['success'],
            fg='white',
            activebackground='#229954',
            activeforeground='white',
            cursor='hand2',
            width=20,
            height=2,
            relief='raised',
            borderwidth=3,
            command=self.analyze_voice_thread,
            state='disabled'
        )
        self.analyze_btn.pack(side='left', padx=5)
        
        # Reset button
        reset_btn = tk.Button(
            action_frame,
            text="🔄 Reset",
            font=('Arial', 11, 'bold'),
            bg='#95a5a6',
            fg='white',
            activebackground='#7f8c8d',
            activeforeground='white',
            cursor='hand2',
            width=10,
            height=2,
            relief='raised',
            borderwidth=2,
            command=self.reset
        )
        reset_btn.pack(side='left', padx=5)
        
        # Progress bar (initially hidden)
        self.progress = ttk.Progressbar(
            parent,
            mode='indeterminate',
            length=400
        )
        
    def create_footer(self):
        """Create footer"""
        footer_frame = tk.Frame(self.root, bg=self.colors['primary'], height=35)
        footer_frame.pack(side='bottom', fill='x')
        
        footer_label = tk.Label(
            footer_frame,
            text="Developed with ❤️ for ML Challenge 2026",
            font=('Arial', 9),
            fg='white',
            bg=self.colors['primary']
        )
        footer_label.pack(pady=8)
        
    def select_file(self):
        """Open file dialog to select audio file"""
        file_path = filedialog.askopenfilename(
            title="Select Audio File",
            filetypes=[
                ("Audio Files", "*.wav *.mp3 *.flac *.ogg *.m4a"),
                ("WAV files", "*.wav"),
                ("MP3 files", "*.mp3"),
                ("FLAC files", "*.flac"),
                ("OGG files", "*.ogg"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.audio_path = file_path
            filename = os.path.basename(file_path)
            
            # Update label
            self.file_label.config(
                text=f"✅ Selected: {filename}",
                fg=self.colors['success'],
                bg='#d5f4e6'
            )
            
            # Enable analyze button
            self.analyze_btn.config(state='normal')
            
            # Clear previous results
            self.clear_results()
            
            print(f"[GUI] File selected: {filename}")
    
    def analyze_voice_thread(self):
        """Run voice analysis in a separate thread to prevent UI freezing"""
        if not self.audio_path:
            messagebox.showwarning("No File", "Please select an audio file first!")
            return
        
        if not os.path.exists(self.audio_path):
            messagebox.showerror("File Not Found", "The selected file no longer exists!")
            return
        
        # Disable analyze button
        self.analyze_btn.config(state='disabled')
        
        # Show progress bar
        self.progress.pack(pady=10)
        self.progress.start(10)
        
        # Clear previous results
        self.clear_results()
        
        # Run analysis in separate thread
        thread = threading.Thread(target=self.perform_analysis, daemon=True)
        thread.start()
    
    def perform_analysis(self):
        """Perform the voice analysis (runs in separate thread)"""
        try:
            print(f"[GUI] Starting analysis...")
            result = analyze_voice(self.audio_path)
            print(f"[GUI] Analysis complete: {result['status']}")
            
            # Update UI in main thread
            self.root.after(0, self.display_results, result)
            
        except Exception as e:
            print(f"[GUI] Error during analysis: {e}")
            self.root.after(0, self.display_error, str(e))
    
    def display_results(self, result):
        """Display analysis results"""
        # Stop progress bar
        self.progress.stop()
        self.progress.pack_forget()
        
        # Re-enable analyze button
        self.analyze_btn.config(state='normal')
        
        # Clear previous results
        self.clear_results()
        
        if result['status'] == 'rejected':
            # Female voice detected
            self.show_rejection()
            
        elif result['status'] == 'success':
            # Success - display results
            if result['is_senior']:
                self.show_senior_results(result)
            else:
                self.show_age_results(result)
                
        else:
            # Error
            messagebox.showerror("Analysis Error", result['message'])
    
    def show_rejection(self):
        """Show rejection message for female voices"""
        result_box = tk.Frame(
            self.result_frame,
            bg=self.colors['danger'],
            relief='solid',
            borderwidth=3
        )
        result_box.pack(fill='both', expand=True, padx=10, pady=10)
        
        icon_label = tk.Label(
            result_box,
            text="❌",
            font=('Arial', 40),
            bg=self.colors['danger'],
            fg='white'
        )
        icon_label.pack(pady=(20, 10))
        
        message_label = tk.Label(
            result_box,
            text="Upload male voice",
            font=('Arial', 18, 'bold'),
            bg=self.colors['danger'],
            fg='white'
        )
        message_label.pack(pady=(0, 20))
        
        info_label = tk.Label(
            result_box,
            text="This system only processes male voices",
            font=('Arial', 10),
            bg=self.colors['danger'],
            fg='#f5f5f5'
        )
        info_label.pack(pady=(0, 15))
    
    def show_age_results(self, result):
        """Show age detection results"""
        result_box = tk.Frame(
            self.result_frame,
            bg=self.colors['success'],
            relief='solid',
            borderwidth=3
        )
        result_box.pack(fill='both', expand=True, padx=10, pady=10)
        
        icon_label = tk.Label(
            result_box,
            text="✅",
            font=('Arial', 40),
            bg=self.colors['success'],
            fg='white'
        )
        icon_label.pack(pady=(15, 10))
        
        title_label = tk.Label(
            result_box,
            text="Analysis Complete",
            font=('Arial', 16, 'bold'),
            bg=self.colors['success'],
            fg='white'
        )
        title_label.pack()
        
        age_label = tk.Label(
            result_box,
            text=f"Detected Age: {result['age']} years",
            font=('Arial', 20, 'bold'),
            bg=self.colors['success'],
            fg='white'
        )
        age_label.pack(pady=(10, 20))
    
    def show_senior_results(self, result):
        """Show results for senior citizens with emotion"""
        result_box = tk.Frame(
            self.result_frame,
            bg=self.colors['senior'],
            relief='solid',
            borderwidth=3
        )
        result_box.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Emotion icons
        emotion_icons = {
            'Happy': '😊',
            'Sad': '😢',
            'Angry': '😠',
            'Neutral': '😐'
        }
        
        emotion_icon = emotion_icons.get(result['emotion'], '🎭')
        
        icon_label = tk.Label(
            result_box,
            text=emotion_icon,
            font=('Arial', 45),
            bg=self.colors['senior']
        )
        icon_label.pack(pady=(15, 5))
        
        title_label = tk.Label(
            result_box,
            text="Senior Citizen Detected",
            font=('Arial', 16, 'bold'),
            bg=self.colors['senior'],
            fg='white'
        )
        title_label.pack(pady=5)
        
        age_label = tk.Label(
            result_box,
            text=f"Age: {result['age']} years",
            font=('Arial', 14, 'bold'),
            bg=self.colors['senior'],
            fg='white'
        )
        age_label.pack(pady=3)
        
        emotion_label = tk.Label(
            result_box,
            text=f"Emotion: {result['emotion']}",
            font=('Arial', 14, 'bold'),
            bg=self.colors['senior'],
            fg='white'
        )
        emotion_label.pack(pady=(3, 20))
    
    def clear_results(self):
        """Clear result display area"""
        for widget in self.result_frame.winfo_children():
            widget.destroy()
    
    def reset(self):
        """Reset the application"""
        self.audio_path = None
        self.file_label.config(
            text="📁 No file selected",
            fg='#7f8c8d',
            bg=self.colors['light']
        )
        self.analyze_btn.config(state='disabled')
        self.clear_results()
        self.progress.stop()
        self.progress.pack_forget()
        print("[GUI] Application reset")
    
    def display_error(self, error_msg):
        """Display error message"""
        self.progress.stop()
        self.progress.pack_forget()
        self.analyze_btn.config(state='normal')
        messagebox.showerror("Error", f"An error occurred:\n\n{error_msg}")

def start_gui():
    """Start the GUI application"""
    root = tk.Tk()
    app = VoiceDetectorGUI(root)
    
    # Center window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    print("Starting GUI in standalone mode...")
    start_gui()

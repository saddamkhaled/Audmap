import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
from audio_processing import load_audio
from audio_processing import perform_fft_parallel
from visualization import display_results
import logging
import traceback
from frequency_analysis import map_to_emotions,extract_acoustic_features




def run_gui():
    """Launch a GUI for audio analysis with enhanced features."""
    def on_select_file():
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("Audio Files", "*.mp3 *.wav")]
            )
            
            if not file_path:
                logging.info("No file selected")
                status_bar.config(text="No file selected")
                return
                
            logging.info(f"Selected file: {file_path}")
            status_bar.config(text="Processing...")

            # Update GUI to show processing status
            console.delete(1.0, tk.END)
            console.insert(tk.END, "Processing audio file...\n", "info")
            console.config(background="black")
            console.config(foreground="white")
        

            # Start progress bar animation
            progress_bar.start()

            try:
                audio, sr = load_audio(file_path)
                
                if len(audio) < sr:  # Less than 1 second of audio
                    raise ValueError("Audio file is too short (less than 1 second)")

                # Display basic file info
                audio_duration = len(audio) / sr
                console.insert(tk.END,f"File path: {file_path}\n","green")
                console.insert(tk.END, f"Sample rate: {sr} Hz\n", "info")
                console.insert(tk.END, f"Duration: {audio_duration:.2f} seconds\n", "info")
                
                
                logging.info("Starting FFT analysis")
                console.insert(tk.END,"Starting audio analysis...\n","info")
                window.update()
                analysis_results = perform_fft_parallel(audio, sr, segment_size=5)
                console.insert(tk.END,"Displaying results...\n","info")
                window.update()

                logging.info("Displaying results")
                
                status_bar.config(text="Analysis completed")
               
                display_emotional_impact(file_path, console)
                display_results(analysis_results, console, segment_size=5, sr=sr)

               
            except Exception as e:
                error_msg = f"Failed to process the audio file:\n{str(e)}"
                logging.error(error_msg)
                messagebox.showerror("Error", error_msg)
                console.insert(tk.END, f"\nError: {str(e)}\n", "error")
                status_bar.config(text="Error during processing")
            finally:
                progress_bar.stop()

        except Exception as e:
            logging.error(f"Unexpected error in GUI: {str(e)}\n{traceback.format_exc()}")
            messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")
            status_bar.config(text="Unexpected error")
            progress_bar.stop()
    def display_emotional_impact(file_path, console):
        """Analyze and display the emotional impact of the audio file."""
        console.insert(tk.END, "\nAnalyzing emotional impact...\n")
        features = extract_acoustic_features(file_path)
        if features:
            console.insert(tk.END, f"Tempo: {features['tempo']:.2f} BPM\n")
            console.insert(tk.END, f"Loudness: {features['loudness']:.5f}\n")
            console.insert(tk.END, f"Spectral Centroid: {features['spectral_centroid']:.2f} Hz\n")
            emotions = map_to_emotions(features)
            console.insert(tk.END, f"Valence: {emotions['valence']}\n")
            console.insert(tk.END, f"Arousal: {emotions['arousal']}\n")
        else:
            console.insert(tk.END, "Failed to analyze emotional impact.\n")
   
            
    def clear_console():
        """Clear the console."""
        console.delete(1.0, tk.END)
        status_bar.config(text="Console cleared")

    def show_about():
        """Display information about the app."""
        messagebox.showinfo("About", "Audio Analyzer\nVersion 1.0\nDeveloped by Saddam Ben Khaled @CaveBenKhaldoun")
    def on_show_emotional_impact():
        """Show emotional impact if a file is selected."""
        file_path = filedialog.askopenfilename(
                filetypes=[("Audio Files", "*.mp3 *.wav")]
            )
        display_emotional_impact(file_path,console) 




    window = tk.Tk()
    window.title("Audio Frequency Analyzer")

    # Configure window size and position
    window_width = 800
    window_height = 600
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Create and pack widgets
    frame = tk.Frame(window, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

   # Create menu frame
    menu_frame = tk.Frame(window, bg="lightgray", padx=5, pady=5)
    menu_frame.pack(fill=tk.X)

    # Create buttons in the menu frame
    select_file_btn = tk.Button(
        menu_frame,
        text="Frequency analysis ",
        command=on_select_file,
        bg="#4CAF50",  # Green background
        fg="white",    # White text
        padx=10,
        pady=5
    )
    select_file_btn.pack(side=tk.LEFT, padx=5)

    display_emotional_impact_btn = tk.Button(
        menu_frame,
        text="Show Emotional Impact",
        command= on_show_emotional_impact,
        bg="#2196F3",  # Blue background
        fg="white",    # White text
        padx=10,
        pady=5
    )
    display_emotional_impact_btn.pack(side=tk.LEFT, padx=5)

    clear_btn = tk.Button(
        menu_frame,
        text="Clear Console",
        command=clear_console,
        bg="#FF5722",  # Orange background
        fg="white",    # White text
        padx=10,
        pady=5
    )
    clear_btn.pack(side=tk.LEFT, padx=5)

    about_btn = tk.Button(
        menu_frame,
        text="About",
        command=show_about,
        bg="#9C27B0",  # Purple background
        fg="white",    # White text
        padx=10,
        pady=5
    )
    about_btn.pack(side=tk.LEFT, padx=5)

    # Console for output
    console = scrolledtext.ScrolledText(
        window,
        wrap=tk.WORD,
        width=80,
        height=20,
        font=("Courier", 10)
    )
    console.pack(fill=tk.BOTH, expand=True, pady=10)

    # Configure text tags
    console.tag_configure("error", foreground="red")
    console.tag_configure("harmful", foreground="red")
    console.tag_configure("non_harmful", foreground="green")
    console.tag_configure("info", foreground="green")

    # Progress bar widget
    progress_bar = ttk.Progressbar(window, mode='indeterminate')
    progress_bar.pack(fill=tk.X, pady=5)

    # Add status bar
    status_bar = tk.Label(
        window,
        text="Ready",
        bd=1,
        relief=tk.SUNKEN,
        anchor=tk.W
    )
    status_bar.pack(fill=tk.X, side=tk.BOTTOM)

    window.mainloop()
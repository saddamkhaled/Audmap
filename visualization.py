# visualization.py
import traceback
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
from constants import  * 
import tkinter as tk
from frequency_analysis import analyze_frequencies, evaluate_emotional_impact

def display_results(analysis_results, console, segment_size=5, sr=44100):
    """Display results in the GUI console and plot the frequency spectrum for all segments."""
    plt.figure(figsize=(12, 6))


        # Initialize counters for tuning and brainwave checks
    tuning_432 = 0
    tuning_440 = 0
    harmful_count = 0
    non_harmful_count = 0
    for idx, (frequencies, magnitude) in enumerate(analysis_results):
        positive_freqs = frequencies[frequencies >= 0]
        positive_magnitude = magnitude[frequencies >= 0]

        color = plt.cm.jet(idx / len(analysis_results))
        plt.plot(positive_freqs, positive_magnitude, color=color, label=f"Segment {idx + 1}")

        dominant_freq_index = np.argmax(positive_magnitude)
        dominant_freq = positive_freqs[dominant_freq_index]
        dominant_magnitude = positive_magnitude[dominant_freq_index]

        is_harmful = not any(low <= dominant_freq <= high for low, high in brainwave_ranges.values())
        segment_start_time = idx * segment_size

        dominant_freq_message = f"Dominant Frequency: {dominant_freq:.2f} Hz "
        dominant_time_message = f"Time: {segment_start_time // 60:.0f}m {segment_start_time % 60:.0f}s"

        if is_harmful:
            harmful_count += 1
            console.insert(tk.END, f"\n{dominant_freq_message} at {dominant_time_message}\n", "harmful")
            
        else:
            non_harmful_count += 1
            console.insert(tk.END, f"\n{dominant_freq_message} at {dominant_time_message}\n", "non_harmful")

        if abs(dominant_freq - 432) < 1:
            tuning_432 += 1
        elif abs(dominant_freq - 440) < 1:
            tuning_440 += 1

        console.insert(tk.END, f"\nSegment {idx + 1}:\n")
        solfeggio_matches, brainwave_matches = analyze_frequencies(positive_freqs, positive_magnitude)
        console.insert(tk.END, "Solfeggio Frequency Matches:\n")
        for freq in solfeggio_matches:
            console.insert(tk.END, f"  Detected solfeggio frequency: {freq:.2f} Hz\n")

        console.insert(tk.END, "\nBrainwave Matches:\n")
        for name, matches in brainwave_matches.items():
            if matches:
                console.insert(tk.END, f"  {name} wave matches: {', '.join(f'{freq:.2f} Hz' for freq in matches)}\n")
        
        evaluate_emotional_impact(brainwave_matches, solfeggio_matches, console)

        # Update solfeggio summary
        for freq in solfeggio_frequencies:
            if any(abs(f - freq) < 1 for f in positive_freqs[np.where(positive_magnitude > np.max(positive_magnitude) * 0.05)]):
                solfeggio_summary[freq]['count'] += 1
                solfeggio_summary[freq]['duration'] += segment_size  # Each segment contributes `segment_size` seconds

        # Update brainwave summary
        for name, (low, high) in brainwave_ranges.items():
            matches = [f for f in positive_freqs if low <= f <= high]
            if matches:
                brainwave_summary[name]['count'] += len(matches)
                brainwave_summary[name]['duration'] += segment_size  # Each segment contributes `segment_size` seconds


    plt.title("Combined Frequency Spectrum (All Segments)")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    plt.xlim(0, 2000)
    plt.legend()
    plt.grid(True)
    plt.show()


import logging
import traceback
import numpy as np
from constants import *
from scipy.signal import butter, lfilter
import tkinter as tk
from scipy.signal import find_peaks

def bandpass_filter(data, lowcut, highcut, fs, order=4):
    """Apply a bandpass filter to the data."""
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y
def butter_bandpass(lowcut, highcut, fs, order=4):
    """Design a bandpass filter using Butterworth."""
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    return b, a
def analyze_segment(audio, sr, i, segment_samples):
    """Analyze a single audio segment."""
    try:
        segment = audio[i * segment_samples:(i + 1) * segment_samples]
        filtered_segment = bandpass_filter(segment, 20, 20000, sr)
        fft_result = np.fft.fft(filtered_segment)
        frequencies = np.fft.fftfreq(len(segment), 1 / sr)
        magnitude = np.abs(fft_result)
        return frequencies, magnitude
    except Exception as e:
        logging.error(f"Error analyzing segment {i}: {e}")
        traceback.print_exc()
        raise e

def analyze_frequencies(frequencies, magnitude):
    """Analyze frequencies and determine matches with solfeggio and brainwave ranges."""
    try:
        detected_frequencies = frequencies[np.where(magnitude > np.max(magnitude) * 0.05)]

        # Check for matches with solfeggio frequencies
        solfeggio_matches = [freq for freq in detected_frequencies if any(abs(freq - sf) < 1 for sf in solfeggio_frequencies)]

        # Check for brainwave alignments
        brainwave_matches = {}
        for name, (low, high) in brainwave_ranges.items():
            brainwave_matches[name] = [freq for freq in detected_frequencies if low <= freq <= high]

        return solfeggio_matches, brainwave_matches
    except Exception as e:
        logging.error(f"Error analyzing frequencies: {e}")
        traceback.print_exc()
        raise e
def evaluate_emotional_impact(brainwave_matches, solfeggio_matches, console):
    """Evaluate and log the emotional impact based on detected frequencies."""
    try:
        for freq in solfeggio_matches:
            if freq in solfeggio_emotional_impact:
                impact = solfeggio_emotional_impact[freq]
                console.insert(tk.END, f"  Emotional Impact of {freq} Hz: {impact}\n")
    except Exception as e:
        logging.error(f"Error evaluating emotional impact: {e}")
        traceback.print_exc()

    """Evaluate and display potential emotional impact."""
    if brainwave_matches:
        console.insert(tk.END, "\nEstimated Emotional Impact:\n")
        for name, matches in brainwave_matches.items():
            if matches:
                if name == 'Delta':
                    console.insert(tk.END, "- Delta waves detected: May induce deep sleep and rest.\n")
                elif name == 'Theta':
                    console.insert(tk.END, "- Theta waves detected: Associated with relaxation and creativity.\n")
                elif name == 'Alpha':
                    console.insert(tk.END, "- Alpha waves detected: Associated with calmness and relaxed alertness.\n")
                elif name == 'Beta':
                    console.insert(tk.END, "- Beta waves detected: May promote focus and alertness.\n")
                elif name == 'Gamma':
                    console.insert(tk.END, "- Gamma waves detected: Associated with heightened cognition and mental clarity.\n")
    else:
        console.insert(tk.END, "No brainwave patterns detected that align with known ranges.\n")
    
    if solfeggio_matches:
        console.insert(tk.END, "\nSolfeggio Frequency Emotional Impact:\n")
        for freq in solfeggio_matches:
            rounded_freq = round(freq)
            if rounded_freq in solfeggio_emotional_impact:
                impact = solfeggio_emotional_impact[rounded_freq]
                console.insert(tk.END, f"  {rounded_freq} Hz detected: {impact}\n")

  # Display solfeggio summary in the console
    console.insert(tk.END, "\nSolfeggio Frequency Summary:\n")
    for freq, data in solfeggio_summary.items():
        if data['count'] > 0:
            console.insert(tk.END, f"  {freq} Hz was detected {data['count']} times with a total of {data['duration']} seconds of listening.\n")

    # Display brainwave summary in the console
    console.insert(tk.END, "\nBrainwave Frequency Summary:\n")
    for name, data in brainwave_summary.items():
        if data['count'] > 0:
            console.insert(tk.END, f"  {name} wave detected {data['count']} times with a total of {data['duration']} seconds of listening.\n")

    # Determine the tuning and display it
    if tuning_432 > tuning_440:
        console.insert(tk.END, "\nThe music is tuned to 432 Hz.\n")
    elif tuning_440 > tuning_432:
        console.insert(tk.END, "\nThe music is tuned to 440 Hz.\n")
    else:
        console.insert(tk.END, "\nUnable to determine if the music is tuned to 432 Hz or 440 Hz.\n")

    # Display harmful or non-harmful status based on the count
    if harmful_count > non_harmful_count:
        console.insert(tk.END, "\nThe audio is more likely to be harmful to the human body and brain.\n")
    else:
        console.insert(tk.END, "\nThe audio is not harmful to the human body and brain.\n")




def calculate_loudness(audio):
    """Calculate the loudness (RMS) of an audio signal."""
    rms = np.sqrt(np.mean(audio**2))
    return rms

def calculate_tempo(audio, sr):
    """Estimate the tempo of an audio signal."""
    envelope = np.abs(audio)
    peaks, _ = find_peaks(envelope, distance=sr // 2)  # Peaks separated by ~0.5 seconds
    peak_intervals = np.diff(peaks) / sr  # Convert intervals to seconds
    if len(peak_intervals) == 0:
        return 0  # No tempo detected
    avg_interval = np.mean(peak_intervals)
    tempo = 60 / avg_interval  # Convert interval to BPM
    return tempo

def calculate_spectral_centroid(audio, sr):
    """Calculate the spectral centroid of an audio signal."""
    fft_result = np.fft.fft(audio)
    frequencies = np.fft.fftfreq(len(fft_result), 1 / sr)
    magnitude = np.abs(fft_result)
    positive_freqs = frequencies[frequencies >= 0]
    positive_magnitude = magnitude[:len(positive_freqs)]
    spectral_centroid = np.sum(positive_freqs * positive_magnitude) / np.sum(positive_magnitude)
    return spectral_centroid

def extract_acoustic_features(audio_file):
    """Extract acoustic features like tempo, loudness, and spectral centroid."""
    try:
        from audio_processing import load_audio
        audio, sr = load_audio(audio_file)
        loudness = calculate_loudness(audio)
        tempo = calculate_tempo(audio, sr)
        spectral_centroid = calculate_spectral_centroid(audio, sr)
        return {
            'tempo': tempo,
            'loudness': loudness,
            'spectral_centroid': spectral_centroid,
        }
    except Exception as e:
        logging.error(f"Error extracting acoustic features: {e}")
        return None

def map_to_emotions(features):
    """Map acoustic features to emotional dimensions (valence and arousal)."""
    if features is None:
        return {"valence": "Unknown", "arousal": "Unknown"}
    tempo = features['tempo']
    loudness = features['loudness']
    spectral_centroid = features['spectral_centroid']
    arousal = " High energy (excited) " if tempo > 120 or loudness > 0.03 else "Low energy (calm)"
    valence = "Positive (happy)" if spectral_centroid > 3000 else " Negative (sad)"
    return {"valence": valence, "arousal": arousal}

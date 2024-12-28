<<<<<<< HEAD
# Audmap
=======
# Audmap - Advanced Audio Analysis Application

![image](https://github.com/user-attachments/assets/911bcfca-5ab0-4490-9307-23c7dbe8b11e)

## Introduction
Audmap is an advanced audio analysis application designed to analyze audio files by identifying their dominant frequencies, calculating their emotional impact, and providing interactive visualizations and psychoacoustic analysis. It allows users to better understand the sound characteristics and the emotional impact of sound.

## 1. Objectives
- Analyze audio files (.mp3 and .wav).
- Identify dominant frequencies and match them with brainwave frequencies and Solfeggio frequencies.
- Calculate the emotional impact based on acoustic features.
- Visualize the frequency spectra of audio segments.
- Provide an intuitive user interface with buttons for analysis, emotional impact, and file management.

## 2. Features

### Audio Analysis
- Load audio files of various formats (.mp3, .wav).
- Segment the audio and apply Fast Fourier Transform (FFT) analysis.
- Identify the dominant frequencies and their correspondences with:
  - Brainwave ranges (Alpha, Beta, Gamma, Delta, Theta).
  - Solfeggio frequencies.

### Emotional Impact
- Calculate acoustic characteristics:
  - Tempo (BPM).
  - Spectral centroid (pitch).
  - Loudness (RMS intensity).
- Map the acoustic characteristics to emotional dimensions:
  - Valence: Positive or negative.
  - Arousal: High (energetic) or low (calm).

### Visualization
- Display frequency spectra in interactive charts.
- Visual summary of dominant frequencies.

### User Interface
- Graphical User Interface (GUI) with:
  - Frequency analysis.
  - Emotional impact display.
  - Console cleanup.
  - About (Information about the app).
  - Status bar to show progress.
  - Menu bar to group features.

## 3. Constraints

### Technical Requirements
- Use the following Python libraries:
  - `tkinter` for the graphical interface.
  - `numpy`, `scipy` for audio data processing.
  - `matplotlib` and `plotly` for visualization.
  - `Docker` for deployment.

### Performance
- Real-time analysis for audio files less than 10 minutes in duration.

## 4. Program Architecture

### Modules
- **audio_processing.py**: Load and preprocess audio files.
- **frequency_analysis.py**: Frequency analysis and matching.
- **visualization.py**: Generate visualizations.
- **gui.py**: User interface.
- **constants.py**: Constants for brainwave and Solfeggio frequencies.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/audmap.git
>>>>>>> b2fed8d565a594840a2b7dcb69aff2ba5f1d2656

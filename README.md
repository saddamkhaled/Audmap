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
   git clone https://github.com/saddamkhaled/audmap.git


This project is a Python-based application that uses **Tkinter** for GUI, **FFmpeg** for multimedia processing, and other Python libraries for audio analysis and visualization. The application is containerized using Docker for easy setup and deployment.

## Requirements

Before setting up the application, make sure you have the following installed:

- **Docker**: To run the application in a containerized environment.
- **X11 Server** (for Linux users): To display the GUI. For macOS or Windows users, you may need to install and configure **XQuartz** or **Xming** respectively.

For **Linux users**, ensure that you have an X server running and access is granted for Docker containers.

### Optional:
- **Python 3.10**: If you prefer to run the application outside of Docker.

## Installation

### Option 1: Using Docker (Recommended)

#### Step 1: Install Docker
Follow the instructions on the [official Docker website](https://docs.docker.com/get-docker/) to install Docker on your system.

#### Step 2: Clone the Repository
Clone the project repository to your local machine:

```bash
git clone https://github.com/saddamkhaled/audmap.git
cd Audmap
```

#### Step 3: Build the Docker Image
Build the Docker image using the provided `Dockerfile`:

```bash
sudo docker build -t audmap:latest .
```

#### Step 4: Allow Docker to Access Your Display (Linux only)
Run the following command to grant Docker permission to access the display (if you're on a Linux machine):

```bash
xhost +local:docker
```

#### Step 5: Run the Application
Run the container with the necessary environment variables and volume mounts:

```bash
sudo docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix audmap:latest
```

This will start the application, and the GUI should appear on your screen.

### Option 2: Installing without Docker (Optional)

If you prefer to run the application without Docker, you can set up the environment manually:

#### Step 1: Install Python 3.10
Make sure Python 3.10 or a compatible version is installed. You can download it from [here](https://www.python.org/downloads/).

#### Step 2: Install Dependencies
Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

Additionally, you may need to install system-level dependencies:

For Ubuntu/Debian-based systems:

```bash
sudo apt-get install python3-tk ffmpeg
```

#### Step 3: Run the Application
Run the main Python script:

```bash
python main.py
```

### Troubleshooting

- **"Couldn't connect to display" error**: Make sure your `DISPLAY` environment variable is set correctly. If you're running on a remote server, you'll need to configure an X server or use virtual display methods like Xvfb or VNC.
- **X11-related issues on Wayland**: If you're using Wayland instead of X11, you might encounter compatibility issues. Ensure that XWayland is installed, or use a VNC/X server solution.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---


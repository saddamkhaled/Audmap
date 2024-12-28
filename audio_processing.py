# audio_processing.py
import multiprocessing
import traceback
import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment
import logging
from frequency_analysis import analyze_segment




def load_audio(file_path):
    """Load an audio file and return the audio time series and sampling rate."""
    try:
        if file_path.lower().endswith('.mp3'):
            audio = AudioSegment.from_file(file_path, format="mp3")
            audio = audio.set_channels(1)  # Convert to mono
            audio = audio.set_frame_rate(44100)  # Standardize sampling rate
            sr = audio.frame_rate
            samples = np.array(audio.get_array_of_samples(), dtype=np.float32)
        elif file_path.lower().endswith('.wav'):
            sr, samples = wavfile.read(file_path)
            if samples.ndim > 1:
                samples = samples.mean(axis=1)  # Convert to mono if stereo
        else:
            raise ValueError("Unsupported file format. Please use MP3 or WAV files.")
        return samples, sr
    except Exception as e:
        logging.error(f"Failed to load audio file {file_path}: {e}")
        raise e
    

def perform_fft_parallel(audio, sr, segment_size=5):
    """Perform FFT analysis in parallel for audio segments."""
    try:
        segment_samples = int(segment_size * sr)
        num_segments = len(audio) // segment_samples
        pool = multiprocessing.Pool()

        # Map the analyze_segment function over each segment index
        analysis_results = pool.starmap(
            analyze_segment, [(audio, sr, i, segment_samples) for i in range(num_segments)]
        )

        pool.close()
        pool.join()
        return analysis_results
    except Exception as e:
        logging.error(f"Error in parallel FFT processing: {e}")
        traceback.print_exc()
        raise e
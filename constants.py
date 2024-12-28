
# Set up logging
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# List of solfeggio frequencies for comparison
solfeggio_frequencies = [174, 285, 396, 417, 528, 639, 741, 852, 963 , 1296]

# Mapping solfeggio frequencies to their emotional and physical effects
solfeggio_emotional_impact = {
    174: "May reduce pain and promote a sense of security.",
    285: "Associated with tissue regeneration and healing minor wounds.",
    396: "Linked to releasing guilt and fear.",
    417: "Facilitates change and helps undo difficult situations.",
    528: "Known for DNA repair and transformation; brings miracles.",
    639: "Encourages harmonious relationships and communication.",
    741: "Aids in problem-solving and emotional stability.",
    852: "Promotes returning to spiritual order and clarity.",
    963: "Associated with awakening intuition and higher consciousness.",
    1074: "Deep Relaxing, Intuition Boost.",
    1185: "Higher Realms Connections, Laser Focus.",
    1296: "Life Balancing, Well-being and Growth."
}

# Brainwave frequency ranges (in Hz)
brainwave_ranges = {
    'Delta': (0.5, 4),
    'Theta': (4, 8),
    'Alpha': (8, 14),
    'Beta': (14, 30),
    'Gamma': (30, 100)
}

# Brainwave summary dictionary structure
brainwave_summary = {
    'Delta': {'count': 0, 'duration': 0},
    'Theta': {'count': 0, 'duration': 0},
    'Alpha': {'count': 0, 'duration': 0},
    'Beta': {'count': 0, 'duration': 0},
    'Gamma': {'count': 0, 'duration': 0},
}

# Solfeggio summary dictionary structure
solfeggio_summary = {freq: {'count': 0, 'duration': 0} for freq in solfeggio_frequencies}

  # Initialize counters for tuning and brainwave checks
tuning_432 = 0
tuning_440 = 0
harmful_count = 0
non_harmful_count = 0
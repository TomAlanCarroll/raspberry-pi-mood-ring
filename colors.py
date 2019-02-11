import operator

RED = 'red'
BLACK = 'black'
CYAN = 'cyan'
ORANGE = 'orange'
GREY = 'grey'
MAGENTA = 'magenta'
TAN = 'tan'
YELLOW = 'yellow'
PURPLE = 'purple'
GREEN = 'green'
WHITE = 'white'

mood_ring_colors = {
    RED: '#D80000',  # energized, excited, adventurous
    BLACK: '#000000',  # stressed, nervous, tense
    CYAN: '#00FFFF',  # calm, relaxed
    ORANGE: '#FF9900',  # unsettled, mixed emotions
    GREY: '#080808',  # very nervous, anxious, sad
    MAGENTA: '#FF00FF',  # fearful, uncertain
    TAN: '#D2B48C',  # restless
    YELLOW: '#FFFF00',  # imaginative
    PURPLE: '#660066',  # happy
    GREEN: '#339933',  # average
    WHITE: '#FFFFFF',  # bored
}

termcolor_colors = [
    GREY,
    RED,
    GREEN,
    YELLOW,
    'blue',  # blue is more of a purple color in termcolor
    MAGENTA,
    CYAN,
    WHITE,
]


def face_emotions_to_color(emotions):
    """
    Maps an emotion dictionary from Azure Face API response to a corresponding color
    "emotion": {
        "anger": 0.0,
        "contempt": 0.0,
        "disgust": 0.0,
        "fear": 0.0,
        "happiness": 1.0,
        "neutral": 0.0,
        "sadness": 0.0,
        "surprise": 0.0
      },
    :param emotions: Emotion dict from Azure Face API response
    :return: Tuple: (Emotion name, the color to illuminate)
    """
    # "anger"  RED
    # "contempt"  BLACK
    # "disgust"  YELLOW
    # "fear" MAGENTA
    # "happiness" PURPLE
    # "neutral" GREEN
    # "sadness" GREY
    # "surprise" ORANGE

    # TODO: Use combinations of emotions to map more colors
    highest_confidence_emotion = max(emotions.items(), key=operator.itemgetter(1))[0]
    if highest_confidence_emotion == 'anger':
        return RED
    elif highest_confidence_emotion == 'contempt':
        return BLACK
    elif highest_confidence_emotion == 'disgust':
        return YELLOW
    elif highest_confidence_emotion == 'fear':
        return MAGENTA
    elif highest_confidence_emotion == 'happiness':
        return PURPLE
    elif highest_confidence_emotion == 'neutral':
        return GREEN
    elif highest_confidence_emotion == 'sadness':
        return GREY
    elif highest_confidence_emotion == 'surprise':
        return ORANGE
    else:
        return None

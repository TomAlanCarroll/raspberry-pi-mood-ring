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
    GREY: '#B3B3B3',  # very nervous, anxious
    MAGENTA: '#FF00FF',  # fearful, uncertain
    TAN: '#D2B48C',  # restless
    YELLOW: '#FFFF00',  # imaginative
    PURPLE: '#660066',  # calm
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
    # TODO: mapping
    return GREEN

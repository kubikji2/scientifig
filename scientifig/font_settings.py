from . import constants
import matplotlib.pyplot

def set_recommended_fonts(fonts=constants.IEEE_FONTS):
    matplotlib.pyplot.rcParams.update(fonts)
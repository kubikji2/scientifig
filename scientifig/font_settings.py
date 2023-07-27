from . import typography_constants
import matplotlib.pyplot

def set_recommended_fonts(fonts=typography_constants.IEEE_FONTS):
    matplotlib.pyplot.rcParams.update(fonts)
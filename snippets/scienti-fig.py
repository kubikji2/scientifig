# CC-0 by JK

# usually, the matplotlib pyplot is referenced as plt
import matplotlib.pyplot as plt
# ... similarly to the numpy
import numpy as np

# set recommended sans-serif fonts
# '-> inspire by DV, MP and JK
tex_fonts = \
{
  # Use LaTeX to write all text
  "text.usetex": True,
  "font.family": "serif",
  # Use 10pt font in plots, to match 10pt font in document
  "axes.labelsize": 10,
  "font.size": 10,
  # Make the legend/label fonts a little smaller
  "legend.fontsize": 8,
  "xtick.labelsize": 8,
  "ytick.labelsize": 8
}
plt.rcParams.update(tex_fonts)

# size relevant constants
IEEE_SINGLE_WIDTH = 7.16 #inches
IEEE_COL_WIDTH = 3.5 #inches
IEEE_FIG_SIZE = (IEEE_COL_WIDTH, IEEE_COL_WIDTH) #modify for text width cols
FIG_SIZE = IEEE_FIG_SIZE
FIG_SIZE_HALVED = (FIG_SIZE[0],0.5*FIG_SIZE[0])

if __name__=="__main__":

  fig, ax = plt.subplots(figsize=FIG_SIZE)
  
  # TODO your stuff here

# size relevant constants
IEEE_SINGLE_COL_WIDTH = 7.16 # inches
IEEE_DOUBLE_COL_WIDTH = 3.5 # inches
IEEE_FIG_SIZE = (IEEE_DOUBLE_COL_WIDTH, IEEE_DOUBLE_COL_WIDTH) # modify for text width cols
FIG_SIZE = IEEE_FIG_SIZE
FIG_SIZE_HALVED = (FIG_SIZE[0], 0.5*FIG_SIZE[0])

THESIS_WIDTH = 6.15 # inches  # 6.14293 # inches

# set recommended sans-serif fonts
# '-> inspire by DV, MP and JK
IEEE_FONTS = \
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


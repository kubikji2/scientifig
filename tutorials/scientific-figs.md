# Knowledge Scroll on Scientific Figs

This scroll summarizes accumulated knowledge considering the visual data presentation for scientific focus forums such as conference papers and journals using mainly the [matplotlib](https://matplotlib.org/) library in python programming languages.
Though mainly focused on scientific papers, the tips can be used for writing general scientific texts such as theses.

## General Tips

- Label your axis, include the units
  - The title is usually omitted since the figure caption replaces it
  - Use different ticks resolution and labels; see [[xtick documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html), [[ytick documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yticks.html)
  - Use log-axis in case of orders-of-magnitude differences; see [[xscale documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xscale.html), [[yscale documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.yscale.html)
  - You can enable (basic) LaTeX syntax in the plot using *raw string literals* denoted as `r'some raw string'`
    - such as `r'\theta~[rad]'` resulting in $\theta~[rad]$, [[advanced reading]](https://matplotlib.org/stable/tutorials/text/usetex.html) and [[examples]](https://matplotlib.org/stable/gallery/text_labels_and_annotations/tex_demo.html)

- Place legend to your plot
  - Place legend to an empty area in your fig to save up space; see [[legend documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html) for possible locations
  - If multiple subplots share a single legend, use `bbox_to_anchor=(x, y, width, height)` to move it above/below the plots
  - It is possible to select only particular lines in the plot to be added to the legend; see `handles` and `labels` in [[legend documentation]](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)
  - It is possible to label your plotted data using the `label` argument
    - e.g., `ax.plot([1, 2, 3], label='my label')`
- Use appropriate color maps for particular data types; see [[Choosing Colormaps in Matplotlib]](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
  - For continuous data, always use perceptually uniform color maps such as *viridis*, *plasma*, and *inferno*
    - avoid *jet*, *turbo*, or *rainbow*
  - Do not combine multiple color maps in each color map category unless explainable
  - Unify the color meaning for qualitative color maps
    - e. g. blue is a baseline model, yellow is an approach 1, green approach 2, etc.

- Fit the figure size to the size in the paper
  - It is easier to tune the parameters directly in your script
  - Most paper templates have specified columns dimensions
    - e.g., the IEEE double-column has a width of 3.5 inches, and the IEEE single-column has a width of 7.16 inches[^1]
    - see `utils` TODO constants references

- Use serif font to fit the fonts used in the paper; see the example below
  - Normal size (`\normalsize`) is 10, size 8 is (`\footnotesize`) for 10pt documents such as usual IEEE templates[^2]
  - Recommended font follows:

    ```python
    font = \
    {
      'family' : 'serif',
      'weight' : 'medium',
      'size'   : 8
    }
    plt.rc('font', **font)
    ```

  - Alternatively, one can use different font sizes for different figure labels as suggested by DV [^3]
  
    ```python
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
    ```

  - NOTE: using `.pgf` (~translationto the LaTeX syntax) lengthens the compilation, and untranslatable segments are exported as undesirable raster images with absolute paths

- Some individuals prefer to remove the figure frame for particular plots; see [[spines documentation]](https://matplotlib.org/stable/api/spines_api.html)
  - e.g., to remove left spine use `ax.spines['left'].set_visible(False)`

[^1]:  Resolution and Size in IEEE Author Center [[link]](https://journals.ieeeauthorcenter.ieee.org/create-your-ieee-journal-article/create-graphics-for-your-article/resolution-and-size/)

[^2]: TeX stackexchange [[link]](https://tex.stackexchange.com/questions/24599/what-point-pt-font-size-are-large-etc)

[^3]: Plot publication-quality figures with matplotlib and LaTeX [[link]](https://jwalton.info/Embed-Publication-Matplotlib-Latex/)

## Figure Snippet

Python snippet implementing universally applicable tips and tricks from above.
This file is also located in `snippets/scienti-fig.py`.

```python
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

```

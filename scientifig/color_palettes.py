import matplotlib.cm

# improved interface for qualitative color maphs matplotlib colormap
def get_clr(color_index, dark=True, alpha=1, cmap_name="tab20"):
    # get color map from color maps
    _cmap = matplotlib.cm.get_cmap(cmap_name)
    # define possible shade increment
    _shade_incr = 0 if dark else 1
    # get particular color from the color map
    c = _cmap((2*color_index + _shade_incr)/20)
    # one-liner that extract RGB from color-tuple, add alpha channel, make it tuple again and return
    return tuple([*c[0:3],alpha])

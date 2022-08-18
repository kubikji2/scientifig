import matplotlib.cm

from . import color_constants

# register ctu8 color map
matplotlib.cm.register_cmap( \
        name=color_constants.CTU8_CM_NAME, \
        cmap=matplotlib.colors.ListedColormap( \
            color_constants.CTU8_LIST, \
            name=color_constants.CTU8_CM_NAME \
        ) \
    )

# covert index into color using colormap and alpha
def __idx2clr(cmap, idx, alpha):
    # get particular color from the color map   
    c = cmap((idx%cmap.N)/cmap.N)
    # one-liner that extract RGB from color-tuple, add alpha channel, make it tuple again and return
    return tuple([*c[0:3],alpha])

# improved interface for qualitative color maphs matplotlib colormap
def get_clr(color_index, dark=True, alpha=1, cmap_name="tab20"):
    # get color map from color maps
    _cmap = matplotlib.cm.get_cmap(cmap_name)
    # define possible shade increment
    _shade_incr = 0 if dark else 1
    return __idx2clr(_cmap, 2*color_index + _shade_incr, alpha)

# color map based on CTU_blue
def get_ctu8_clr(color_index, alpha=1):
    
    # try to get color map from known color maps ...
    try:
        _cmap = matplotlib.cm.get_cmap(color_constants.CTU8_CM_NAME)
    except ValueError:
        # ... if fails add it
        matplotlib.cm.register_cmap( \
            name=color_constants.CTU8_CM_NAME, \
            cmap=matplotlib.colors.ListedColormap( \
                color_constants.CTU8_LIST, \
                name=color_constants.CTU8_CM_NAME \
            ) \
        )
        _cmap = matplotlib.cm.get_cmap(color_constants.CTU8_CM_NAME)
    
    # return converted version
    return __idx2clr(_cmap, color_index, alpha)
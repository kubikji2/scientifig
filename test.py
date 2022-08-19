from difflib import Match
from itertools import product
import matplotlib.pyplot as plt

from scientifig import color_constants, color_maps
from scientifig import font_settings

if __name__=="__main__":
    col = color_maps.get_clr(1)
    print(col)
    """
    font_settings.set_recommended_fonts()
    for axi in range(8):
        plt.plot([i for i in range(0,10)], [2*i + 2*i*i - axi*(i-5) for i in range(0,10)], color=color_maps.get_clr(axi))
    plt.xlabel(r" $\varphi$ [some units]")
    plt.ylabel(r" $\partial\Pi$ [some other units]")
    plt.show()
    """
    import matplotlib.cm as cm
    import matplotlib.colors
    import numpy as np
    print(cm.get_cmap('Oranges_r', 128)(0))
    newcolors = np.asarray([tuple(clr) for clr in product([0,1],[0,1],[0,1],[1])])
    newcolors = color_constants.CTU20_LIST
    new_cm = matplotlib.colors.ListedColormap(newcolors, name='test')
    cm.register_cmap(name="ctu",cmap=new_cm)
    #color_maps.get_clr(axi,cmap_name="ctu")
    font_settings.set_recommended_fonts()
    for axi in range(8):
        plt.plot([i for i in range(0,10)], [2*i + 2*i*i - axi*(i-5) for i in range(0,10)], color=color_maps.get_ctu8_clr(axi), linewidth=3)
    plt.xlabel(r" $\varphi$ [some units]")
    plt.ylabel(r" $\partial\Pi$ [some other units]")
    plt.show()

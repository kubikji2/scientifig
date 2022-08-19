# Perceptually pleasible colors derived from CTU blue [1] aka Pantone 300 C [2] using Paletton [3]
# - [1] https://www.cvut.cz/sites/default/files/content/e254fb38-e72d-463b-8c9f-cb0435416f29/cs/20201112-graficky-manual-identity-cvut-v-praze.pdf
# - [2] https://icolorpalette.com/color/pantone-300-c
# - [3] https://paletton.com/#uid=13-0u0k++BBy7ZHZD+V+WrG+glw

CTU_BLUE_HEX = "0x005EB8" # defined by CTU
CTU_ORANGE_HEX = "0xFF9700" # complementary color to CTU_Blue
CTU_RED_HEX_b = "0xFF1300" # red at 135 deg, bright
CTU_RED_HEX = "0xFF2C00" # red at 140 deg
CTU_GREEN_HEX_b = "Ox00CF24" # green at 135 deg, bright
CTU_GREEN_HEX = "0x00C64A" # green at 140 deg
CTU_PURPLE_HEX = "0x7300BC" # purple at 70 deg
CTU_YELLOW_HEX = "0xFFFC00" # yellow at 70 deg
CTU_CYAN_HEX = "0x00B1A4" # cyan at -20 deg
CTU_OLIVE_HEX = "0xA7F200" # olive at -80 deg
#CTU_PINK_HEX = "0xD40081" # pink at 100 deg
CTU_PINK_HEX = "0xFF009B" # pink at 100 deg

# Hand tuned colors with the base saturation (with the exception of pink that is a bit brighter)
CTU_CYAN_HEX_alt = "0x00B29F" # hand tuned
CTU_PURPLE_HEX_alt = "0x7C00BC" # hand tuned
CTU_PINK_HEX_alt = "0xF65AB5" # hand tuned
CTU_YELLOW_HEX_alt = "0xFFD900" # hand tuned

"""
# tab20c/tab10c-like color alternatative
CTU_LIST_HEX =  \
                [
                    CTU_BLUE_HEX,
                    CTU_ORANGE_HEX,
                    CTU_GREEN_HEX,
                    CTU_RED_HEX,
                    CTU_PURPLE_HEX,
                    "0x000000",
                    CTU_PINK_HEX,
                    "0x000000",
                    CTU_OLIVE_HEX,
                    CTU_CYAN_HEX,
                ]
"""

# two quadruples of alternating colors
# '-> very loosely inspired by 'tab10c' sequential color map
CTU_LIST_HEX =  \
                [
                    CTU_BLUE_HEX,
                    CTU_ORANGE_HEX,
                    CTU_GREEN_HEX,
                    CTU_RED_HEX,
                    CTU_PURPLE_HEX_alt,
                    CTU_YELLOW_HEX_alt,
                    CTU_CYAN_HEX_alt,
                    CTU_PINK_HEX_alt,
                    "0x000000",
                    "0x000000",
                ]

# duplication basic ctu color map
# '-> TODO add brighter alternatibe to each color
#     '-> it would require different iteration
CTU20_LIST_HEX = [ c for c in CTU_LIST_HEX for _ in [c,c]]

# this 'private' method convert hexadecimal representation to the color represetation used by MatPlotLib
# '-> TODO make umprove it 
def __clr_hex2clr(_hex):
    c = []
    # converting each digit pairs to separate color
    for i in range(1,4):
        _comp = int(_hex[2*i:2*i+2], base=16)/255.0
        c.append(_comp)
    # adding alpha at full opacity
    c.append(1)
    # converting to tuple to meet the required representation
    return tuple(c)

# CTU 20 color list
# '-> NOTE: not finished
CTU20_LIST = [__clr_hex2clr(_hex) for _hex in CTU20_LIST_HEX]

# CTU 16 color list
# '-> NOTE: not finished
CTU16_CM_NAME = "ctu16"
CTU16_LIST = CTU20_LIST[0:16]

# CTU 8 color list
# '-> NOTE: kinda finished
CTU8_CM_NAME = "ctu8"
CTU8_LIST = [__clr_hex2clr(_hex) for _hex in CTU_LIST_HEX[0:8]]

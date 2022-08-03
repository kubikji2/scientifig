# Color Maps notes

Where to start:

- Different color maps categories used in matplotlib are explained and listed here [[link]](https://matplotlib.org/stable/tutorials/colors/colormaps.html)
- **Never use non-perceptual uniform color maps** they are confusing

## CTU sequential color map

- start from CTU blue `#005eb8` aka Pantone 300 [[link]](https://icolorpalette.com/color/pantone-300-c)
- use Hue-ChromaLuminance (HCL) color space[^1] to create perceptually uniform sequential color map (colors are perceptually equally distant from each other)
- use [paletton.com](https://paletton.com/) to interpolate in Hue angle and select appropriate range
  - see [[link]](https://paletton.com/#uid=13-0u0k++BBy7ZHZD+V+WrG+glw)
- [ ] find which format is used by python
- [ ] export colors from paletton.com
- [ ] create color palette

[^1]: source [[link]](https://medium.com/nightingale/color-in-a-perceptual-uniform-way-1eebd4bf2692)
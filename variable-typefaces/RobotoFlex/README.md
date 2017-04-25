# RobotoFlex
- demo to test the capabilities of the new fontformat
- work in progress

Preview in [Fontview](https://github.com/googlei18n/fontview/releases):
![robotoflex preview](preview.gif)

## Current Design Master
- Regular
	- Light
		- Height
		- Diacritics
		- Baselineshift
		- Mono			  
	  	- MonoFaux
	  	- Curvature
	  	- CurvatureEqual
	  	- nWidth
	- Bold
    		- RoundCorners
		- Tight

## Features currently missing in the font format
- per-glyph-interpolation axes (the height-sub-axes are currently achieved by a workaround)
- math for the slider behaviour to increase usability (e.g. to make the faux-mono-axis a child of the mono-axis, to prevent strange results if both are applied) 

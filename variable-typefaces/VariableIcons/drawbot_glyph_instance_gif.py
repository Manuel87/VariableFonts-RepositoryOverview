from GlyphsApp import *
import objc
GSInstance = objc.lookUpClass("GSInstance")
GSInterpolationFontProxy = objc.lookUpClass("GSInterpolationFontProxy")

#fill(0.2, 0.2)
myFont = Glyphs.font
selectedLayers = myFont.selectedLayers

import math # for cos, sin and pi functions

# static variables
canvas = 512 # size of the gif in pixels
num_frames = 1  # number of frames in the animation
indent = 10
n = 0
fps = 12
fixscale = 0.85#false

indent = canvas / 100 * indent

def new_page(): 
    newPage(canvas, canvas) # new page from canvas variable
    frameDuration(1/fps) # set the dividend to desired FPS (frames per second) 
    #fill(0.2,1) # color of background
    #rect(0, 0, canvas, canvas) # draw the background

n = 0
for thisInstance in myFont.instances:
    new_page()
    #n = n + 1
    #print n
    instanceFont = thisInstance.interpolatedFontProxy
    n = n + 1
    for thisLayer in selectedLayers:
        
        
        instanceGlyph = instanceFont.glyphForName_(thisLayer.parent.name)
        
        instanceLayer = instanceGlyph.layers[instanceFont.fontMasterID()]
        
       # glyphWidth = instanceLayer.width
       # glyphHeight = instanceLayer.bounds.size.height
       # translate(width()/2 - glyphWidth/2, height()/2 - glyphHeight/2)
        
        path = instanceLayer.bezierPath
        
        if n == 1:
            # calculate the width and height of the path
            #minx, miny, maxx, maxy = path.bounds()
            minx = path.bounds().origin.x
            miny = path.bounds().origin.y
            maxx = minx + path.bounds().size.width
            maxy = miny + path.bounds().size.height
        

            w = maxx - minx
            h = maxy - miny
            # calculate the box where we want to draw the path in
            boxWidth = width() - indent * 2
            boxHeight = height() - indent * 2
            # calculate a scale based on the given path bounds and the box
            s = min([boxWidth / float(w), boxHeight / float(h)])
            # translate to the middle
        translate(width()*.5, height()*.5)
            # set the scale
        
        if fixscale != False:
            scale(fixscale)
        else:
            scale(s)
        # translate the negative offset, letter could have overshoot
        translate(-minx, -miny)
        # translate with half of the width and height of the path
        translate(-w*.5, -h*.5)
        
        drawPath(path)
        

    


saveImage("~/Downloads/icon_" + instanceGlyph.name + ".gif")
print "'icon_" + instanceGlyph.name + ".gif' saved"
  
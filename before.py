def rgb_to_hsv(r, g, b):
    maxValue = max(r, g, b)
    minValue = min(r, g, b)

    v = max(r, g, b)

    if v == 0: return 0, 0, 0

    diff = maxValue - minValue
    s = diff/v
    if s == 0: return 0, s, v

    f = 60/diff
  
    if r == maxValue: return ((360+(g-b)*f + 360) % 360, s, v)
    if g == maxValue: return (120 + (b-r)*f, s, v)
    if b == maxValue: return (240 + (r-g)*f, s, v)



def hsv_to_rgb(h, s, v):
    max = v
    min = v-s*v
    diff = max - min
    f = diff/60
    
    if   h < 60:  return (max, h*f+min, min)
    elif h < 120: return (min-(h-120)*f, max, min)
    elif h < 180: return (min, max, (h-120)*f+min)
    elif h < 240: return (min, min-(h-240)*f, max)
    elif h < 300: return ((h-240)*f+min, min, max)
    else:         return (max, min, (min-(h-360)*f))

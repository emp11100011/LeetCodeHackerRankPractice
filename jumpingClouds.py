def jumpingOnClouds(c):
    jumps = 0
    nextCloud = 0
    while nextCloud != len(c)-2:
        if c[nextCloud] == 0 and c[nextCloud + 2] == 0:
            jump = jump + 2
        

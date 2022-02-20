from mimetypes import init
from typing import final
from numpy import mat


def minCost(rows, cols, initR, initC, finalR, finalC, costRows, costCols):
    matRowCol = []
    for irow in range(rows):
        colVal = []
        for jrow in range(cols):
            colVal.append(0)
        matRowCol.append(colVal)

    matRowCol[initR][initC] = 11
    matRowCol[finalR][finalC] = 10
    
    cost = 0
    if (initR + initC) < (finalR + finalC):
        for cRow in range(initR, finalR+1):
            for cCol in range(initC, finalC+1):
                if  (matRowCol[cRow][cCol] != 11) :
                    if cCol == initC:
                        pass
                    matRowCol[cRow][cCol] = costCols[cCol-1]
            if (matRowCol[cRow][initC] != 11):
                if matRowCol[cRow-1][initC] == 11:
                    matRowCol[cRow][initC] = 0 + costRows[cRow-1]
                else:
                    matRowCol[cRow][initC] = matRowCol[cRow-1][initC] + costRows[cRow-1]
        return sum(matRowCol[finalR])
    if (initR + initC) > (finalR + finalC):
        for cRow in range(finalR, initR, -1):
            for cCol in range(finalC, initC, -1),:
                if  (matRowCol[cRow][cCol] != 11) :
                    if cCol == initC:
                        pass
                    matRowCol[cRow][cCol] = costCols[cCol-1]
            if (matRowCol[cRow][initC] != 11):
                if matRowCol[cRow+1][initC] == 11:
                    matRowCol[cRow][initC] = 0 + costRows[cRow-1]
                else:
                    matRowCol[cRow][initC] = matRowCol[cRow+1][initC] + costRows[cRow-1]
        print(matRowCol)
        return sum(matRowCol[finalR])
       


# minCost(3, 3, 1, 2, 0, 0, [2,5], [6,1])
minCost(4, 4, 3, 3, 1, 2, [1, 2, 3], [7,8,9])

# minCost(83, 85, 69, 62, 18, 61, [128, 34, 585, 254, 496, 516, 410, 394, 561, 518, 97, 219, 172, 57, 167, 413, 583, 278, 265, 13, 470, 243, 620, 229, 102, 19, 434, 540, 619, 96, 543, 173, 8, 380, 392, 46, 567, 450, 289, 275, 292, 218, 160, 552, 470, 253, 50, 558, 391, 10, 333, 516, 282, 374, 211, 366, 5, 146, 205, 541, 604, 112, 486, 597, 141, 133, 350, 597, 371, 170, 51, 92, 151, 301, 275, 511, 249, 531, 256, 376, 41, 154], [286, 594, 418, 339, 408, 590, 22, 126, 480, 467, 244, 317, 449, 435, 358, 424, 325, 343, 130, 299, 56, 358, 82, 589, 390, 268, 369, 587, 315, 496, 352, 170, 16, 237, 322, 402, 183, 271, 149, 102, 412, 606, 41, 448, 213, 224, 98, 595, 483, 74, 539, 249, 306, 499, 562, 545, 422, 320, 365, 288, 97, 260, 408, 579, 592, 378, 587, 607, 346, 547, 315, 352, 378, 389, 447, 129, 266, 191, 575, 11, 314, 235, 132, 400])

# expected output = 16357
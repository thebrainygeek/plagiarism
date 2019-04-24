from collections import defaultdict

def getMissionFiles():
    #getting mission files, which are width by length by height, all are the same length
    files = dict()
    #one block on ground
    files[1][0]
    #several disconnected blocks on ground
    files[2] = [[[None, "stone", None, None, "stone", None, None, "stone", None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]]
                ]
    #two level tower
    files[3] =[[[None, None, None, None, "stone", None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]],
                [[None, None, None, None, "stone", None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]],
                ]
    #three level tower
    files[3] =[[[None, None, None, None, "stone", None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]],
                [[None, None, None, None, "stone", None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]],
                [[None, None, None, None, "stone", None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None],
                [None, None, None, None, None, None, None, None, None, None]],
                ]
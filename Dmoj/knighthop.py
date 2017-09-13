def find_path(start_pos, end_pos, path=[]):
    if start_pos == end_pos:
        return path

    if len(path) > 300:
        print "l"
        return path
        quit()

    [xi, yi] = start_pos
    [xf, yf] = end_pos
    path.append(start_pos)

    all_possible = [[xi+1, yi+2], [xi+2, yi+1], [xi+2, yi-1], [xi+1, yi-2], [xi-1, yi-2], [xi-2, yi-1],
                [xi-2, yi+1], [xi-1, yi+2]]
    

    possible = []
    for i in range(len(all_possible)):
        if all_possible[i][0] in range(0,9) and all_possible[i][1] in range(0,9):
            possible.append(all_possible[i])
        
    for i in all_possible:
        e_p = find_path(i, end_pos, path)
        if e_p:
            return e_p

    return None

import sys
sys.setrecursionlimit(1500000000)

from math import pi

def countIntersections(list):
    chords = {}
    intersections = 0

    data = zip(*list)
    for radian, identifier in data:
        chord = identifier.split("_")[1]
        if chord not in chords:
            chords[chord] = []
        chords[chord].append(radian % (2 * pi))

    chordList = chords.values()
    for i, (s1, e1) in enumerate(chordList):
        for s2, e2 in chordList[i + 1:]:
            if s1 < s2 < e1 or s1 < e2 < e1:
                intersections += 1

    return intersections

print(countIntersections([(0.78, 1.47, 1.77, 3.92), ("s_1", "s_2", "e_1", "s_2")]))
print(countIntersections([(0.9, 1.3, 1.70, 2.92), ("s_1", "e_1", "s_2", "e_2")]))





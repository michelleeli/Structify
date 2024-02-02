# Structify

The goal of my algorithm is to properly group the data to analyze the number of intersections
1. I approach the algorithm first by grouping the identifiers into a hash, with a key of the identifier name and the value as a tuple of the starting and ending points. I acheive this by zipping the data and iterating through the data to create a dictionary, simplifying any radians (if they are surpassing 2pi, they are equivalent)

2. I then iterate through the dictionary to find if there are any intersections (if a chord's starting point or ending point is between another chord's starting/ending points). 

    # Note
    The algorithm is written with no equivalencies (ex: s1 < s2 < e1), which does not compare the intersection on the circumference of the circle as question states that only intersections within the circle count

# Big O

The Big O runtime is O(n^2) because we have a nested loop iterating through the values of the the chordList. In a more specific manner, it is O(n^2 + m), m being the inital iteration through the data, which can then be simplified into O(n^2).  


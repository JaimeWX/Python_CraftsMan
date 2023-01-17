import bisect

def rank(self):
    breakpoints = (6, 7, 8, 8.5)
    grades = ('D', 'C', 'B', 'A', 'S')
    index = bisect.bisect(breakpoints, float(self.rating))
    return grades[index]

# radon cc radon_cyclomatic_complexity2.py -s
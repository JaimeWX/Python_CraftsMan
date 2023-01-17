def rank(self):
    rating_num = float(self.rating)
    if rating_num >= 8.5:
        return 'S'
    elif rating_num >= 8:
        return 'A'
    elif rating_num >= 7:
        return 'B'
    elif rating_num >= 6:
        return 'C'
    else:
        return 'D'

# radon cc radon_cyclomatic_complexity.py -s
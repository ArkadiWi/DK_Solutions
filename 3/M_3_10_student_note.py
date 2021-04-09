# Func pobiera procent zdobytych punktów i zwraca ocenę jako wynik
def show_note(points_in_percent: float):
    grades = ('niedostateczny', 'dopuszczający', 'dostateczny', 'dobry', 'bardzo dobry', 'celujący')
    levels = (0, 45, 55, 80, 90, 95, 100)

    for i, level in enumerate(levels):
        if level < points_in_percent:
            continue
        else:
            return grades[i]


print(show_note(55))

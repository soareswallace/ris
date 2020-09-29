from skfeature.function.statistical_based.gini_index import gini_index
import random


def select_the_best_attributes_only(X, y):
    gini_values_selected = []
    gini_values = gini_index(X, y)

    for index, gini_value in enumerate(gini_values):
        if gini_value < gini_values.mean():
            gini_values_selected.append(index)

    if len(gini_values_selected) == 0:
        gini_values_selected.append(random.randint(0, len(gini_values) - int(1)))

    return gini_values_selected

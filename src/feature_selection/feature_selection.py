from skfeature.function.statistical_based import CFS


def select_the_best_attributes_only(X, y):
    indexes = CFS.cfs(X, y)  # this CFS function uses a correlation based heuristic to return the best features.
    return X[:, indexes], y

def filter_by_percentage(p):
    """
    Stupid simple filter by random number
    """
    import random

    if random.random() < p:
        return False
    else:
        return True

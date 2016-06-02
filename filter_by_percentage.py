def filter_by_percentage(p):
    """
    Stupid simple filter by random number
    
    :param p: float < 1
    :return: boolean
    """
    import random

    if random.random() < p:
        return False
    else:
        return True

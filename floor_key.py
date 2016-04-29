def floor_key(d, m):
    """
    Find the nearest key (<=) in the dict
    
    ex: v = {1: 'a', 5: 'b', 7: 'c'}
    v[floor_key(v, 3)] == 'a'
    v[floor_key(v, 6)] == 'b'
    """
    
    keys = sorted(d.keys())
    
    for k, v in enumerate(keys):
        if v <= m:
            if len(keys) < k + 2:
                return v
            if keys[k + 1] > m:
                return v

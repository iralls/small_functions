def moving_average(l, num=5):
    """
    weighted moving average
    
    weights for each section surrounding the focal point are generated
    in the following way given the example l = [1,2,3,4,5], num = 3,
    where 'num' is the number of points being averaged together (focal point
    in the middle of the num. In this example it is 3, so groupings would be
    [(1),2], [1,(2),3], [2,(3),4], [3,(4),5], [4,(5)].
    If num were 5, it would be
    [(1),2,3], [1,(2),3,4], [1,2,(3),4,5], [2,3,(4),5], [3,4,(5)]:

        * Find the weight of the focal point (arbitrary but generic exponential
        moving average uses this method and it seems to give good weights):
          = 2 / number of points being averaged together
          = 2 / len(a)
          = 2 / 3.0 = 0.663...
        * Find the remaining percentage to divvy up between the total remaining points in the list
          in the list (len(l) - 1)
          = 1 - (2 / len(a))
          = 1 - 0.663
          = 0.333..
        * Divide by two to find the remaining weight to divvy up between each "side" of the focal point
          = (1 - (2 / len(a))) / 2.0
          = 0.33 / 2.0
          = 0.166..
        * Find the weights by generating a list of floats (size (len(l) - 1) / 2.0)
        where each entry is the remaining weight to divide per side (0.1666) multiplied by
        the number of entries on each side of the focal point (2 in this example) - i
        for i in the range of points 0..(len(l) - 1) / 2.0, divided by the sum of numbers
        less than or equal to the (len(l) - 1) / 2.0.
        * Multiply the weights by the entries in the list
        
        Example for one iteration of a list:
        [1,2,3,4,5] where num = 3
        the "focal" point here is 1
        weight for 3 = 2 / 3.0 = 0.666...
        weights so far = [0.666, ??]. Since there is no number before 1, the only point used
        is the one after it.
        
        Remaining weights = 1 - 0.666 = 0.333
        weights for each side = 0.333 / 2.0 = 0.166
        so the weights to divide between ?? (a single entry), is 0.1666
        so, for i in range 1..1 (number of points on each side of the focal point)
        multiply 0.166 * ((1 - 0) / (1)) = 0.1666
        final weights are [0.1666, 0.666, 0.1666], the middle being the focal point
        
        the same methodology for num = 5 returns
        [0.0999, 0.1999, 0.4, 0.1999, 0.0999]
    """
    
    import math
    
    if num % 2 == 0:
        raise Exception("Moving average must have an odd window size")
    
    if len(l) < num:
        raise Exception("Length of list must be at least as large as number of points to average")
     
    # max number of points to look ahead/behind for
    look_ahead = int(math.ceil((num - 1) / 2.0))
    
    def add_factorial(n):
        return (n * (n + 1)) / 2.0
    
    def multiply(a):
        return int(round(a[0] * a[1]))
    
    # weights for each section surrounding the focal point
    total_weights = [((1 - 2 / float(num)) / 2.0) * ((look_ahead - i) / float(add_factorial(look_ahead))) for i in xrange(look_ahead)]

    l2 = []
    for index in range(len(l)):
        
        # weight for focal point is constant
        focal = l[index]
        focal_weight = 2 / float(num)
        
        # adjust the weights
        if index < look_ahead:
            weights_reversed = total_weights[::-1]
            additional_right_weights = weights_reversed[0:len(weights_reversed) - len(l[max(0, index - look_ahead):index])]
            
            right_weights = sorted(total_weights + additional_right_weights)[::-1]
            left_weights = total_weights[0:index]
            
            left_points = l[max(0, index - look_ahead):index]
            right_points = l[index + 1:index + 1 + len(right_weights)]
        # TODO
        #elif i >= len(l) - look_ahead:
        #    pass
        else:
            left_weights = total_weights[::-1]
            right_weights = total_weights

            left_points = l[max(0, index - look_ahead):index]
            right_points = l[index + 1:index + look_ahead + 1]

            
        weights = left_weights + [focal_weight] + right_weights
        points = left_points + [focal] + right_points
        final_points = map(multiply, zip(weights, points))
      
        l2.append(sum(final_points))
    return l2

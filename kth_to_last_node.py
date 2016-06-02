def kth_to_last_node(k, node, count=0):
    """
    Find the k-th to last node in a linked list
    """
    def go(k, node, acc):
        if not node.next:
            return (node, 1)
        else:
            (n, acc) = go(k, node.next, acc)

            acc += 1
            if acc == k:
                return (node, acc)
            else:
                return (n, acc)

    return go(k, node, 0)[0]

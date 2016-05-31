def kth_to_last_node(k, node, count=0):
    """
    Find the k-th to last node in a linked list
    """
    if not node.next:
        return kth_to_last_node(k, node.next, count)
    else:
        count += 1
        if count == k:
            return node

# -*- coding: utf-8 -*-

def h_distance(pfield, node, gnode):
    """Heuristic function based on raw distance.
    """
    return abs(node.x - gnode.x) + abs(node.y - gnode.y)

def h_distance_portals(pfield, node, gnode):
    """Heuristic function based on raw distance,
    with support for proper portal handling.
    """

    # see if we've got a portal
    if node.is_portal():
        # find the partner node
        pnode = pfield.find_portal_exit(node)

        # distance when going through the portal
        pdist = abs(pnode.x - gnode.x) + abs(pnode.y - gnode.y) + 1

        # distance without using the portal
        dist = abs(node.x - gnode.x) + abs(node.y - gnode.y)

        # return the minimum
        return min(dist, pdist)

    # otherwise, same behaviour as h_distance function
    return abs(node.x - gnode.x) + abs(node.y - gnode.y)

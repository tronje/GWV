# -*- coding: utf-8 -*-

def h_distance(pfield, node, goal='g'):
    gnode = pfield.findNode(goal)
    return abs(node.x - gnode.x) + abs(node.y - gnode.y)


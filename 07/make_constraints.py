from arc_consistency import Constraint

def make_constraints(nwork):
    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A1'),
                    nwork.get_node('name', 'D1')
                ],
                lambda word1, word2: word1[0] == word2[0]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A1'),
                    nwork.get_node('name', 'D2')
                ],
                lambda word1, word2: word1[1] == word2[0]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A1'),
                    nwork.get_node('name', 'D3')
                ],
                lambda word1, word2: word1[2] == word2[0]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A2'),
                    nwork.get_node('name', 'D1')
                ],
                lambda word1, word2: word1[0] == word2[1]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A2'),
                    nwork.get_node('name', 'D2')
                ],
                lambda word1, word2: word1[1] == word2[1]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A2'),
                    nwork.get_node('name', 'D3')
                ],
                lambda word1, word2: word1[2] == word2[1]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A3'),
                    nwork.get_node('name', 'D1')
                ],
                lambda word1, word2: word1[0] == word2[2]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A3'),
                    nwork.get_node('name', 'D2')
                ],
                lambda word1, word2: word1[1] == word2[2]
            )
    )

    nwork.constraints.add(
            Constraint(
                [
                    nwork.get_node('name', 'A3'),
                    nwork.get_node('name', 'D3')
                ],
                lambda word1, word2: word1[2] == word2[2]
            )
    )

import pytest

class Cell:
    def __init__(self, is_alive):
        self._state = is_alive
        self.neighbours = set()

    def __eq__(self, other):
        return self._state == other._state

    def __hash__(self):
        return id(self)

    def set_neighbour(self, cell):
        self.neighbours.add(cell)

    def count_living_neighbours(self):
        return len({neighbor for neighbor in self.neighbours if neighbor._state})

def apply_rule(living_cell, number_of_living_neighbors):
    if number_of_living_neighbors in {2, 3}:
        return Cell(is_alive=True)
    # TODO: overcrowding
    return Cell(is_alive=False)


DEAD_CELL = Cell(is_alive=False)
LIVING_CELL = Cell(is_alive=True)

@pytest.mark.parametrize('number_of_living_neighbors, expected_cell',
    [# dies of loneliness
     (0, DEAD_CELL),
     (1, DEAD_CELL),
     # stable
     (2, LIVING_CELL),
     # reproduction
     (3, LIVING_CELL),
     # dies of overpopulation
     (4, DEAD_CELL),
     (5, DEAD_CELL),
     (6, DEAD_CELL),
     (7, DEAD_CELL),
     (8, DEAD_CELL),]
)
def test_rule_application_for_living_cell(number_of_living_neighbors,
                                          expected_cell):
    living_cell = Cell(is_alive=True)

    new_cell = apply_rule(living_cell, number_of_living_neighbors)

    assert new_cell == expected_cell

def test_count_living_neighbours_with_one_living_neighbour():
    cellOne = Cell(True)
    cellOne.set_neighbour(Cell(True))
    assert cellOne.count_living_neighbours() == 1


def test_count_living_neighbours_with_one_dead_neighbour():
    cellOne = Cell(True)
    cellOne.set_neighbour(Cell(False))
    assert cellOne.count_living_neighbours() == 0

def test_evolve():





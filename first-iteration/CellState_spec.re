open Jest;
open Expect;

open CellState;

type testData = {
   currentState: t,
   numberOfNeighbours: int,
   expectedNextState: t
}

let testData = [
  { currentState: Alive, numberOfNeighbours: 1, expectedNextState: Dead },
  { currentState: Alive, numberOfNeighbours: 2, expectedNextState: Alive },
  { currentState: Dead, numberOfNeighbours: 2, expectedNextState: Dead },
  { currentState: Alive, numberOfNeighbours: 3, expectedNextState: Alive },
  { currentState: Dead, numberOfNeighbours: 3, expectedNextState: Alive },
  { currentState: Alive, numberOfNeighbours: 4, expectedNextState: Dead },
];

Belt.List.forEach (testData, ({currentState, numberOfNeighbours, expectedNextState}) => {
  test("A(n) $currentState cell with $numberOfNeighbours is $expectedNextState", () => {
    expect(atNextTick(currentState, numberOfNeighbours)) |> toEqual(expectedNextState)
  });
})

type t = Alive | Dead

let atNextTick = (currentCellState: t, numberOfNeighbours: int) =>
  switch(numberOfNeighbours) {
   | 2 => currentCellState
   | 3 => Alive
   | _ => Dead
}

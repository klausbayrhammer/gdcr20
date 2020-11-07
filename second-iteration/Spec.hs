import Data.Matrix
import Test.Hspec

data CellState = DEAD | ALIVE deriving (Eq, Show)

data Cell = Cell { state :: CellState } deriving (Eq, Show)

stateOf :: Cell -> CellState
stateOf(Cell{state=s}) = s


type Grid = Matrix Cell

cellOf :: Grid -> Int -> Int -> Cell
cellOf grid n m = getElem n m grid


main :: IO ()
main = hspec $ do
  describe "Cells have states" $ do
    it "A dead cell is dead" $ do
      (stateOf Cell{state=DEAD} ) `shouldBe` DEAD
    it "An alive cell is alive" $ do
      (stateOf Cell{state=ALIVE} ) `shouldBe` ALIVE
  describe "Grid has cells at position" $ do
    it "A at 1 1 " $ do
      let cell = Cell{state=DEAD}
      let grid = fromLists [ [cell] ]
      cellOf grid 1 1 `shouldBe` cell



--  describe "Grid has neighbours" $ do
--    it "A cell in the middle of 3x3 grid has no alive neighbours" $ do
--      let dead = Cell{state=DEAD}
--      let grid = fromLists [ [dead, dead, dead], [dead, dead, dead]], [dead, dead, dead]]]

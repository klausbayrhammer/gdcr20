using System;
using UniverseNameSpace;

public class Universe
{
    public Universe(int x, int y)
    {
    }

    public void SetCellStateAt(CellState cellState, int x, int y)
    {
        throw new NotImplementedException();
    }

    public void Iterate()
    {
        throw new NotImplementedException();
    }


    public CellState GetCellStateAt(int x, int y)
    {
        return CellState.Dead;
    }
}

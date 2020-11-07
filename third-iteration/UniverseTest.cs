using NUnit.Framework;
using UniverseNameSpace;

[TestFixture]
public class UniverseTest
{
    [Test]
    public void InitializeUniverseWithDeadCells()
    {
        var universe = new Universe(1,1);

        var cellState = universe.GetCellStateAt(0,0);

        Assert.AreEqual(CellState.Dead, cellState);
    }
}

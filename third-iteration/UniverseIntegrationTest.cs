using NUnit.Framework;
using UniverseNameSpace;

[TestFixture]
public class UnitIntegrationTests
{
    [Test]
    public void ThreeByThreeUniverseWithOneLivingCellIteratesToOnlyDeadCells()
    {
        var universe = new Universe(3,3);
        universe.SetCellStateAt(CellState.Alive, 0, 0);
        universe.Iterate();

        var cellState = universe.GetCellStateAt(0,0);

        Assert.AreEqual(CellState.Dead, cellState);
    }
}

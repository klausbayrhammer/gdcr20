// A simple example to get you started
// JUnit assertion - the default Java assertion library
// https://junit.org/junit5/

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;


public class GameOfLifeTest {

    @Test
    void overpopulation_lifeCell_shouldDie() {
        assertEquals(false, new Cell().nextState(4, true));
    }

    @Test
    void cellShouldNotBeStatic() {
        assertEquals(false, new Cell().nextState(4, true));
    }

    private static class Cell {
        public boolean isAlive;

        static boolean nextState(int neighbours) {
            return self.isAlive;
        }
    }
}



package org.example;

import org.junit.jupiter.api.Test;

import java.util.List;

import static org.junit.jupiter.api.Assertions.*;

class ContainDuplicate_217Test {
    @Test
    void test0() {
        ContainDuplicate_217 mod = new ContainDuplicate_217();

        assertTrue(mod.containsDuplicate(new int[]{1, 2, 3, 1}));
        assertFalse(mod.containsDuplicate(new int[]{1, 2, 3, 4}));
        assertTrue(mod.containsDuplicate(new int[]{1, 1, 1, 3, 3, 4, 3, 2, 4, 2}));
    }
}

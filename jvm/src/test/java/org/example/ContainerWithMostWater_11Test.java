package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class ContainerWithMostWater_11Test {
    ContainerWithMostWater_11 obj;

    @BeforeEach
    void setup() {
        obj = new ContainerWithMostWater_11();
    }

    @Test
    void test0() {
        int[] input = new int[]{1,8,6,2,5,4,8,3,7};

        assertEquals(49, obj.maxArea(input));
    }
}

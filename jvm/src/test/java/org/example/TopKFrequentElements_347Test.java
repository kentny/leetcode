package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

public class TopKFrequentElements_347Test {
    TopKFrequentElements_347 solution = new TopKFrequentElements_347();

    @Test
    void test0() {
        int[] input = new int[]{1,1,1,2,2,3};

        int[] output = solution.topKFrequent(input, 2);

        assertArrayEquals(new int[]{1,2}, output);
    }

    @Test
    void test1() {
        int[] input = new int[]{1};

        int[] output = solution.topKFrequent(input, 1);

        assertArrayEquals(new int[]{1}, output);
    }

}

package org.example;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class NumberOfIslands_200Test {
    @Test
    void test0() {
        char[][] input = {
            {'1','1','0','0','0'},
            {'1','1','0','0','0'},
            {'0','0','1','0','0'},
            {'0','0','0','1','1'},
        };

        int result = new NumberOfIslands_200().numIslands(input);

        assertEquals(3, result);
    }

    @Test
    void test1() {
        char[][] input = {
            {'1','1','1'},
            {'0','1','0'},
            {'1','1','1'}
        };

        int result = new NumberOfIslands_200().numIslands(input);

        assertEquals(2, result);
    }
}

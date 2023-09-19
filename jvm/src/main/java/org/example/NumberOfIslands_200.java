package org.example;

public class NumberOfIslands_200 {
    public int numIslands(char[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        boolean[][] checked = new boolean[m][n];
        int result = 0;

        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (grid[i][j] == '1' && !checked[i][j]) {
                    result++;
                    check(grid, checked, i, j);
                }
            }
        }
        return result;
    }

    void check(char[][] grid, boolean[][] checked, int row, int col) {
        if (checked[row][col] || grid[row][col] == '0') {
            return;
        }

        checked[row][col] = true;

        if (col < grid[0].length - 1) {
            check(grid, checked, row, col+1);
        }
        if (row < grid.length - 1) {
            check(grid, checked, row + 1, col);
        }
        if (col > 0) {
            check(grid, checked, row, col-1);
        }
        if (row > 0) {
            check(grid, checked, row-1, col);
        }
    }
}

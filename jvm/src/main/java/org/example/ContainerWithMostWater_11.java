package org.example;

import static java.lang.Math.max;
import static java.lang.Math.min;

public class ContainerWithMostWater_11 {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length - 1;

        int maxAmount = 0;
        while (left < right) {
            int amount = (right - left) * min(height[left], height[right]);
            maxAmount = max(amount, maxAmount);

            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        return maxAmount;
    }
}

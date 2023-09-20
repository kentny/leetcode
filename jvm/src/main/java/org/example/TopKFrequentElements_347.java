package org.example;

import java.util.*;

public class TopKFrequentElements_347 {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();

        for (int num : nums) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        List<Integer> sortedCounts = map.values().stream().sorted(Comparator.reverseOrder()).toList();

        Set<Integer> topKElementSet = new HashSet<>();
        for (int i=0; i<k; i++) {
            for (int j : map.keySet()) {
                if (map.get(j).equals(sortedCounts.get(i))) {
                    topKElementSet.add(j);
                }
            }
        }
        return topKElementSet.stream().mapToInt(Integer::intValue).toArray();
    }
}

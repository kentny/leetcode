package org.example;

import java.util.*;

public class GroupAnagrams_49 {

    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> result = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();

        for (String str : strs) {
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sortedStr = Arrays.toString(chars);

            Integer index = map.get(sortedStr);
            if (index == null) {
                List<String> newList = new ArrayList<>();
                newList.add(str);
                result.add(newList);
                Integer newListIndex = result.size() - 1;
                map.put(sortedStr, newListIndex);
            } else {
                result.get(index).add(str);
            }
        }

        return result;

//        Map<Integer, List<String>> anagrams = new HashMap<>();
//
//        for (String str : strs) {
//            char[] chars = str.toCharArray();
//
//            int sum = 0;
//            for (char c : chars) {
//                sum += c;
//            }
//
//            List<String> anagram = anagrams.get(sum);
//            if (anagram == null) {
//                List<String> newList = new ArrayList<>();
//                newList.add(str);
//                anagrams.put(sum, newList);
//            } else {
//                anagram.add(str);
//            }
//        }
//
//        return anagrams.values().stream().toList();
    }
}

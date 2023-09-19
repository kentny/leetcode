package org.example;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class ValidAnagram_242Test {
    ValidAnagram_242 obj;

    @BeforeEach
    void setup() {
        obj = new ValidAnagram_242();
    }

    @Test
    void test0() {
        assertTrue(obj.isAnagram("anagram", "nagaram"));
        assertFalse(obj.isAnagram("rat", "car"));
    }
}

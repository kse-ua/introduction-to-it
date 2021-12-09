package com.company;
import java.util.*;

public class Main {
    static Map<String, Integer> cache = new HashMap<String, Integer>();

    public static void main(String[] args) {
        System.out.println("sub: " + subProcedure(5, 2));
        System.out.println("add: " + addProcedure(5,2));
    }

    public static int addProcedure(int a, int b){
        String key = Integer.toString(a) + "," + Integer.toString(b);
        if(cache.containsKey(key)){
            return cache.get(key);
        }
        int res = a + b;
        cache.put(key, res);
        return res;
    }
    public static int subProcedure(int a, int b){
        String key = Integer.toString(a) + "," + Integer.toString(b);
        if(cache.containsKey(key)){
            return cache.get(key);
        }
        int res = a - b;
        cache.put(key, res);
        return res;
    }
}

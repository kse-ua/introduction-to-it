package com.company;
import java.util.*;

public class Main {
    static Map<String, Integer> cache = new HashMap<String, Integer>();

    public static void main(String[] args) {
        System.out.println(
                         addFunction(10, 20) + " " +
                         addFunction(1, 2) + " " +
                         addFunction(100, 20) + " " +
                         addFunction(100, 200) + " ");
        System.out.print(
                         addProcedure(10, 20) + " " +
                         addProcedure(1, 2) + " " +
                         addProcedure(100, 20) + " " +
                         addProcedure(100, 200) + " ");
    }

    public static int addFunction(int a, int b){
        int res = a + b;
        return res;
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
}

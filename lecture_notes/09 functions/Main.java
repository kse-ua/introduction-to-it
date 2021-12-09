package com.company;
import java.util.*;

public class Main {
    static String[] cities = {"Athens", "Roma", "London", "Beijing", "Kiev", "Riga"};

    public static void main(String[] args) {
        f1();

        System.out.println(Arrays.toString(cities));
        System.out.println(Arrays.toString(getLengths(cities)));
    }

    public static void f1(){
        {
            String[] cities = {"Athens", "Roma"};

            System.out.println(Arrays.toString(cities));
            System.out.println(Arrays.toString(toUpperCase(cities.clone())));

            System.out.println(Arrays.toString(cities));
            System.out.println(Arrays.toString(toLowerCase(cities.clone())));
        }
        {
            String[] cities = {"Athens", "Beijing", "Kiev"};
            System.out.println(Arrays.toString(cities));
            System.out.println(Arrays.toString(toUpperCase(cities.clone())));
        }
    }

    public static int[] getLengths(String[] s){
        int[] lengths = new int[s.length];
        for(int i = 0; i < s.length; i++) {
            lengths[i] = s[i].length();
        }
        return lengths;
    }

    public static String[] toUpperCase(String s[]){
        for(int i = 0; i < s.length; i++) {
            s[i] = s[i].toUpperCase();
        }
        return s;
    }

    public static String[] toLowerCase(String s[]){
        for(int i = 0; i < s.length; i++) {
            s[i] = s[i].toLowerCase();
        }
        return s;
    }
}

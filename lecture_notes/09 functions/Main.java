package com.company;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        catchRest(1, 2, 3);

        Map<String, String> map = new HashMap<String, String>();
        map.put("field", "value");
        f2(1, "Marcus", map);
    }

    public static void catchRest(Object ...args){
        System.out.println(Arrays.toString(args));
    }
    public static void f2(Object ...args){
        for(int i = 0; i < args.length; i++){
            String type = args[i].getClass().getName();
            System.out.println("Type: " + type);
            System.out.println("Value: " + args[i].toString());
        }
    }
}

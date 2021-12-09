package com.company;

public class Main {
    public static void main(String[] args) {
        System.out.print(max(10,20) + " ");
        System.out.print(max(10) + " ");
        System.out.print(max(-20));
    }

    public static int max(int a, int b){
        return (a > b) ? a : b;
    }
    public static int max(int a){
        return max(a, 0);
    }
    public static int max(){
        return max(0,0);
    }
}

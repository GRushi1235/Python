import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int count =0;
        int temp = 0;
        while(n>0){
         temp = n%10;
         n= n/10;
         if(temp == 4)
         count++;   
        }
        System.out.println(count);
    }
}

import java.util.Scanner;



class Palimdrome {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        Integer num = sc.nextInt();

        if(num < 0) {
            System.out.println("Fail");
        } 
        int revNum = 0;
        int temp = num;
        while(temp > 0) {

            revNum = revNum * 10 + temp % 10;
            temp = temp / 10;
        }
        if(revNum == num) {
            System.out.println("TRUE");
        } else {
            System.out.println("FALSE");
        }

    }

}
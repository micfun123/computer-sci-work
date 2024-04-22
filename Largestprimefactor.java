import java.util.Scanner;


public class Largestprimefactor {
    public static void main(String[] args) {
        long num;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Enter a number: ");
            num = scanner.nextLong();
        }
        long largest = 0;
        for (long i = 2; i <= num; i++) {
            if (num % i == 0) {
                num = num / i;
                largest = i;
                i = 2;
            }
        }
        System.out.println(largest);
    }
}

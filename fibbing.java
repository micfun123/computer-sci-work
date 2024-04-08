import java.util.Scanner;
public class fibbing {
    public static void main(String[] args) {
        int a = 0;
        int b = 1;
        int z = 0;
        //ask user for number of terms
        System.out.println("Enter the number of terms: ");
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            for (int i = 0; i < n; i++){
                z = a + b;
                System.out.println(z);
                a = b;
                b = z;
            }
        }
    } 
}
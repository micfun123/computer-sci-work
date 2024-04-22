public class Largestprimefactor {
    public static void main(String[] args) {
        long num = 600851475143l;
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

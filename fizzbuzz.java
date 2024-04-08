public class fizzbuzz{

    /**
     * @param n
     * @return
     */
    public static String fizzbuzztest(int n){
        String current = "";
        if (n % 3 == 0) {
            current = current + "Fizz";
        }
        if (n % 5 == 0) {
            current = current + "Buzz";
        }
        if (current == "") {
            current = String.valueOf(n);
        }
        

        return current;
    }

    public static void main(String[] args) {
        System.out.println(fizzbuzztest(5));
        System.out.println(fizzbuzztest(3));
        System.out.println(fizzbuzztest(15));
        System.out.println(fizzbuzztest(124));
    }

}
public class numpaladrom {

    public static boolean isPalindrome(int num){
        int temp = num;
        int rev = 0;
        while (temp > 0){
            rev = rev * 10 + temp % 10; // 0 * 10 + 1 = 1
            temp /= 10; 
        }
        return rev == num;
    }

    public static void main(String[] args) {
        System.out.println(isPalindrome(20));
        System.out.println(isPalindrome(202));
    }
}

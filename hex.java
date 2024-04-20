public class hex {

    public static void tohex(int num){
        if (num == 0) {
            System.out.print(0);
            System.out.println("\n");
            return;
        }
        int[] hex = new int[100];
        int counter = 0;
        while (num != 0) {
            hex[counter] = num % 16;
            num = num / 16;
            counter ++;
        }
        for (int i = counter - 1; i >= 0; i--) {
            
            if (hex[i] >= 10) {
                System.out.print((char)(hex[i] + 55));
            } else {
                System.out.print(hex[i]);
            }

        }
        System.out.println("\n");
    }

    public static void main(String[] args) {
        hex.tohex(100);
        hex.tohex(11);
        hex.tohex(5);
        hex.tohex(0);
    }
    
}

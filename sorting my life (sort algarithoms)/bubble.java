public class bubble {

    // bubble sort
     static void bubblesorter(int data[]) {
        int n = data.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (data[j] > data[j + 1]) {
                    // swap temp and data[i]
                    int temp = data[j];
                    data[j] = data[j + 1];
                    data[j + 1] = temp;
                }
            }
        }
        for (int i = 0; i < n; i++) {
            System.out.print(data[i] + " ");
        }
    }


    public static void main(String[] args) {
        
        int data[] = { 5,2,6,1134,13413,54,1,6,89,23,6,8,34,73,4,327,5,324 };
        bubblesorter(data);

    }
}

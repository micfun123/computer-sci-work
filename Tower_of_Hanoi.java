public class Tower_of_Hanoi {
    
    

    public static void solver(int number_of_disks, char start, char end, char temp){
        if (number_of_disks == 1) {
            System.out.println("Move disk " + number_of_disks + " From " + start + " to "+ end);
            return;
        }
        solver(number_of_disks - 1, start, temp, end);
        System.out.println("Move disk " + number_of_disks + " From " + start + " to "+ end);
        solver(number_of_disks - 1, temp, end, start);
    }

    public static void main(String[] args) {
    
        char start = 'A';
        char end = 'C';
        char temp = 'B';
        solver(3, start, end, temp);

    }
}

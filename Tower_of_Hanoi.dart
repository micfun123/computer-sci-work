
int move = 0;

void solver(int number_of_disks, start, end, temp){
  move = move +1;
  if (number_of_disks ==1) {
    print("Move disk 1 from rod "+ start + " to rod " + end);
    return ;
  }
  solver(number_of_disks - 1, start, temp, end);
  print("Move disk "+ number_of_disks.toString() + " from rod "+ start+ " to rod "+ end);
  solver(number_of_disks - 1, temp, end, start);

}


void main(){
  solver(5, "A", "C", "B");
  print("Number of moves: " + move.toString());
}

let solver = (number_of_disks, source, target, temp) => {
    if (number_of_disks === 1) {
        console.log(`Move disk 1 from ${source} to ${target}`);
        return;
    }
    solver(number_of_disks - 1, source, temp, target);
    console.log(`Move disk ${number_of_disks} from ${source} to ${target}`);
    solver(number_of_disks - 1, temp, target, source);
}

solver(3, "A", "C", "B");

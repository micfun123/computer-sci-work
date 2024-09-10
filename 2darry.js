let staff = ["anna", "bob", "charlie"];
let sales = [[100, 110, 120, 110], [200, 210, 220, 210], [300, 310, 320, 310]];
let total = 0;

function add(accumulator, a) {
    return accumulator + a;
  }

for (let index = 0; index < staff.length; index++) {
    console.log("Staff member: " + staff[index] + " they solded "+ sales[index].reduce(add, 0));
    for (let quarters = 0; quarters < sales[index].length; quarters++) {
        console.log("On Quarter: " + (quarters+1) + "they sold " + sales[index][quarters]) 
        total = total + sales[index][quarters];
    }
    console.log("\n")    
}
console.log("Thats a total of: " + total);
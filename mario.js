function pyramid(hight) {
    console.log(hight);
    for (let step = 0; step < hight+1; step++){
        for (let space = 0; space < hight-step; space++){
            process.stdout.write(" ");
        }
        for (let hash = 0; hash < step; hash++){
            process.stdout.write("#");
        }
        process.stdout.write(" ");
        for (let hash = 0; hash < step; hash++){
            process.stdout.write("#");
        }
        console.log()
    }
  }

pyramid(5);
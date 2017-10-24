
var countBits = function(num) {

    var counter = 0;
    while (num > 0) {
        counter = counter + (num & 1);
        num = num >> 1;
    }

    return counter;
}

console.log(countBits(15))
console.log(countBits(1))
console.log(countBits(0))
console.log(countBits(-10))

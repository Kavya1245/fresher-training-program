"use strict";
function getEvenNumbers(nums) {
    return nums.filter(n => n % 2 === 0);
}
console.log(getEvenNumbers([1, 2, 3, 4, 5, 6]));

// function to double every number in an array
function double(nums) {
    return nums.map(n => n * 2);
}
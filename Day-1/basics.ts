function getEvenNumbers(nums: number[]): number[] {
  return nums.filter(n => n % 2 === 0);
}
console.log(getEvenNumbers([1,2,3,4,5,6]));

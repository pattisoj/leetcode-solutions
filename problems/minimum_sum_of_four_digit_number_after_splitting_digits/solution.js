/**
 * @param {number} num
 * @return {number}
 */
var minimumSum = function(num) {
    const digits = num.toString().split('');
    const n = digits.length;
    let sum = 0;
    digits.sort();
    
    for (let i = 0; i < n / 2; i++) {
        const pair = digits[i] + digits[n - 1 - i];
        sum += +pair;
    }
  
    return sum;
};
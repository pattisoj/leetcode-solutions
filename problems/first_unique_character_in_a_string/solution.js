/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function(s) {
    let repeats = {};
    
    for (let c of s.split("")){
        if (!(c in repeats)) repeats[c] = 0;
        repeats[c]++;
    }
    
    for (let i = 0; i < s.length; i++){
        if (repeats[s[i]] === 1) return i;
    }
    return -1;
};
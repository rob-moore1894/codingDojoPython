// Reverse String

function reverseString(str){
    var newStr = "";
    for (var i = str.length - 1; i >= 0; i--){
        newStr += str[i]
    }
    console.log(str)
    console.log(newStr);
    return newStr;
}

reverseString("I was put on this Earth to be phenomenal!");

// “String: Is Palindrome
// Create a function that returns a boolean whether the string is a strict palindrome. For "a x a" or "racecar", return true. Do not ignore spaces, punctuation and capitalization: if given "Dud" or "oho!", return false.”

function isPalindrome(str){
    var newStr = str.toLowerCase().replace(/[^A-Za-z0-9]/g, '');
    console.log(newStr)
    for (var i = 0; i < newStr.length / 2; i++){
        if(newStr[i] != newStr[newStr.length - 1 - i]){
            return false
        }
    }

    return true;
}

console.log(isPalindrome("RaCe CaR"));
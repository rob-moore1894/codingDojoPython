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
function docReady(fn) {
    // stack overflow
    // see if DOM is already available
    if (document.readyState === "complete" || document.readyState === "interactive") {
        // call on next available tick
        setTimeout(fn, 1);
    } else {
        document.addEventListener("DOMContentLoaded", fn);
    }
}

function resumeMoney(value, fix = 2){

    value = value.toFixed(fix)

    let signal = ""

    let right = value.toString().split(".")[1]
    let left = value.toString().split(".")[0]

    // make the negative left act like a positive left
    if(left[0] == "-"){
        left = left.substr(1)
        signal = "-"
    }

    let cutMax = left.length
    let suffix = 0

    while(
        3 < cutMax
    ){
        cutMax -= 3
        suffix += 1
    }

    if(left.substr(cutMax,cutMax) == ""){
        return signal + left.substr(0,cutMax)+"."+right
    }else{
        return signal + left.substr(0,cutMax)+"."+left.substr(cutMax,cutMax)+" "+suffixMoney[suffix]
    }

}
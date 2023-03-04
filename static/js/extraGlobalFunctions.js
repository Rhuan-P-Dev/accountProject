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

    let right = value.toString().split(".")[1]
    let left = value.toString().split(".")[0]

    let cutMax = left.length
    let suffix = 0

    while(true){
        if(3 < cutMax){
            cutMax -= 3
            suffix += 1
        }else{
            break
        }
    }

    if(left.substr(cutMax,cutMax) == ""){
        return left.substr(0,cutMax)+"."+right
    }else{
        return left.substr(0,cutMax)+"."+left.substr(cutMax,cutMax)+" "+suffixMoney[suffix]
    }

}
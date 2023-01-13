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

function sumArray(array){

    let result = 0

    for (let index = 0; index < array.length; index++) {
        result+=array[index]
    }

    return result

}
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

docReady(function(){

    //socket.send({'cmd': "???"})


    loc    = window.document.location
    socket = io.connect(loc.origin)

    socket.on('from_server', function(msg) {
        if(msg.cmd == "???"){
        }
    })

})
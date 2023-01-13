
import { YearController } from "./yearController.js"
import { PaintController } from "./paintController.js"
import { KeyBordController } from "./keyBordController.js"

export function upDateSite(year){
    resetSite()
    getSiteInfo(year)
    Year.setYear(year)
    Year.saveYear()
}


const loc    = window.document.location
const socket = io.connect(loc.origin)

var Year = ""
var Paint = ""
var KeyBord = ""

docReady(function(){

    const yearNode = document.getElementById("mainYear")

    Year = new YearController(yearNode)
    Paint = new PaintController(yearNode)
    KeyBord = new KeyBordController()

    setTimeout(browseInit,100)

    // build the site
    socket.on('from_server', function(msg) {
        if(msg.cmd == "allYearData"){
            buildCalendar(msg.data)

            document.getElementById("mainSum").innerHTML = moneyStandard+sumArray(msg.data)

            Paint.paintCalendar(msg.data)
            Paint.paintYear(msg.data)

        }
    })

})



function buildCalendar(data){

    let monthsBox = document.getElementById("monthsBox")
    
    for (let index = 0; index < data.length; index++) {

        let tempTemplate = monthTemplate

        let numberCalendar = flatNumberToFatNamber[index+1]
        let nameCalendar = calendarConverter[index+1]

        tempTemplate = tempTemplate.replace("{id}",numberCalendar)
        tempTemplate = tempTemplate.replace("{month}",numberCalendar+" - "+nameCalendar)
        tempTemplate = tempTemplate.replace("{value}", data[index])

        tempTemplate = tempTemplate.replace("{value}", moneyStandard+data[index])

        monthsBox.insertAdjacentHTML("beforeend",tempTemplate)

    }

}

function getSiteInfo(year){
    socket.send({'cmd': 'getAllYearData', 'data': year})
}

function resetSite(){
    document.getElementById("monthsBox").innerHTML = ""
}



// all functions that will be performed once
function browseInit(){

    initSite()

    KeyBord.buildControlersTriggers()

}



function initSite(){
    let year = Year.loadYear()
    if(!year){
        year = Year.getYear()
    }

    getSiteInfo(year)
    Year.setYear(year)

}
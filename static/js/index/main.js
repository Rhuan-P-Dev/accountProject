
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

            document.getElementById("mainSum").innerHTML = moneyStandard+resumeMoney(
                msg.data.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
            )

            Paint.paintCalendar(msg.data)
            Paint.paintYear(msg.data)

            buildMonthsTriggers()

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

        tempTemplate = tempTemplate.replace("{moneyValue}", moneyStandard+resumeMoney(data[index]))

        monthsBox.insertAdjacentHTML("beforeend",tempTemplate)

    }

}

function getSiteInfo(year){
    socket.send({'cmd': 'getAllYearData', 'data': year})
}

function resetSite(){
    document.getElementById("monthsBox").innerHTML = ""
}

function buildMonthsTriggers(){

    let months = document.querySelectorAll(".month")

    for (let index = 0; index < months.length; index++) {

        months[index].addEventListener("click",function(){

            socket.send({'cmd': 'setAccountsData', 'year':Year.getYear(), 'month':parseInt(this.getAttribute("id"))})

            setTimeout(() => {
                location.href = "accounts"
            },25)

        })
        
    }
        
}


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
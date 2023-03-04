
//import { YearController } from "./yearController.js"
//import { upDateSite } from "./main.js"

//const yearController = new YearController()

export class DataController{

    dataElement = ""

    constructor(dataElement = document.getElementById("mainData")){
        this.dataElement = dataElement
    }

    setYear(value){
        this.dataElement.setAttribute("year",value)
        this.updateDate()
    }

    setMonth(value){
        value = this.checkMonth(value)
        this.dataElement.setAttribute("month",value)
        this.updateDate()
    }

    getYear(){
        return  parseInt(this.dataElement.getAttribute("year"))
    }

    getMonth(){
        return parseInt(this.dataElement.getAttribute("month"))
    }

    updateDate(){
        this.dataElement.innerHTML = flatNumberToFatNamber[this.getMonth()]+"/"+this.getYear()+" - "+calendarConverter[this.getMonth()]
    }

    mathYear(value){
        this.setYear(this.getYear()+value)
    }

    mathMonth(value){
        this.setMonth(this.getMonth()+value)
    }






    checkMonth(value){
        if(value < 1){
            this.mathYear(-1)
            return 12
        }else if(value > 12){
            this.mathYear(1)
            return 1
        }
        return value
    }

}
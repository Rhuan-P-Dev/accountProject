
export class YearController{

    yearElement = ""

    constructor(yearElement = document.getElementById("mainYear")){
        this.yearElement = yearElement
    }
    
    getYear(){
        return parseInt(this.yearElement.innerHTML)
    }

    setYear(year){
        this.yearElement.innerHTML = year
    }

    saveYear(){
        localStorage.setItem("year", this.getYear())
    }

    loadYear(){
        return parseInt(localStorage.getItem("year"))
    }

    math(value){
        this.setYear(this.getYear()+value)
    }

}
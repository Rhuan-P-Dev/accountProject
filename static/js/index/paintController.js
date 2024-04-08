
const COLOR = {
    "default":"gray",
    "defaultBackground":"rgba(128, 128, 128, 0.2)",

    "positive":"green",
    "positiveBackground":"rgba(0, 128, 0, 0.2)",

    "negative":"red",
    "negativeBackground":"rgba(255, 0, 0, 0.2)",
}

export class PaintController{

    yearElement = ""

    constructor(yearElement){
        this.yearElement = yearElement
    }
    
    paintCalendar(allMonthsValueArray){

        let months = document.querySelectorAll(".month")
    
        for (let index = 0; index < months.length; index++) {
    
            let value = allMonthsValueArray[index]
    
            let result = this.checkValue(value)
    
            months[index].style.border = "2px solid "+result.color
            months[index].style.backgroundColor = result.backgroundColor
            
        }

    }

    paintYear(allMonthsValueArray){
        this.yearElement.style.color = this.checkValue(
            allMonthsValueArray.reduce((accumulator, currentValue) => accumulator + currentValue, 0)
        ).color
    }

    checkValue(value){

        let color = {"color":COLOR.default,"backgroundColor":COLOR.defaultBackground}
    
        if(value < 0){
            return {"color":COLOR.negative,"backgroundColor":COLOR.negativeBackground}
        }else if(value > 0){
            return{"color":COLOR.positive,"backgroundColor":COLOR.positiveBackground}
        }
    
        return color
    
    }

}
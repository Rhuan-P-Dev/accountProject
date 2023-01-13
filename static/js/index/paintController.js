
// which color patterns should be applied
// B = back ground
const COLOR = {
    "default":"gray",
    "defaultB":"rgba(128, 128, 128, 0.2)",

    "positive":"green",
    "positiveB":"rgba(0, 128, 0, 0.2)",

    "negative":"red",
    "negativeB":"rgba(255, 0, 0, 0.2)",
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
            months[index].style.backgroundColor = result.backGroundColor
            
        }
            
    }

    paintYear(allMonthsValueArray){
        this.yearElement.style.color = this.checkValue(sumArray(allMonthsValueArray)).color
    }

    checkValue(value){

        let color = {"color":COLOR.default,"backGroundColor":COLOR.defaultB}
    
        if(value < 0){
            return {"color":COLOR.negative,"backGroundColor":COLOR.negativeB}
        }else if(value > 0){
            return{"color":COLOR.positive,"backGroundColor":COLOR.positiveB}
        }
    
        return color
    
    }

}

import { YearController } from "./yearController.js"
import { upDateSite } from "./main.js"

const keyBordFunctions = {"ArrowLeft":mainLeftFunction,
                          "ArrowRight":mainRightFunction}

const yearController = new YearController()

export class KeyBordController{

    buildControlersTriggers(){

        let mainLeft = document.getElementById("mainLeft")
        let mainRight = document.getElementById("mainRight")

        let html = document.querySelector("html")

        mainLeft.addEventListener("click",function(){
            mainLeftFunction()
        })

        mainRight.addEventListener("click",function(){
            mainRightFunction()
        })

        html.addEventListener("keydown",function(e){
            if(keyBordFunctions[e["key"]]){
                keyBordFunctions[e["key"]]()
            }
        })

    }

}


function mainLeftFunction(){
    yearController.math(-1)
    upDateSite(yearController.getYear())
}

function mainRightFunction(){
    yearController.math(1)
    upDateSite(yearController.getYear())
}
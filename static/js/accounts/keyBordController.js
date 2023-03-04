
import { DataController } from "./dataController.js"

const Data = new DataController()

const keyBordFunctions = {"ArrowLeft":ArrowLeftFunction,
                          "ArrowRight":ArrowRightFunction,
                          " ":spaceFunction}

export class KeyBordController{

    leftButtonElement = ""
    midButtonlement = ""
    rightButtonElement = ""

    constructor(leftButton = document.getElementById("mainLeft"), midButton = document.getElementById("mainMid"), rightButton = document.getElementById("mainRight")){
        this.leftButtonElement = leftButton
        this.midButtonlement = midButton
        this.rightButtonElement = rightButton
    }

    buildTriggers(){
        return
        document.querySelector("html").addEventListener("keydown",function(e){
            if(keyBordFunctions[e["key"]]){
                keyBordFunctions[e["key"]]()
            }
        })

    }

}


function ArrowLeftFunction(){
    Data.mathMonth(-1)
}

function ArrowRightFunction(){
    Data.mathMonth(1)
}

function spaceFunction(){
    location.href = "/"
}
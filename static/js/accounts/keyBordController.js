
import { DataController } from "./dataController.js"
import { AccountsController } from "./accountsController.js"
import { ServerRequestController } from "./serverRequestController.js"

const Data = new DataController()
const Accounts = new AccountsController()
const ServerRequest = new ServerRequestController()

const keyBoardShiftFunctions = {"ArrowLeft":ArrowLeftFunction,
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
        document.querySelector("html").addEventListener("keydown",function(e){
            if(keyBoardShiftFunctions[e["key"]] && e["shiftKey"]){
                keyBoardShiftFunctions[e["key"]]()
            }
        })

    }

}


function ArrowLeftFunction(){
    Accounts.reset()
    Data.mathMonth(-1)
    ServerRequest.getAccounts()
}

function ArrowRightFunction(){
    Accounts.reset()
    Data.mathMonth(1)
    ServerRequest.getAccounts()
}

function spaceFunction(){
    location.href = "/"
}
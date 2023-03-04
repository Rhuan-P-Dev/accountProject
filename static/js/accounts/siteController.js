
import { DataController } from "./dataController.js"

const Data = new DataController()

export class SiteController{

    mainUp = ""
    mainMid = ""
    mainDown = ""

    sortBox = ""
    accountsBox = ""


    constructor(mainUp = document.getElementById("mainUp"), mainMid = document.getElementById("mainMid"), mainDown = document.getElementById("mainDown"), accountsBox = document.getElementById("accountsBox"), sortBox = document.getElementById("sortBox")){
        this.mainUp = mainUp
        this.mainMid = mainMid
        this.mainDown = mainDown

        this.sortBox = sortBox
        this.accountsBox = accountsBox
    }

    buildTriggers(){
        window.addEventListener("resize",function(){
            new SiteController().initStart()
        })
    }

    initStart(){
        this.accountsBox.style.height = (window.innerHeight - (this.sortBox.clientHeight + this.mainUp.clientHeight + this.mainDown.clientHeight) - 5) + "px"
    }

}
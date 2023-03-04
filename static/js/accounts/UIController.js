
import { AccountsController } from "./accountsController.js"
import { DataController } from "./dataController.js"
import { ServerRequestController } from "./serverRequestController.js"

const Accounts = new AccountsController()
const Data = new DataController()
const ServerRequest = new ServerRequestController()

var deleteButtonSwitch = false

export class UIController {

    leftButtonElement = ""
    midButtonlement = ""
    rightButtonElement = ""

    addElement = ""
    saveElement = ""
    deleteElement = ""

    constructor(leftButton = document.getElementById("leftButton"), midButton = document.getElementById("midButton"), rightButton = document.getElementById("rightButton"), accountAdd = document.getElementById("accountsAdd"), accountSave = document.getElementById("accountsSave"), accountDelete = document.getElementById("accountsDelete")){
        this.leftButtonElement = leftButton
        this.midButtonlement = midButton
        this.rightButtonElement = rightButton
        this.addElement = accountAdd
        this.saveElement = accountSave
        this.deleteElement = accountDelete
    }

    buildTriggers(){

        UI.addElement.addEventListener("click",function(){
            Accounts.add()
        })

        UI.leftButtonElement.addEventListener("click",function(){
            Accounts.reset()
            Data.mathMonth(-1)
            ServerRequest.getAccounts()
        })

        UI.midButtonlement.addEventListener("click",function(){
            location.href = "/"
        })

        UI.rightButtonElement.addEventListener("click",function(){
            Accounts.reset()
            Data.mathMonth(1)
            ServerRequest.getAccounts()
        })

        UI.saveElement.addEventListener("click",function(){
            Accounts.save()
        })

        UI.deleteElement.addEventListener("click",function(){

            let allAccounts = document.querySelectorAll(".account")

            for (let index = 0; index < allAccounts.length; index++) {
                if(deleteButtonSwitch){
                    if(!allAccounts[index].getAttribute("class").match("freeze")){
                        allAccounts[index].setAttribute("class","account")

                        allAccounts[index].setAttribute("delete","false")
                    }
                }else{
                    if(!allAccounts[index].getAttribute("class").match("freeze")){
                        allAccounts[index].setAttribute("class","account delete")

                        allAccounts[index].setAttribute("delete","true")
                    }
                }
            }

            if(deleteButtonSwitch){
                UI.deleteElement.style.color = ""
                deleteButtonSwitch = false
            }else{
                UI.deleteElement.style.color = "red"
                deleteButtonSwitch = true
            }

        })

    }

}

const UI = new UIController()
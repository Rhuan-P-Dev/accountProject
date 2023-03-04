
import { DataController } from "./dataController.js"
import { ServerRequestController } from "./serverRequestController.js"
import { SumBarController } from "./sumBarController.js"

const Data = new DataController()
const ServerRequest = new ServerRequestController()
//const SumBar = new SumBarController()

const convertNumberToName = {1:"name",3:"value",5:"product",7:"method",9:"start",11:"end",13:"date"}
const defaultActions = {3:parseFloat, 9:parseInt, 11:parseInt, 13:parseInt}

var accountChangerArray = []

var accountChangerTimer = ""

export class AccountsController {

    addElement = ""
    saveElement = ""
    deleteElement = ""

    accountsBoxElement = ""

    constructor(accountAdd = document.getElementById("accountsAdd"), accountSave = document.getElementById("accountsSave"), accountDelete = document.getElementById("accountsDelete"), accountsBox = document.getElementById("accountsBox")){
        this.addElement = accountAdd
        this.saveElement = accountSave
        this.deleteElement = accountDelete
        this.accountsBoxElement = accountsBox
    }

    add(account = accountTemplate.replace("{ID}",randomUniqueId()), add = true){
        this.accountsBoxElement.insertAdjacentHTML("afterbegin",account)
        this.addCheckTrigger(this.accountsBoxElement.childNodes[0])
        this.addDeleteTrigger(this.accountsBoxElement.childNodes[0])
        if(add){
            this.accountsBoxElement.childNodes[0].setAttribute("action","add")
        }
    }

    reset(){
        this.accountsBoxElement.innerHTML = ""
    }

    addCheckTrigger(account){

        if(account.getAttribute("class").match("freeze")){
            return
        }

        let readyCheckFunction = new AccountsController().readyCheck
        let readyFunction = new AccountsController().ready

        account.childNodes[3].addEventListener("keyup",function(){

            if(parseInt(this.value)){
                readyFunction(this, true)
            }else{
                readyFunction(this, false)
            }

            readyCheckFunction(this.parentElement)

            new SumBarController().checkAllAccounts()

        })

        account.childNodes[9].addEventListener("keyup",function(){
            if(
                parseInt(this.value) < parseInt(account.childNodes[11].value) && parseInt(this.value) >= 1 
                || 
                this.value.toLowerCase() == "inf" && account.childNodes[11].value.toLowerCase() == "inf"
                ||
                parseInt(this.value) == 1 && parseInt(account.childNodes[11].value) == 1
            ){
                readyFunction(this, true)
                readyFunction(account.childNodes[11], true)
            }else{
                readyFunction(this, false)
                readyFunction(account.childNodes[11], false)
            }

            readyCheckFunction(this.parentElement)

        })

        account.childNodes[11].addEventListener("keyup",function(){
            if(
                parseInt(this.value) > parseInt(account.childNodes[9].value) && parseInt(this.value) >= 1 
                || 
                this.value.toLowerCase() == "inf" && account.childNodes[9].value.toLowerCase() == "inf"
                ||
                parseInt(this.value) == 1 && parseInt(account.childNodes[9].value) == 1
            ){
                readyFunction(this, true)
                readyFunction(account.childNodes[9], true)
            }else{
                readyFunction(this, false)
                readyFunction(account.childNodes[9], false)
            }

            readyCheckFunction(this.parentElement)

        })

        for (let index = 1; index < 14; index+=2) {
            
            account.childNodes[index].addEventListener("keyup",function(){

                let thisAccount = this.parentElement

                if(thisAccount.getAttribute("actionLocked") != "locked"){
                    thisAccount.setAttribute("action","update")
                }

                clearTimeout(accountChangerTimer)

                accountChangerTimer = setTimeout(function(){
                    new AccountsController().accountChanger(thisAccount)
                },300)

            })
            
        }

    }

    readyCheck(account){
        if(account.childNodes[3].getAttribute("ready") == "True" && account.childNodes[9].getAttribute("ready") == "True" && account.childNodes[11].getAttribute("ready") == "True"){
            new AccountsController().ready(account, true)
        }else{
            new AccountsController().ready(account, false)
        }
        new AccountsController().defineType(account)
    }

    ready(target, response){
        if(response){
            target.style.borderColor = "green"
            target.setAttribute("ready","True")
        }else{
            target.style.borderColor = "red"
            target.setAttribute("ready","False")
        }
    }

    defineType(account){
        if(parseInt(account.childNodes[9].value) == parseInt(account.childNodes[11].value)){
            account.setAttribute("type","month")
        }
        if(account.childNodes[9].value.toLowerCase() == "inf"){
            account.setAttribute("type","inf")
        }
        if(parseInt(account.childNodes[9].value) < parseInt(account.childNodes[11].value)){
            account.setAttribute("type","months")
        }
    }

    save(){

        let requestObject = {
            "month":[],
            "months":[],
            "inf":[],
        }

        for (let index = 0; index < accountChangerArray.length; index++) {
            if(accountChangerArray[index].getAttribute("ready") == "True"){
                let accountData = new AccountsController().getAccountInfo(accountChangerArray[index])
                requestObject[accountChangerArray[index].getAttribute("type")][requestObject[accountChangerArray[index].getAttribute("type")].length] = accountData
            }
        }

        if(requestObject["month"]){
            ServerRequest.saveMonth(requestObject["month"])
        }

        if(requestObject["months"]){
            for (let index = 0; index < requestObject["months"].length; index++) {
               ServerRequest.saveMonths(requestObject["months"][index])
            }
        }

        if(requestObject["inf"]){
            ServerRequest.saveInf(requestObject["inf"])
        }


    }

    addDeleteTrigger(account){

        account.addEventListener("click",function(){

            if(this.getAttribute("delete") == "true"){

                Accounts.accountChanger(this)
                this.style.display = "none"
                this.setAttribute("action","remove")

                new SumBarController().checkAllAccounts()

            }
        })

    }

    accountsLoad(accounts){
        
        if(accounts){
            for (let index = 0; index < accounts.length; index++) {

                let tempID = accounts[index].ID
                let tempAccount = ""

                if(accounts[index].type == "month" || accounts[index].month == Data.getMonth() && accounts[index].year == Data.getYear()){
                    tempAccount = accountTemplate.replace("{ID}",tempID)
                }else{
                    tempAccount = accountTemplateFrezze.replace("{ID}",tempID)
                }

                this.add(tempAccount, false)

                let tempAccountElement = document.getElementById(tempID)

                tempAccountElement.setAttribute("type",accounts[index].type)

                tempAccountElement.setAttribute("action",accounts[index].flag)

                tempAccountElement.setAttribute("month",accounts[index].month)

                tempAccountElement.setAttribute("year",accounts[index].year)

                tempAccountElement.setAttribute("actionLocked", accounts[index].actionLocked)

                this.accountsBuilder(tempAccountElement, accounts[index])
                    
                if(accounts[index].type == "months"){

                }else if(accounts[index].type == "inf"){
                    tempAccountElement.childNodes[9].value = "INF"
                    tempAccountElement.childNodes[11].value = "INF"

                }else{
                    tempAccountElement.childNodes[9].value = 1
                    tempAccountElement.childNodes[11].value = 1
                }

               new AccountsController().accountsSetState(tempAccountElement, true)

            }
        }

        new SumBarController().checkAllAccounts()
    }

    accountsBuilder(element, account){

        for (let index = 1; index < 14; index+=2) {

            if(account[convertNumberToName[index]]){
                element.childNodes[index].value = account[convertNumberToName[index]]
            }
            
        }

    }

    accountsSetState(account, state){
        new AccountsController().ready(account, state)
        new AccountsController().ready(account.childNodes[3], state)
        new AccountsController().ready(account.childNodes[9], state)
        new AccountsController().ready(account.childNodes[11], state)
    }

    accountChanger(account){
 
        for (let index = 0; index < accountChangerArray.length; index++) {
            if(accountChangerArray[index].getAttribute("id") == account.getAttribute("id")){
                return
            }
        }

        accountChangerArray[accountChangerArray.length] = account

    }

    getAccountInfo(account, detailed = false){

        let accountData = {}

        accountData.flag = account.getAttribute("action")
        accountData.type = account.getAttribute("type")
        accountData.ID = account.getAttribute("id")

        if(detailed){
            accountData.actionLocked = account.getAttribute("actionLocked")
            accountData.month = account.getAttribute("month")
            accountData.year = account.getAttribute("year")
        }
        

        for (let index = 1; index < 14; index+=2) {

            if(account.childNodes[index].value){
                if(defaultActions[index]){
                    accountData[convertNumberToName[index]] = defaultActions[index](account.childNodes[index].value)
                }else{
                    accountData[convertNumberToName[index]] = account.childNodes[index].value
                }
                
            }
            
        }

        return accountData

    }

    getAllAccounts(){
        return document.querySelectorAll(".account")
    }

    getAccountReady(account){
        return account.getAttribute("ready")
    }

}

const Accounts = new AccountsController()
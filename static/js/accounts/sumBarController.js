
import { AccountsController } from "./accountsController.js"

const Accounts = new AccountsController()

export class SumBarController {

    sumBarElement = ""

    constructor(sumBar = document.getElementById("sumBar")){
        this.sumBarElement = sumBar
    }

    checkAllAccounts(){
        
        let allAccounts = Accounts.getAllAccounts()

        let sumResult = 0

        for (let index = 0; index < allAccounts.length; index++) {
            if(allAccounts[index].getAttribute("action") != "remove"){
                if(allAccounts[index].childNodes[3].value){
                    sumResult += parseFloat(allAccounts[index].childNodes[3].value)
                }
            }
        }

        SumBar.setSumBarValue(sumResult)

    }

    setSumBarValue(value){
        this.sumBarElement.innerText = moneyStandard+resumeMoney(value)
    }

}

const SumBar = new SumBarController()
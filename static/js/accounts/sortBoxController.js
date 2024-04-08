
import { AccountsController } from "./accountsController.js"

const Accounts = new AccountsController()

const effectConversor = {"upDown":"downUp","downUp":"upDown"}
const effectColor = {"upDown":"green","downUp":"red"}

const convertSortTypeToNumber = {"sortName":1,"sortValue":3,"sortProduct":5,"sortMethod":7,"sortStart":9,"sortEnd":11,"sortDate":13}

const convertTypeToParser = {"str":parserString, "float":parseFloat, "int":parseInt}

export class SortBoxController {

    sortBoxElement = ""

    constructor(sortBox = document.getElementById("sortBox")){
        this.sortBoxElement = sortBox
    }

    buildTriggers(){

        for (let index = 1; index < 14; index+=2) {
            this.sortBoxElement.childNodes[index].addEventListener("click",function(){

                SortBox.sortReset(this.getAttribute("sortType"))
        
                this.style.borderBottomColor = effectColor[this.getAttribute("sortEffect")]

                this.setAttribute("sortEffect", effectConversor[this.getAttribute("sortEffect")])

                SortBox.sortAccounts(this.getAttribute("sortType"), this.getAttribute("type"), this.getAttribute("sortEffect"))
    
            })
        }

    }

    sortAccounts(sortType, type, sortEffect){

        let values_ID = []

        let allAccounts = Accounts.getAllAccounts()

        for (let index = 0; index < allAccounts.length; index++) {

            if(allAccounts[index].childNodes[convertSortTypeToNumber[sortType]].value != "" && Accounts.getAccountReady(allAccounts[index]) != "False"){

                let value = convertTypeToParser[type](allAccounts[index].childNodes[convertSortTypeToNumber[sortType]].value)

                values_ID[values_ID.length] = [value, allAccounts[index].getAttribute("id")]
                
            }
            
        }

        let finalArray = []

        if(type == "str"){
            finalArray = values_ID.sort(function(a, b){
                return a[0].localeCompare(b[0])
            })
            if(sortEffect == "downUp"){
                finalArray = mirrorArray(finalArray)
            }
        }else{
            if(sortEffect == "upDown"){
                finalArray = values_ID.sort(function(a, b){
                    return b[0] - a[0] 
                })
            }else{
                finalArray = values_ID.sort(function(a, b){
                    return a[0] - b[0]
                })
            }
        }

        let loadArray = []

        for (let index = 0; index < finalArray.length; index++) {
            let tempAccount = document.getElementById(finalArray[index][1])
            loadArray[loadArray.length] = Accounts.getAccountInfo(tempAccount, true)
            tempAccount.parentNode.removeChild(tempAccount)
        }

        Accounts.accountsLoad(loadArray)

    }

    sortReset(ignore){
        let tempAllSortElement = document.querySelectorAll(".sort")

        for (let index = 0; index < tempAllSortElement.length; index++) {
            if(tempAllSortElement[index].getAttribute("id") != ignore){
                tempAllSortElement[index].setAttribute("sortEffect","upDown")
                tempAllSortElement[index].style.borderBottomColor = "gray"
            }
        }
    }

}

function mirrorArray(array){

    let result = []

    for (let index = array.length-1; -1 < index; index--) {
        result[result.length] = array[index]
    }

    return result

}
 
function parserString(value){
    return value.toString()
}

const SortBox = new SortBoxController()
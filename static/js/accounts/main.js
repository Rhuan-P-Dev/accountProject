
import { UIController } from "./UIController.js"
import { DataController } from "./dataController.js"
import { ServerRequestController } from "./serverRequestController.js"
import { KeyBordController } from "./keyBordController.js"
import { SiteController } from "./siteController.js"
import { AccountsController } from "./accountsController.js"
import { SortBoxController } from "./sortBoxController.js"
import { SumBarController } from "./sumBarController.js"

var UI = ""
var Data = ""
var ServerRequest = ""
var KeyBord = ""
var Site = ""
var Accounts = ""
var SortBox = ""
var SumBar = ""

docReady(function(){

    UI = new UIController()
    Data = new DataController()
    ServerRequest = new ServerRequestController()
    KeyBord = new KeyBordController()
    Site = new SiteController()
    Accounts = new AccountsController()
    SortBox = new SortBoxController()
    SumBar = new SumBarController()

    setTimeout(browseInit,1)

    socket.on('from_server', function(msg) {
        if(msg.cmd == "initSite"){

            Data.setYear(msg.year)
            Data.setMonth(msg.month)

            ServerRequest.getAccounts()

        }else if(msg.cmd == "loadAccounts"){

            Accounts.accountsLoad(msg.accounts[0])
            Accounts.accountsLoad(msg.accounts[1])
            Accounts.accountsLoad(msg.accounts[2])

        }
    })

})

function browseInit(){

    UI.buildTriggers()
    KeyBord.buildTriggers()
    Site.buildTriggers()
    SortBox.buildTriggers()

    ServerRequest.getData()

    Site.initStart()

    SumBar.checkAllAccounts()

}

import { DataController } from "./dataController.js"

const Data = new DataController()

export class ServerRequestController{

    getData(){
        socket.send({'cmd': 'getAccountsData'})
    }

    getAccounts(){
        socket.send({'cmd': 'getAccounts', 'year': Data.getYear(), 'month': Data.getMonth()})
    }

    saveMonth(data){
        let request = {'year': Data.getYear(), 'month': Data.getMonth(), 'objects':data, "type":"month"}
        socket.send({'cmd': 'saveMonthObjects', 'data': request})
    }

    saveMonths(data){
        let request = {'year': Data.getYear(),'month': Data.getMonth(), 'objects':[data], 'end':data.end,'start':data.start} // << same group
        socket.send({'cmd': 'saveMonthsObjects', 'data': request})
    }

    saveInf(data){
        let request = {'year': Data.getYear(),'month': Data.getMonth(), 'objects': data}
        socket.send({'cmd': 'saveInfObjects', 'data': request})
    }

}
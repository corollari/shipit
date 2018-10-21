
let contractAddress="0xc1769937adb8e0a8338690acd0325d6fdd87a0a0"

//let web3js = new Web3(web3.currentProvider);

var ShipIt = web3.eth.contract(ABI).at(contractAddress);

function createProject(){
	ShipIt.startCountDown(1, {from: web3.eth.accounts[0], gas: 3000000, value: 1}, function(err, res){});
}

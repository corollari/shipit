
let contractAddress="0xc1769937adb8e0a8338690acd0325d6fdd87a0a0"

//let web3js = new Web3(web3.currentProvider);

var ShipIt = web3.eth.contract(ABI).at(contractAddress);

function createProject(){
	let length=document.querySelector("#message").value;
	let amount=document.querySelector("#money").value;
	ShipIt.startCountDown(length, {from: web3.eth.accounts[0], gas: 3000000, value: 100}, function(err, res){});
}

function estimateLength(){
	let user=document.querySelector("#name").value;
	let repo=document.querySelector("#email").value;
	fetch("/api/"+user+'/'+repo)
		.then(function(response) {
			return response.text();
		}).then(function(txt) {
			document.querySelector("#message").value=txt;
		});
}

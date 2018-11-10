
let contractAddress="0xc1769937adb8e0a8338690acd0325d6fdd87a0a0"

//let web3js = new Web3(web3.currentProvider);

var ShipIt = web3.eth.contract(ABI).at(contractAddress);

function createProject(e){
	let length=document.querySelector("#message").value*3600*24;
	let amount=document.querySelector("#money").value;
	ShipIt.startCountDown(length, {from: web3.eth.accounts[0], gas: 3000000, value: web3.toWei(amount, "ether")}, function(err, res){});
}

function estimateLength(){
	let user=document.querySelector("#name").value;
	let repo=document.querySelector("#email").value;
	fetch("/api/"+user+'/'+repo)
		.then(function(response) {
			return response.text();
		}).then(function(txt) {
			document.querySelector("#message").value=Number(txt)/(3600*24);
		});
}

function loadProjects(){
document.querySelector("#intro .fields").innerHTML="";
ShipIt.getContractsByOwner(web3.eth.accounts[0], (err, res)=>
	{

		console.log(res);
		for(let i=0; i<res.length; i++){
			document.querySelector("#intro .fields").innerHTML+=' <div class="field half">		<label for="proj">Project '+i+'</label><input type="text" id="proj'+i+'" /></div><div class="field half"><label for="name">. </label><button onclick="verify('+i+')">SUBMIT</button></div>'
		}
	}
);
}

function verify(id){
	/*fetch("/api2/"+document.querySelector("#"+id).value)
		.then(function(response) {
			return response.text();
		}).then(function(txt) {
			if(txt=="true"){
				alert("Verified!");
			}
		});
	*/
	let url = document.querySelector("#proj"+id).value;
	ShipIt.verify(id, function(err, res){
		alert("Verified!");
	});
}

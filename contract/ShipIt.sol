pragma solidity ^0.4.24;

contract ShipIt{

	address oracleAddress;

	constructor() public{
		oracleAddress=msg.sender;
	}

	modifier onlyOracle(){
		require(msg.sender==oracleAddress);
		_;
	}

	struct Project{
		address owner;
		uint balance;
		uint deadline;
		bool verified;
	}
	
	Project[] _projects;

	function startCountDown(uint _projectLength) payable external returns (uint){
		_projects.push(Project(msg.sender, msg.value, _projectLength+now, false));
		return _projects.length-1;
	}

	function verify(uint _projectId) external onlyOracle{
		require(_projectId<_projects.length);
		Project storage project=_projects[_projectId];
		require(project.verified==false);
		require(now<=project.deadline);
		project.verified=true;
		project.owner.transfer(project.balance);
	}

	function getContractsByOwner(address _owner) view external returns (uint[]){
		uint length=0;
		for(uint i=0; i<_projects.length; i++){
			if(_projects[i].owner==_owner){
				length++;	
			}
		}
		uint[] memory ownedProjects=new uint[](length);
		uint index=0;
		for(i=0; i<_projects.length; i++){
			if(_projects[i].owner==_owner){
				ownedProjects[index]=i;
				index++;
			}
		}
		return ownedProjects;	
	}
	
	function getProject(uint _projectId) view external returns (uint, uint, bool){
	    Project memory project=_projects[_projectId];
	    return (project.balance, project.deadline, project.verified);
	}
}

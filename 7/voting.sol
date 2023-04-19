pragma solidity >=0.4.22 <0.7.0;

contract Ballot {
    struct Voter{
        uint weight;        // 얼마만큼의 투표권을 가졌는지 (본인 + 위임투표권)
        bool voted;         // 투표했는가
        address delegate;   // 투표권 양도한 사람의 주소
        uint vote;          // 누구에게 투표했는지
    }

    struct Proposal {
        bytes32 name;    // 후보자 이름
        uint voteCount; // 투표수
    }

    address public chairperson; // 선거위원자 주소

    mapping(address => Voter) public voters;    //투표권 가진 사람들의 주소 맵

    Proposal[] public proposals;    // 후보자들

    constructor(bytes32[] memory proposalNames)public{
        chairperson = msg.sender;
        voters[chairperson].weight=1;

        // 후보 등록
        for(uint i = 0; i < proposalNames.length; i++){
            proposals.push(Proposal({
                name: proposalNames[i], voteCount: 0}));
        }
    }
    function giveRightToVote(address voter)public{
        require( msg.sender == chairperson,
        "Only chairperson can give right to vote."
        );
        require( !voters[voter].voted,
        "The voter already voted."
        );
        require(voters[voter].weight == 0);
        voters[voter].weight=1;
    }
    //투표권 양도
    function delegate(address to)public {
        Voter storage sender = voters[msg.sender];
        require(!sender.voted, "You already voted.");   // 투표 여부 확인
        require(to != msg.sender,"No Self-delegation!"); // 자신에게 양도 x

        while(voters[to].delegate != address(0)){       // 투표권 양도하지 않은 사람까지
            to = voters[to].delegate;
            require(to != msg.sender, "Delegation Loop!");  // 자신에게 양도한 사람에게 투표권 양도로 루프에 빠지지 않게
        }

        sender.voted = true;
        sender.delegate=to;
        Voter storage delegate_ = voters[to];
        // 양도받은 자가 이미 투표했다면면
        if(delegate_.voted)
            proposals[delegate_.vote].voteCount += sender.weight;   // 그 사람이 투표한 사람에게 자신이 가진 투표권 만큼 추가 투표
        else // 아직 양도받은 자가 투표 전이라면
            delegate_.weight += sender.weight;  // 자신의 투표권을 넘김김
    }
    function vote (uint proposal) public{
        Voter storage sender = voters[msg.sender];
        require(sender.weight != 0, "Has no right to vote");
        require(!sender.voted,"Already voted.");
        sender.voted = true;
        sender.vote = proposal;
        proposals[proposal].voteCount += sender.weight;
    }

    function getWinner() public view returns (uint winner){
        uint winningVoteCount = 0;
        for(uint p = 0;p<proposals.length;p++){
            if(proposals[p].voteCount > winningVoteCount){
                winningVoteCount = proposals[p].voteCount;
                winner = p;
            }
        }
    }

    function winnerName() public view returns(bytes32 name){
        name = proposals[getWinner()].name;
    }

}



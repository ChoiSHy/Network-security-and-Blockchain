pragma solidity ^0.8.0;

contract Auction2{
    bool isOpen;
    bool finishable;

    uint hope_price;
    uint limit_time;

    address payable owner;

    uint max_price;
    address payable max_bidder;

    mapping(address => uint) ret_map;

    constructor(uint[] memory datas)public {
        require(datas[1] > block.timestamp, "limit time error");
        isOpen=true;
        finishable=false;

        owner = payable(msg.sender);

        hope_price = datas[0];
        limit_time = datas[1];
        max_price=0;
    }

    function bid() public payable{
        require(isOpen,"Auction closed");
        require(block.timestamp <= limit_time, "time out");
        require(msg.value > max_price, "bid more price");
        require(msg.value <=hope_price,"it's too much");

        ret_map[max_bidder] += max_price;

        max_price=msg.value;
        max_bidder = payable(msg.sender);

        emit max_price_renewal(max_price, max_bidder);  
    } 
    function withdraw()public payable{
        require(ret_map[msg.sender] != 0, "there's no balace to withdraw");

        address payable to = payable(msg.sender);
        uint ret_price = ret_map[msg.sender];
        ret_map[msg.sender]=0;
        to.transfer(ret_price);
    }
    function finish() public payable{
        require(owner == msg.sender, "not owner");
        require(isOpen,"it's closed");
        require(block.timestamp >= limit_time || max_price==hope_price,"unsatisfied to terminate");

        emit finish_auction(max_price, max_bidder);
        isOpen=false;
        owner.transfer(max_price);
        max_price=0;
        
    }
    event max_price_renewal(uint price, address bidder_);
    event finish_auction(uint price, address bidder_);
}
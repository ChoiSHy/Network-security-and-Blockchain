pragma solidity ^0.6.0;

contract Auction{
    bool isOpen;
    bool finishable;

    uint hope_price;
    uint limit_time;

    address payable owner;

    uint max_price;
    address payable max_bidder;

    constructor(uint[] memory datas)public {
        require(datas[1] > block.timestamp, "제한 기간 오류");
        isOpen=true;
        finishable=false;

        owner = payable(msg.sender);

        hope_price = datas[0];
        limit_time = datas[1];
        max_price=0;
    }

    function bid() public payable{
        require(isOpen,"경매종료");
        require(now <= limit_time, "경매 기간 지남");
        require(msg.value > max_price, "가격 미달");
        require(msg.value <=hope_price,"희망 가격 초과");

        max_bidder.transfer(max_price);
        max_price=msg.value;
        max_bidder = msg.sender;
        emit max_price_renewal(max_price, max_bidder);  
    } 
    function finish() public payable{
        require(owner == msg.sender, "owner 아님");
        require(isOpen,"경매 종료");
        require(now >= limit_time || max_price==hope_price,"종료 조건 미달");

        emit finish_auction(max_price, max_bidder);
        isOpen=false;
        owner.transfer(max_price);
        max_price=0;
        
    }
    event max_price_renewal(uint price, address bidder_);
    event finish_auction(uint price, address bidder_);
}
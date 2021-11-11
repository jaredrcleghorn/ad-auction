// SPDX-License-Identifier: MIT
pragma solidity 0.8.9;

contract AdAuction {
    string public text;
    string public imageUrl;
    address public owner;
    address public winner;
    mapping(address => uint) public bids;

    event Bid();

    constructor() {
        owner = msg.sender;
    }

    function bid(string memory _text, string memory _imageUrl) public payable {
        uint _bid = bids[msg.sender] + msg.value;

        require(_bid > bids[winner], 'You need to bid more ETH.');

        text = _text;
        imageUrl = _imageUrl;
        winner = msg.sender;
        bids[msg.sender] = _bid;

        emit Bid();
    }

    function withdraw() public {
        require(msg.sender == owner);
        payable(owner).transfer(address(this).balance);
    }
}

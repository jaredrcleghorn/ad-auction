from brownie import chain
from web3.constants import ADDRESS_ZERO

text = 'Test'
imageUrl = 'http://example.com/test.png'
bid = 1

def test_deploy(accounts, ad_auction):
    """
    Test if the contract is correctly deployed.
    """

    assert ad_auction.text() == ''
    assert ad_auction.imageUrl() == ''
    assert ad_auction.owner() == accounts[0].address
    assert ad_auction.winner() == ADDRESS_ZERO

def test_can_bid(accounts, ad_auction):
    """
    Test if an account can bid.
    """

    assert ad_auction.balance() == 0

    tx = ad_auction.bid(text, imageUrl, {'from': accounts[0], 'value': bid})

    assert ad_auction.balance() == bid
    assert ad_auction.text() == text
    assert ad_auction.imageUrl() == imageUrl
    assert ad_auction.winner() == accounts[0].address
    assert ad_auction.bids(accounts[0].address) == bid
    assert 'Bid' in tx.events

def test_can_withdraw(accounts, ad_auction):
    """
    Test if the owner can withdraw.
    """

    ad_auction.bid(text, imageUrl, {'from': accounts[0], 'value': bid})

    assert ad_auction.balance() == bid

    balance_before_withdraw = accounts[0].balance()
    ad_auction.withdraw({'from': accounts[0]})

    assert ad_auction.balance() == 0
    assert accounts[0].balance() == balance_before_withdraw + bid

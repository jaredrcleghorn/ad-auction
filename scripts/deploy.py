from brownie import AdAuction, SolidityStorage, VyperStorage, accounts, network


def main():
    # requires brownie account to have been created
    if network.show_active()=='development':
        # add these accounts to metamask by importing private key
        owner = accounts[0]
        SolidityStorage.deploy({'from':accounts[0]})
        VyperStorage.deploy({'from':accounts[0]})
        AdAuction.deploy({'from': owner})

    elif network.show_active() == 'kovan':
        # add these accounts to metamask by importing private key
        owner = accounts.load("main")
        SolidityStorage.deploy({'from':owner})
        VyperStorage.deploy({'from':owner})
        AdAuction.deploy({'from': owner})

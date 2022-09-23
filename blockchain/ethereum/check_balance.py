from web3 import Web3
infura_url = "https://mainnet.infura.io/v3/20f432fc50224134931fa8d09a03607f"
web3 = Web3(Web3.HTTPProvider(infura_url))
print(web3.isConnected())
print(web3.eth.blockNumber)
balance = web3.eth.getBalance("0x35dDD8Bb810F61F61B9578da42A995CDF3a87f36")
print(balance)
print(web3.fromWei(balance, 'ether'))
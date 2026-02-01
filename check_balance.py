from algosdk.v2client import algod

ALGOD_ADDRESS = "https://testnet-api.algonode.cloud"
ALGOD_TOKEN = ""

client = algod.AlgodClient(ALGOD_TOKEN, ALGOD_ADDRESS)

address = input("Enter your Algorand address: ")

account_info = client.account_info(address)
balance = account_info["amount"]

print("Balance in microAlgos:", balance)
print("Balance in ALGO:", balance / 1_000_000)

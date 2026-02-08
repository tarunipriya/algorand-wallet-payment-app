from algosdk import account, mnemonic
from algosdk.v2client import algod
from algosdk.future.transaction import PaymentTxn

# Connect to Algorand TestNet
algod_address = "https://testnet-api.algonode.cloud"
algod_token = ""

client = algod.AlgodClient(algod_token, algod_address)

# Sender details
sender_mnemonic = "PASTE YOUR 25 WORD MNEMONIC HERE"
sender_private_key = mnemonic.to_private_key(sender_mnemonic)
sender_address = account.address_from_private_key(sender_private_key)

# Receiver address (can be any valid Algorand address)
receiver_address = "PASTE RECEIVER ADDRESS HERE"

# Transaction parameters
params = client.suggested_params()

# Create payment transaction (sending 0.001 Algo)
txn = PaymentTxn(
    sender=sender_address,
    sp=params,
    receiver=receiver_address,
    amt=1000  # microAlgos
)

# Sign transaction
signed_txn = txn.sign(sender_private_key)

# Send transaction
txid = client.send_transaction(signed_txn)
print("Transaction ID:", txid)

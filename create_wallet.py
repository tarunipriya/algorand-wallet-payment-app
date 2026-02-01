from algosdk import account, mnemonic

private_key, address = account.generate_account()
mnemo = mnemonic.from_private_key(private_key)

print("Your Algorand Address:")
print(address)

print("\nSAVE THIS MNEMONIC SAFELY:")
print(mnemo)

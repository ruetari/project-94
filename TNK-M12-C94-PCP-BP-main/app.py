

from flask import Flask, render_template, request
import os
from time import time
from blockchain import BlockChain, Block, Miner
from conversion import getGasPrices

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

chain = BlockChain()
currentBlock = None
failedBlocks = []

miner1 = Miner('Miner 1')
miner2 = Miner('Miner 2')
miner3 = Miner('Miner 3')

chain.addMiner(miner1)
chain.addMiner(miner2)
chain.addMiner(miner3)

@app.route("/", methods= ["GET", "POST"])
def home():
    global blockData, currentBlock, chain, failedBlocks
     
    allPrices = getGasPrices()
        
    if request.method == "GET":
        return render_template('index.html', allPrices = allPrices)
    else:
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        landId = request.form.get("landId")
        lattitude = request.form.get("latitude")
        longitude = request.form.get("longitude")
        area = request.form.get("area")
        amount = request.form.get("amount")
        mode = request.form.get("mode")
        print(mode)

        gasPrices, gweiPrices, etherPrices, dollarPrices = allPrices

        gasPriceGwei = gweiPrices[mode]
        gasPriceEther = etherPrices[mode]
        transactionFeeEther = etherPrices[mode] * 21000
        transactionFeeDollar = dollarPrices[mode] * 21000

        transaction = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
                "landId": landId,  
                "latitude": lattitude,
                "longitude": longitude,
                "area": area,
                "gasPriceGwei" : gasPriceGwei,
                "gasPriceEther" : gasPriceEther, 
                "transactionFeeEther" : transactionFeeEther,
                "transactionfeeDollar" : transactionFeeDollar          
            }  
        # Call chain.addToMiningPool() method with transaction
        chain.addToMiningPool(transaction)
        
    return render_template('index.html', blockChain = chain, allPrices = allPrices)

@app.route("/blockchain", methods= ["GET", "POST"])
def show():
    global chain, currentBlock, failedBlocks

    currentBlockLength  = 0
    if currentBlock:
        currentBlockLength = len(currentBlock.transactions)
    
    return render_template('blockchain.html', blockChain = chain.chain, currentBlockLength = currentBlockLength, failedBlocks= failedBlocks)
    
@app.route("/miningPool", methods= ["GET", "POST"])
def miningPool():
    global chain
    # Check if we get post request via miner's mining form button
    if request.method == "POST":
        # Accept the 'miner' parameter as minerAddress
        minerAddress = request.form.get("miner")
        # Call chain.minePendingTransactions() and pass it minerAddress
        chain.minePendingTransactions(minerAddress)
    # Return the pendingTransactions from chain as pendingTransactions
    return render_template('miningPool.html', pendingTransactions = chain.pendingTransactions, miners = chain.miners)
    
if __name__ == '__main__':
    app.run(debug = True, port=4001)
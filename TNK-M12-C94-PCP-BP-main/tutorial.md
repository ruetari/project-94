PCP

Mine Transactions and Calculate Reward
======================================


In this activity, you will learn to add the pending transactions to the mining pool and add the reward when the miner mines a block.


Follow the given steps to complete this activity:


* Open the file blockchain.py.


* Create a list to store all the pending transactions that are yet to be mined in the init() of the Blockchain class.


    `self.pendingTransactions = []`




* Define a function in the Blockchain class to add a new transaction to the mining pool.


    `def addToMiningPool(self, transaction):`
    
    &emsp;&emsp;`self.pendingTransactions.append(transaction)`
* Define the method for mining pending transactions that takes the miner’s address to identify the miner.


    `def minePendingTransactions(self, minerAddress):`
    
    &emsp;  `for miner in self.miners:`

    &emsp;&emsp;`if miner.address == minerAddress:`

    &emsp;&emsp;&emsp;`currentBlock = miner.createBlock(len(self.chain), self.pendingTransactions)`

    &emsp;&emsp;&emsp;`if(currentBlock):`

    &emsp;&emsp;&emsp;&emsp;`isBlockAdded = self.addBlock(currentBlock)`

    &emsp;&emsp;&emsp;&emsp;`if(isBlockAdded): `

    &emsp;&emsp;&emsp;&emsp;&emsp;`isValid = self.validateBlock(currentBlock)`

    &emsp;&emsp;&emsp;&emsp;&emsp;`currentBlock.isValid = isValid`

    &emsp;&emsp;&emsp;&emsp;&emsp;`self.pendingTransactions = self.pendingTransactions[3:]`

* Call reward() method of the miner object with currentBlock to reward the miner.

	`miner.reward(currentBlock)`


* Open the file app.py.


* Add the new transaction to the mining pool when the buy button is clicked in the home() method.

    `chain.addToMiningPool(transaction)`
 
* Call the mine pending transactions method when the user clicks on the Mine Transactions button inside the miningPool() function.
 
    `if request.method == "POST":`
    
    &emsp;&emsp;`minerAddress = request.form.get("miner")`
    
    &emsp;&emsp;`chain.minePendingTransactions(minerAddress)`
  
* Display the pending transactions on the mining pool web page by rendering the pending transactions list.
 
    `return render_template('miningPool.html', pendingTransactions = chain.pendingTransactions)`  


* Save and run the code to check the output.
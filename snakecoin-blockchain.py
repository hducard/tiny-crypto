#import importlib.machinery
#import importlib.util
#from pathlib import Path

#import snakecoin-block
#import snakecoin-genesis.py
#import snakecoin-new-block

from snakecoingenesis import create_genesis_block
from snakecoinblock import *

# Create Blockchain and add Genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

#length of blockchain
num_of_blocks = 20

#Add blocks to chain
for i in range(0,num_of_blocks):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add
    #print transaction
    print("Block #{} is part of the blockchain", format(block_to_add.index))
    print("Hash: {}\n", format(block_to_add.hash))

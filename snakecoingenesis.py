import datetime as date
from snakecoinblock import *

def create_genesis_block():
    # manually construct a block with index 0 and arb hash value
    return Block(0, date.datetime.now(), "Genesis Block", "0")

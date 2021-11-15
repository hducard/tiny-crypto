import hashlib as hasher
import datetime as date

class Block:
    def __init__ (self, index, timestamp, data, previoushash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previoushash = previoushash
        self.hash = self.hash_block()


    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8')+str(self.timestamp).encode('utf-8')+str(self.data).encode('utf-8')+str(self.previoushash).encode('utf-8'))
        return sha.hexdigest()

def next_block(last_block):
    this_index = last_block.index+1
    this_timestamp = date.datetime.now()
    this_data = "Hey I'm Block "+ str(this_index)
    this_hash = last_block.hash
    return Block(this_index, this_timestamp, this_data, this_hash)

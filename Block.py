# @Author MAYANK YADAV
# This is a simple Block structure - not exactly like a blockchain, but similar.

"""

Here is the structure of the Block

    +---------------------------------+
    |  Hash of the Previous Block     |
    +---------------------------------+
    |           Nonce                 |
    +---------------------------------+
    |       Text information          |
    +---------------------------------+
    |    Hash of the current Block    |
    |    (to have first 4 0 bits)     |
    +---------------------------------+

"""
# criteria = "0000"
import sys
import time
import textwrap
from hashlib import sha256

class Block:
    def __init__(self, criteria, is_first):
        self.is_first = False # by default no block is genesis block
        self.previous_hash = None # string
        self.nonce = None # integer
        self.info = None # string
        self.hash = None # hash of the block itself.
        self.criteria = criteria

        if is_first:
            return self.genesis_block();

    def genesis_block(self):
        self.is_first = True
        self.previous_hash = "0"*64;
        self.nonce = 0;
        self.info = "Genesis Block";
        self.hash = "0"*64;

    def clean_info(self, raw_info):
        # Strip leading/trailing whitespace, replace multiple newlines with one
        clean_text = "\n".join(line.strip() for line in raw_info.strip().splitlines() if line.strip())
        return clean_text


    def mine_block(self, previous_block):
        self.is_first = False
        self.previous_hash = previous_block.hash # string
        self.nonce = 0

        print("Enter data to be saved on Blockchain. Press Ctrl+D (Unix/macOS) or Ctrl+Z then Enter (Windows) to finish.")
        try:
            raw_info = sys.stdin.read()
        except EOFError:
            raw_info = ""

        self.info = self.clean_info(raw_info)

        text = str(self.previous_hash) + str(self.nonce) + str(self.info)
        self.hash =  sha256(text.encode("utf-8")).hexdigest()
        print(f"Mining new block ...")
        start_time = time.time()
        while(not self.hash.startswith(self.criteria)):
            self.nonce += 1
            text = str(self.previous_hash) + str(self.nonce) + str(self.info)
            self.hash =  sha256(text.encode("utf-8")).hexdigest()
        print(f"Mining Successful with Nonce {self.nonce}, in {time.time()-start_time} seconds.")
        return self
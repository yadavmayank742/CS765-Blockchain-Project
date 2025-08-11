# @author Mayank Yadav
# this is to simulate a blockchain
# new block is validated before getting added for current
# hash and must have the hash of previous block

# on every addition, the whole blockchain is validated too.
# on every query, the blockchain is validated too.

from Block import Block;
from hashlib import sha256;
import textwrap

class Blockchain:
    def __init__(self, name=""):
        self.name = name;
        self.chain = [];
        self.criteria = "0000" # SHA256 starting with 4 zeroes.
        self.chain.append(Block(criteria=self.criteria, is_first=True));

    def add_block(self):
        block = Block(criteria = self.criteria, is_first = False);
        new_block = block.mine_block(previous_block = self.chain[-1]);
        if(self.validate_blockchain() and self.validate_new_block(block = new_block)):
            self.chain.append(new_block)

    def validate_blockchain(self):
        """
        validates for the blockchain to be valid
        i.e. does all the blocks are following guidelines or not
        Returns:
            bool: True for valid or False for invalid block
        """
        for num, block in enumerate(self.chain):
            if(not block.is_first):
                # check if it has hash of previous block
                if(block.previous_hash != self.chain[num-1].hash):
                    print(f"Block number {num} has wrong hash of previous block.")
                    return False;

                # check if its own hash is correct or not
                text = str(block.previous_hash) + str(block.nonce) + str(block.info)
                if not sha256(text.encode("utf-8")).hexdigest().startswith(self.criteria):
                    print(f"Block number {num} doesn't satisfy the criteria.")
                    return False

        return True

    def validate_new_block(self, block):
        """
        This is to validate the block for being valid
        Test for:
            1. Valid Previous Block hash
            2. Valid threshold

        Args:
            block (Block): a block to be validated

        Returns:
            bool: True for valid or False for invalid block
        """
        if(block.previous_hash != self.chain[-1].hash):
            return False;

        # calculate hash to meet required criteria (first 4 characters to be zero)
        text = str(block.previous_hash) + str(block.nonce) + str(block.info)
        if not sha256(text.encode("utf-8")).hexdigest().startswith(self.criteria):
            return False

        return True

    def print_block(self, block_num, block):
        width = 89  # total width of the box (including borders)
        content_width = width - 4  # for '|' + 2 spaces on each side

        # Header
        print(f"\n{' ' * 24}Block Number: {block_num}")
        print(f"{' ' * 28}+{'-'*width}+")
        print(f"{' ' * 28}|  Previous Block Hash: {block.previous_hash}")
        print(f"{' ' * 28}+{'-'*width}+")
        print(f"{' ' * 28}|                Nonce: {block.nonce}")
        print(f"{' ' * 28}+{'-'*width}+")

        # Wrap and print info text line by line
        wrapped_text = textwrap.wrap(block.info, width=content_width)
        print(f"{' ' * 28}|                 Text: {wrapped_text[0] if wrapped_text else ''}")
        for line in wrapped_text[1:]:
            print(f"{' ' * 28}|{' ' * 17}{line}")

        print(f"\n{' ' * 28}+{'-'*width}+")
        print(f"{' ' * 28}|            Self Hash: {block.hash}")
        print(f"{' ' * 28}+{'-'*width}+")

    def show_blockchain(self):
        if not self.validate_blockchain():
            print(f"Blockchain is Not valid.")
            return

        print(f"Blockchain: {self.name}")
        for num, block in enumerate(self.chain):
            self.print_block(num, block)

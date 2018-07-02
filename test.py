import zeroone_hash
from binascii import unhexlify, hexlify

import unittest

# zeroone block #1
# user@b1:~/zeroone$ zeroone-cli getblockhash 1
# 000005e9eeef7185898754d08dbfd6ecc167cfa83c4e15dcb1dcc0d79cc13fbf
# user@b1:~/zeroone$ zeroone-cli getblock 000005e9eeef7185898754d08dbfd6ecc167cfa83c4e15dcb1dcc0d79cc13fbf
# {
#  "hash": "000005e9eeef7185898754d08dbfd6ecc167cfa83c4e15dcb1dcc0d79cc13fbf",
#  "confirmations": 80391,
#  "size": 179,
#  "height": 1,
#  "version": 536870912,
#  "merkleroot": "a4298441592013a2b6265ac312aebc245fe53b3ce2c243598c89c4f70f17e6ae",
#  "tx": [
#    "a4298441592013a2b6265ac312aebc245fe53b3ce2c243598c89c4f70f17e6ae"
#  ],
#  "time": 1517407356,
#  "mediantime": 1517407356,
#  "nonce": 80213,
#  "bits": "1e0ffff0",
#  "difficulty": 0.000244140625,
#  "chainwork": "0000000000000000000000000000000000000000000000000000000000200020",
#  "previousblockhash": "00000c8e2be06ce7e6ea78cd9f6ea60e22821d70f8c8fbb714b6baa7b4f2150c",
#  "nextblockhash": "00000aeb1683851ca7b40dea400cafe986116d904a93bae004341ea52a0930ab"
# }

header_hex = ("00000020" + # version
    "0c15f2b4a7bab614b7fbc8f8701d82220ea66e9fcd78eae6e76ce02b8e0c0000" + # reverse-hex previousblockhash
    "aee6170ff7c4898c5943c2e23c3be55f24bcae12c35a26b6a2132059418429a4" + # reverse-hex merkleroot
    "7ccc715a" + # reverse-hex time
    "f0ff0f1e" + # reverse-hex bits
    "55390100")  # reverse-hex nonce

best_hash = '434341c0ecf9a2b4eec2644cfadf4d0a07830358aed12d0ed654121dd9070000' # reverse-hex block hash

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.block_header = unhexlify(header_hex)
        self.best_hash = best_hash

    def test_zeroone_hash(self):
        self.pow_hash = hexlify(zeroone_hash.getPoWHash(self.block_header))
        self.assertEqual(self.pow_hash.decode(), self.best_hash)


if __name__ == '__main__':
    unittest.main()


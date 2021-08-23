import unittest
from src.crypto import Crypto


class TestCrypto(unittest.TestCase):
    test_environment = dict()
    test_environment["api_key"] = "test_api_key"
    test_environment["api_secret"] = "test_api_secret"
    test_environment["currency"] = "CAD"
    test_environment["cryptos"] = ["XLM"]

    def test_crypto_instantiation(self):
        crypto_test = Crypto(self.test_environment)
        assert(crypto_test.api_key == self.test_environment["api_key"]
               and crypto_test.api_secret == self.test_environment["api_secret"])
        assert(crypto_test.currency == self.test_environment["currency"]
               and crypto_test.cryptos == self.test_environment["cryptos"])

    def test_coinbase_connection_success(self):
        crypto_test = Crypto(self.test_environment)
        crypto_test.connect_coinbase()

    def test_coinbase_connection_failure(self):
        empty_environment = {"api_key": "", "api_secret": "", "currency": "", "cryptos": ""}
        crypto_test = Crypto(empty_environment)
        self.assertRaises(ValueError, crypto_test.connect_coinbase)


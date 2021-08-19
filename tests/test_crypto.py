import unittest
from src.crypto import Crypto


class TestCrypto(unittest.TestCase):
    def test_crypto_instantiation(self):
        crypto_test = Crypto("test_api_key", "test_secret_key", "test_currency", "[test_list]")
        assert(crypto_test.api_key == "test_api_key" and crypto_test.api_secret == "test_secret_key")
        assert(crypto_test.currency == "test_currency" and crypto_test.cryptos == "[test_list]")

    def test_coinbase_connection_success(self):
        crypto_test = Crypto("test_api_key", "test_secret_key", "test_currency", "[test_list]")
        crypto_test.connect_coinbase()

    def test_coinbase_connection_failure(self):
        crypto_test = Crypto("", "", "", "")
        self.assertRaises(ValueError, crypto_test.connect_coinbase)

    def test_get_crypto_for_one_crypto(self):
        crypto_test = Crypto("test_api_key", "test_secret_key", "USD", ["XLM"])

        test_client = crypto_test.connect_coinbase()
        assert(len(crypto_test.get_crypto_price(test_client)) == 1)

    def test_get_crypto_for_multiple_crypto(self):
        crypto_test = Crypto("test_api_key", "test_secret_key", "USD", ["XLM", "BTC", "ETH", "ADA"])

        test_client = crypto_test.connect_coinbase()
        assert(len(crypto_test.get_crypto_price(test_client)) == 4)



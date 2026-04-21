"""Tests for ErrorFrameworkCryptocom."""

from __future__ import annotations

from bt_api_cryptocom.errors.cryptocom_translator import CryptoComErrorTranslator


class TestCryptoComErrorTranslator:
    """Tests for CryptoComErrorTranslator."""

    def test_error_map_exists(self):
        """Test ERROR_MAP is defined."""
        assert hasattr(CryptoComErrorTranslator, "ERROR_MAP")

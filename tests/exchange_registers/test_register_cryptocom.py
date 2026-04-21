"""Tests for exchange_registers/register_cryptocom.py."""

from __future__ import annotations

from bt_api_cryptocom.registry_registration import register_cryptocom


class TestRegisterCryptocom:
    """Tests for Crypto.com registration module."""

    def test_module_imports(self):
        """Test module can be imported."""
        assert register_cryptocom is not None

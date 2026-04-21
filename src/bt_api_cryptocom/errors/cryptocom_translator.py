from bt_api_base.error import ErrorTranslator, UnifiedError, UnifiedErrorCode


class CryptoComErrorTranslator(ErrorTranslator):
    ERROR_MAP = {
        0: (None, "Success"),
        10001: (UnifiedErrorCode.INTERNAL_ERROR, "System error"),
        10002: (UnifiedErrorCode.INVALID_PARAMETER, "Invalid parameter"),
        10003: (UnifiedErrorCode.IP_BANNED, "IP not authorized"),
        10004: (UnifiedErrorCode.INVALID_API_KEY, "Invalid API key"),
        10005: (UnifiedErrorCode.INVALID_SIGNATURE, "Invalid signature"),
        10006: (UnifiedErrorCode.EXPIRED_TIMESTAMP, "Timestamp expired"),
        10007: (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Request too frequent"),
        10008: (UnifiedErrorCode.PERMISSION_DENIED, "Insufficient permissions"),
        20001: (UnifiedErrorCode.INSUFFICIENT_BALANCE, "Insufficient balance"),
        20007: (UnifiedErrorCode.ORDER_NOT_FOUND, "Order not found"),
        30003: (UnifiedErrorCode.INVALID_SYMBOL, "Symbol not exists"),
        30004: (UnifiedErrorCode.PRECISION_ERROR, "Price precision error"),
        30005: (UnifiedErrorCode.INVALID_VOLUME, "Quantity precision error"),
        30006: (UnifiedErrorCode.MIN_NOTIONAL, "Minimum notional not met"),
    }

    HTTP_STATUS_MAP = {
        400: (UnifiedErrorCode.INVALID_PARAMETER, "Bad request"),
        401: (UnifiedErrorCode.INVALID_API_KEY, "Unauthorized"),
        403: (UnifiedErrorCode.PERMISSION_DENIED, "Forbidden"),
        404: (UnifiedErrorCode.ORDER_NOT_FOUND, "Not found"),
        429: (UnifiedErrorCode.RATE_LIMIT_EXCEEDED, "Too many requests"),
        500: (UnifiedErrorCode.INTERNAL_ERROR, "Internal server error"),
        503: (UnifiedErrorCode.EXCHANGE_OVERLOADED, "Service unavailable"),
    }

    @classmethod
    def translate(cls, raw_error: dict, venue: str) -> UnifiedError | None:
        error = raw_error.get("error", raw_error)
        code = error.get("code")
        msg = error.get("message", error.get("description", ""))

        if code is not None and code in cls.ERROR_MAP:
            unified_code, default_msg = cls.ERROR_MAP[code]
            if unified_code is None:
                return None
            return UnifiedError(
                code=unified_code,
                category=cls._get_category(unified_code),
                venue=venue,
                message=msg or default_msg,
                original_error=f"{code}: {msg}",
                context={"raw_response": raw_error},
            )

        status = error.get("status")
        if status and status in cls.HTTP_STATUS_MAP:
            unified_code, default_msg = cls.HTTP_STATUS_MAP[status]
            return UnifiedError(
                code=unified_code,
                category=cls._get_category(unified_code),
                venue=venue,
                message=msg or default_msg,
                original_error=f"HTTP {status}: {msg}",
                context={"raw_response": raw_error},
            )

        return UnifiedError(
            code=UnifiedErrorCode.INTERNAL_ERROR,
            category=cls._get_category(UnifiedErrorCode.INTERNAL_ERROR),
            venue=venue,
            message=msg or "Unknown error",
            original_error=str(raw_error),
            context={"raw_response": raw_error},
        )

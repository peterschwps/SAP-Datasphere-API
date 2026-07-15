import asyncio


class DatasphereException(Exception):
    """
    Common base class for all exceptions raised by this library.
    """


class AuthenticationFailed(DatasphereException):
    pass


class InvalidConfiguration(DatasphereException):
    pass


class MissingCredentials(DatasphereException):
    def __init__(self) -> None:
        super().__init__(
            "Client secret not found. Please provide a client secret in "
            "the configuration."
        )


class UnexpectedResponse(DatasphereException):
    pass


class TaskChainTimeout(DatasphereException):
    """
    Raised when a started task chain does not finish in time.
    """

    def __init__(self, chain: str, space: str, log_id: int) -> None:
        self.chain = chain
        self.space = space
        self.log_id = log_id
        super().__init__(
            f"Task chain '{chain}' in '{space}' exceeded its timeout "
            f"(log ID: {log_id})."
        )


class TaskChainCancelled(asyncio.CancelledError):
    """
    Raised when local polling is cancelled after a chain started.
    """

    def __init__(self, chain: str, space: str, log_id: int) -> None:
        self.chain = chain
        self.space = space
        self.log_id = log_id
        super().__init__(
            f"Local polling for task chain '{chain}' in '{space}' was "
            f"cancelled; the remote run may continue (log ID: {log_id})."
        )

from PyMyGekko import MyGekkoApiClientBase

class MyGekkoLocalApiClient(MyGekkoApiClientBase):
    """The api client to access MyGekko locally."""

    def __init__(
        self,
        username: str,
        password: str,
        session: ClientSession,
        host: str,
        scheme: str,
    ) -> None:
        super().__init__(
            authentication_params={
                "username": username,
                "password": password,
            },
            session=session,
            host=host,
            scheme=scheme,
        )

class Error(Exception):
    def __init__(
        self,
        ui_message="algo deu errado",
        internal_message="Internal Server Error",
        status_code=500,
    ):
        self.ui_message = ui_message
        self.internal_message = internal_message
        self.status_code = status_code

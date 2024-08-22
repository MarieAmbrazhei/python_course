from requests import Response


class ResponseError:
    """
    The ResponseError class is designed to extract and store error messages
    from an HTTP response object.
    """

    def __init__(self, response: Response):
        """
       Initializes the ResponseError instance by extracting the 'error' field
       from the JSON content of the provided response object.
       """
        self.error_message = response.json().get('error')

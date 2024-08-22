import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('TOKEN')


class Headers:
    """
    The Headers class is responsible for providing the necessary HTTP headers
    for making requests to the API. Currently, it includes the basic authorization
    header that uses a bearer token.
    """
    basic = {
        "Authorization": f"Bearer {token}"
    }

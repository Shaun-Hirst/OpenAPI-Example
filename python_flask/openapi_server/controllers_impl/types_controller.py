# pylint: disable=E0401
# E0401: Unable to import

"""controller example for handling different types."""

from datetime import datetime
from uuid import uuid4
import random
from flask import send_file

from openapi_server.models.simple import Simple  # noqa: E501


def get_example_string():  # noqa: E501
    """Your GET endpoint

    Get string # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return "Hello World", 200


def get_examples_datetime():  # noqa: E501
    """Your GET endpoint

    get date time # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return datetime.now(), 200


def get_examples_file():  # noqa: E501
    """Your GET endpoint

    get file # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return_obj = {"Content-Disposition":
                  "attachment; filename=\"example.txt\"",
                  "content-type": "application/octet-stream"}

    result = send_file("test_files/example.txt"), 200, return_obj

    return result


def get_examples_float():  # noqa: E501
    """Your GET endpoint
    get float/double # noqa: E501


    :rtype: Union[float, Tuple[float, int], Tuple[float, int, Dict[str, str]]
    """
    return random.uniform(10.5, 75.5) ,200

def get_examples_integer():  # noqa: E501
    """Your GET endpoint

    get integer # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return random.getrandbits(16), 200


def get_examples_model():  # noqa: E501
    """Your GET endpoint
    get model # noqa: E501


    :rtype: Union[Simple, Tuple[Simple, int], Tuple[Simple, int, Dict[str, str]]
    """
    return Simple(id=uuid4(), name="test", created=datetime.now()), 200


def get_examples_modelarray():  # noqa: E501
    """Your GET endpoint

    get array or models # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    results = []
    for num in range(10):
        results.append(
            Simple(id=uuid4(), name="test-" + str(num+1), created=datetime.now())
            )

    return results, 200


def get_examples_number():  # noqa: E501
    """Your GET endpoint

    get number # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return random.getrandbits(64), 200


def get_examples_uuid():  # noqa: E501
    """Your GET endpoint

    get uuid # noqa: E501


    :rtype: Union[object, Tuple[object, int], Tuple[object, int, Dict[str, str]]
    """
    return uuid4(), 200


def get_types_boolean():  # noqa: E501
    """Your GET endpoint
    get boolean # noqa: E501


    :rtype: Union[bool, Tuple[bool, int], Tuple[bool, int, Dict[str, str]]
    """

    return bool(random.getrandbits(1))

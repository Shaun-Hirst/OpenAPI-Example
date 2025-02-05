"""controller implimentation for types"""
from datetime import datetime
from uuid import uuid4
from typing import List
import random

from openapi_server.models.simple import Simple
from openapi_server.apis.types_controller_impl_base import BaseTypesControllerImpl


class BaseTypesControllerImpl(BaseTypesControllerImpl):
    """implimentation of controller methods"""
    async def get_example_string(
        self,
    ) -> str:
        """get string"""
        return (200, "Hello World")

    async def get_examples_datetime(
        self,
    ) -> datetime:
        """get datetime"""
        return (200, datetime.now())

    async def get_examples_float(
        self,
    ) -> float:
        """get float/double"""
        return (200, random.uniform(10.5, 75.5))


    async def get_examples_integer(
        self,
    ) -> int:
        """get integer"""
        return (200, random.getrandbits(16))


    async def get_examples_model(
        self,
    ) -> Simple:
        """get model"""
        model = Simple(id=uuid4(), name="test", created=datetime.now())
        return (200, model)


    async def get_examples_modelarray(
        self,
    ) -> List[Simple]:
        """get array or models"""
        results = []
        for num in range(10):
            results.append(
                Simple(id=uuid4(), name="test-" + str(num+1), created=datetime.now())
                )
        return (results, 200)

    async def get_examples_number(
        self,
    ) -> float:
        """get number"""
        return (200, random.getrandbits(64))


    async def get_examples_uuid(
        self,
    ) -> str:
        """get uuid"""
        return (200, uuid4())


    async def get_types_boolean(
        self,
    ) -> bool:
        """get boolean"""
        return (200, bool(random.getrandbits(1)))

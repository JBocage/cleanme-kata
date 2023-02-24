from pydantic import BaseModel


class ExamplePayload(BaseModel):
    """An example payload schema"""

    first_number: int
    second_number: int

from pydantic import BaseModel, Field


class Address(BaseModel):
    city: str = Field(..., example="taipei-city")
    district: str = Field(..., example="da-an-district")
    street: str = Field(..., example="fuxing-south-road")


class Order(BaseModel):
    id: str = Field(..., example="A0000001")
    name: str = Field(..., example="Melody Holiday Inn")
    address: Address
    price: float = Field(..., example=250)
    currency: str = Field(..., example="TWD")

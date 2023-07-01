import pydantic


class CreateContactValidation(pydantic.BaseModel):
    name: str
    surname: str = ""

    phone_number: str

    message_text: str

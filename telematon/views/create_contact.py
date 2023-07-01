from telematon.utils import create_contact, get_contact, send_message
from telematon.validation.create_contact import CreateContactValidation

from .base import BaseJSONView


class CreateContactView(BaseJSONView):
    def process_data(self):
        json_input: dict = self.json_data

        data = CreateContactValidation(**json_input)

        user = None
        contacts = create_contact(data.phone_number, data.name, data.surname)
        if not contacts.users:
            user = get_contact(data.phone_number)
        else:
            user = contacts.users[0]

        if not user:
            return {"message": "User not found", "status": "error"}, 404

        send_message(user.id, data.message_text)

        return {
            "message": f"Message sent to: {data.name} {data.surname}",
            "status": "success",
        }

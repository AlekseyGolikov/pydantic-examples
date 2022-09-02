
from pydantic import BaseModel
from typing import Dict


class User(BaseModel):
    name: str
    birth: str
    age: int
    address: Dict


input_data = {
    'name': 'Alex',
    'birth': '10.04.1987',
    'age': 35,
    'address': {
        'id': 610025,
        'city': 'Kirov',
        'street': 'Mostovickay'
    }
}


if __name__ == '__main__':
    user = User(**input_data)
    print(user)
    print(user.address['city'])

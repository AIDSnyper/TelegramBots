from aiogram.dispatcher.filters.state import State, StatesGroup


class PersonalData(StatesGroup):
    name = State()
    lname = State()
    email = State()
    phone = State()

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from states.personalData import PersonalData
from loader import dp
from aiogram.dispatcher import FSMContext
from keyboards.default.contact import contactru
from keyboards.inline.key import categoryMenu
from aiogram.types import ReplyKeyboardRemove


@dp.message_handler(CommandStart(), state=None)
async def enter_test(message: types.Message):
    await message.answer("https://t.me/petnovostroyki/2148")
#     await message.answer("""Здравствуйте! 
# Мы рады, что наш пост вас заинтересовал. 🙂

# Выберите удобный способ консультации:
# - Напишите нашим менеджерам в чат @managerpn_bot  👩🏼‍💻👨🏻‍💻
# - Нажмите кнопку «Заказать обратный звонок» или оставьте свой номер телефона сообщением ниже ⬇️""")
    await message.answer("Пожалуста введите своё имя")
    await PersonalData.fullName.set()


@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state: FSMContext):
    fullname = message.text

    await state.update_data(
        {"name": fullname}
    )

    await message.answer("""Нажмите кнопку '📲 Поделиться контактом'""", reply_markup=contactru)

    await PersonalData.next()

@dp.message_handler(content_types=types.ContentType.CONTACT, state=PersonalData.phoneNum)
async def answer_email(message: types.Message, state: FSMContext):
    contact = message.contact
    phone_number = contact.phone_number
    await state.update_data({"phone": phone_number})

    await message.answer("Пожалуста введите свой вопрос")

    await PersonalData.next()


@dp.message_handler(state=PersonalData.question)
async def answer_phone(message: types.Message, state: FSMContext):
    question = message.text

    await state.update_data({"question": question})
    data = await state.get_data()
    name = data.get("name")
    phone = data.get("phone")
    question = data.get("question")

    msg = "Была получена следующая информация:\n"
    msg += f"Ваше имя - {name}\n"
    msg += f"Телефон: - {phone}\n"
    msg += f"Вопрос - {question}"
    await message.answer(msg, reply_markup=ReplyKeyboardRemove())
    await message.answer("Спасибо! Менеджер свяжется с Вами в ближайшее время ❤️")
    await state.finish()

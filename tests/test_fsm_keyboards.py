import pytest

from bale.fsm import FSMContext, MemoryStorage, State, StatesGroup
from bale.keyboards import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)


class OrderStates(StatesGroup):
    waiting_for_name = State()
    waiting_for_address = State()


@pytest.mark.asyncio
async def test_fsm_memory_storage() -> None:
    storage = MemoryStorage()
    ctx = FSMContext(storage, chat_id=123, user_id=456)

    assert await ctx.get_state() is None

    await ctx.set_state(OrderStates.waiting_for_name)
    assert await ctx.get_state() == "OrderStates:waiting_for_name"

    await ctx.set_data({"item": "book"})
    await ctx.update_data(quantity=2)

    data = await ctx.get_data()
    assert data == {"item": "book", "quantity": 2}

    await ctx.clear()
    assert await ctx.get_state() is None
    assert await ctx.get_data() == {}


def test_inline_keyboard_markup_builder() -> None:
    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("Button 1", callback_data="btn_1"),
        InlineKeyboardButton("Website", url="https://bale.ai"),
    )
    d = kb.to_dict()
    assert "inline_keyboard_markup" in d
    rows = d["inline_keyboard_markup"]["list_of_inline_list"]
    assert len(rows) == 1
    buttons = rows[0]["inline_list"]
    assert len(buttons) == 2
    assert buttons[0]["text"] == "Button 1"
    assert buttons[0]["callback_data"] == {"value": "btn_1"}
    assert buttons[1]["url"] == {"value": "https://bale.ai"}


def test_reply_keyboard_markup_builder() -> None:
    kb = ReplyKeyboardMarkup()
    kb.row(
        KeyboardButton("ارسال شماره تماس", request_contact=True),
        KeyboardButton("ارسال موقعیت", request_location=True),
    )
    d = kb.to_dict()
    assert "reply_keyboard_markup" in d
    rows = d["reply_keyboard_markup"]["list_of_keyboard_list"]
    assert len(rows) == 1
    assert rows[0]["keyboard_list"][0]["request_contact"] == {"value": True}

    remove = ReplyKeyboardRemove()
    assert remove.to_dict() == {"reply_keyboard_remove": {"remove_keyboard": True}}

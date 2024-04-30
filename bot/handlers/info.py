from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _
from aiogram.types import BufferedInputFile

import plotly.express as px

router = Router(name="info")


@router.message(Command(commands=["info", "help", "about"]))
async def info_handler(message: types.Message) -> None:
    """Information about bot."""
    df = px.data.wind()
    fig = px.bar_polar(df, r="frequency", theta="direction",
                   color="strength", template="plotly_dark",
                   color_discrete_sequence= px.colors.sequential.Plasma_r)
    img_bytes = fig.to_image(format="png")
    # test reply with image
    await message.answer_photo(BufferedInputFile(img_bytes, filename="plot.png"), caption=_("about"))

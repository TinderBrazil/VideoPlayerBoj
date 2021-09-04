"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import asyncio
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "👋🏻 **Oi [{}](tg://user?id={})**, \n\nI'm **TioMortyBot**. \nPosso transmitir vídeos no chat de voz do Telegram do YouTube e arquivos de vídeo do Telegram 😉! \n\n**Feito com ❤️ By @TiuMorty!** 👑"
HELP_TEXT = """
🏷️ --**Configurando**-- :

\u2022 Inicie um bate-papo por voz em seu canal ou grupo.
\u2022 Adicionar bot e conta de usuário no chat com direitos de administrador.
\u2022 Use /stream [youtube link] or /stream como uma resposta a um arquivo de vídeo.

🏷️ --**Comandos Comun**-- :

\u2022 `/start` - inicie o bot
\u2022 `/help` - mostre a mensagem de ajuda

🏷️ --**Comandos apenas de administradora**-- :

\u2022 `/stream` - comece a transmitir o vídeos
\u2022 `/mute` - silenciar o usuário no bate-papo por voz
\u2022 `/unmute` - ativar o som do usuário no bate-papo por voz
\u2022 `/endstream` - fim do fluxo atual e vc esquerdo

© **Powered By** : 
**@TioMorty | @TiuMorty** 👑
"""


@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/TiuMorty"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/TioMorty"),
            ],
            [
                InlineKeyboardButton("BACK HOME", callback_data="home"),
                InlineKeyboardButton("CLOSE MENU", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("HOW TO USE", callback_data="help"),
            ],
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/TiuMorty"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/TioMorty"),
            ],
            [
                InlineKeyboardButton("CLOSE MENU", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("HOW TO USE", callback_data="help"),
            ],
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/TiuMorty"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/TioMorty"),
            ],
            [
                InlineKeyboardButton("CLOSE MENU", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("CHANNEL", url="https://t.me/TiuMorty"),
                InlineKeyboardButton("SUPPORT", url="https://t.me/TioMorty"),
            ],
            [
                InlineKeyboardButton("BACK HOME", callback_data="home"),
                InlineKeyboardButton("CLOSE MENU", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)

# SCP-079-CONFIG - Manage the settings of each bot
# Copyright (C) 2019 SCP-079 <https://scp-079.org>
#
# This file is part of SCP-079-CONFIG.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import logging
from time import sleep
from typing import Optional, Union

from pyrogram import Client, InlineKeyboardMarkup, Message, ParseMode
from pyrogram.errors import FloodWait

logger = logging.getLogger(__name__)


def answer_callback(client: Client, query_id: str, text: str) -> Optional[bool]:
    result = None
    try:
        while not result:
            try:
                result = client.answer_callback_query(
                    callback_query_id=query_id,
                    text=text
                )
            except FloodWait as e:
                sleep(e.x + 1)
    except Exception as e:
        logger.warning(f"Answer query to {query_id} error: {e}", exc_info=True)

    return result


def edit_message_reply_markup(client: Client, cid: int, mid: int,
                              markup: InlineKeyboardMarkup) -> Optional[Union[bool, Message]]:
    result = None
    try:
        while not result:
            try:
                result = client.edit_message_reply_markup(
                    chat_id=cid,
                    message_id=mid,
                    reply_markup=markup
                )
            except FloodWait as e:
                sleep(e.x + 1)
    except Exception as e:
        logger.warning(f"Edit message reply markup error: {e}", exc_info=True)

    return result


def edit_message_text(client: Client, cid: int, mid: int, text: str,
                      markup: InlineKeyboardMarkup = None) -> Optional[Message]:
    result = None
    try:
        if text.strip():
            while not result:
                try:
                    result = client.edit_message_text(
                        chat_id=cid,
                        message_id=mid,
                        text=text,
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True,
                        reply_markup=markup
                    )
                except FloodWait as e:
                    sleep(e.x + 1)
    except Exception as e:
        logger.warning(f"Edit message in {cid} error: {e}", exc_info=True)

    return result


def send_message(client: Client, cid: int, text: str, mid: int = None,
                 markup: InlineKeyboardMarkup = None) -> Optional[Message]:
    result = None
    try:
        if text.strip():
            while not result:
                try:
                    result = client.send_message(
                        chat_id=cid,
                        text=text,
                        parse_mode=ParseMode.MARKDOWN,
                        disable_web_page_preview=True,
                        reply_to_message_id=mid,
                        reply_markup=markup
                    )
                except FloodWait as e:
                    sleep(e.x + 1)
    except Exception as e:
        logger.warning(f"Send message to {cid} error: {e}", exc_info=True)

    return result

#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class GetInlineGameHighScores(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``158``
        - ID: ``F635E1B``

    Parameters:
        id (:obj:`InputBotInlineMessageID <nan_dev.raw.base.InputBotInlineMessageID>`):
            N/A

        user_id (:obj:`InputUser <nan_dev.raw.base.InputUser>`):
            N/A

    Returns:
        :obj:`messages.HighScores <nan_dev.raw.base.messages.HighScores>`
    """

    __slots__: List[str] = ["id", "user_id"]

    ID = 0xf635e1b
    QUALNAME = "functions.messages.GetInlineGameHighScores"

    def __init__(self, *, id: "raw.base.InputBotInlineMessageID", user_id: "raw.base.InputUser") -> None:
        self.id = id  # InputBotInlineMessageID
        self.user_id = user_id  # InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetInlineGameHighScores":
        # No flags
        
        id = TLObject.read(b)
        
        user_id = TLObject.read(b)
        
        return GetInlineGameHighScores(id=id, user_id=user_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.id.write())
        
        b.write(self.user_id.write())
        
        return b.getvalue()

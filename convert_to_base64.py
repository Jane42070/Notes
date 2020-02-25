#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import base64, pyperclip
"""
    Convert pictures to base64 enc, safe and easy.
"""
# picture = input("Picture's full directory:")

# Open picture as binary source
with open("./Modern_Chinese_History/中国近现代史的分期.jpg", mode="rb") as f:
    Data = base64.b64encode(f.read())
    # Save base64 binary source to clipboard
    str_Data = str(Data)
    pyperclip.copy(str_Data)
    print("Convert to bases64:\n%s" % pyperclip.paste())
    f.close()

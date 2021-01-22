# -*- coding: utf-8 -*-

import sublime


# 半全角配置
AngleConf = {
    "half": {
        "，": ",",
        "。": ".",
        "？": "?",
        "！": "!",
        "、": ",",
        "；": ";",
        "：": ":",
        "“": "\"",
        "”": "\"",
        "‘": "'",
        "’": "'",
        "（": "(",
        "）": ")",
        "《": "<",
        "》": ">",
        "〈": "<",
        "〉": ">",
        "【": "[",
        "】": "]",
        "～": "~",
    },
    "full": {
        ",": "，",
        ".": "。",
        "?": "？",
        "!": "！",
        ":": "：",
        ";": "；",
        "\"": "“",
        "'": "‘",
        "(": "（",
        ")": "）",
        "<": "《",
        ">": "》",
        "[": "【",
        "]": "】",
        "~": "～",
    }
}


# GetSetting 获取插件配置
def GetSetting(key):
    return sublime.load_settings('TonyWater.sublime-settings').get(key)

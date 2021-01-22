# -*- coding: utf-8 -*-

import sublime
import sublime_plugin
import json
import hashlib
import time
import urllib.parse
import os
import operator
from .json2go import JSON2Go
from .base import AngleConf, GetSetting


# --------------------------------


# TonyJsonPrettyCommand json 格式化
class TonyJsonPrettyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = json.dumps(json.loads(text), 4, False, False)
        self.view.replace(edit, self.view.sel()[0], res)


# TonyJsonMinifyCommand json 最小化
class TonyJsonMinifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = json.dumps(json.loads(text))
        self.view.replace(edit, self.view.sel()[0], res)


# --------------------------------


# TonyTimestampToDateCommand 时间戳转日期 e.g. 1577808000 => 2020-01-01 00:00:00
class TonyTimestampToDateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(text)))
        self.view.replace(edit, self.view.sel()[0], res)


# TonyDateToTimestampCommand 日期转时间戳 e.g. 2020-01-01 00:00:00 => 1577808000
class TonyDateToTimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = str(int(time.mktime(time.strptime(text, '%Y-%m-%d %H:%M:%S'))))
        self.view.replace(edit, self.view.sel()[0], res)


# TonyTimestampCommand 当前时间戳 e.g. 1577808000
class TonyTimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        res = str(int(time.time()))
        self.view.replace(edit, self.view.sel()[0], res)


# --------------------------------


# TonyToUpperCommand 转大写 e.g. abc => ABC
class TonyToUpperCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.upper()
        self.view.replace(edit, self.view.sel()[0], res)


# TonyToLowerCommand 转小写 e.g. Abc => abc
class TonyToLowerCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.lower()
        self.view.replace(edit, self.view.sel()[0], res)


# TonyHalfAngleCommand 转半角 e.g. 。 => .
class TonyHalfAngleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text
        for chr in AngleConf["half"]:
            res = res.replace(chr, AngleConf["half"][chr])
        self.view.replace(edit, self.view.sel()[0], res)


# TonyFullAngleCommand 转全角 e.g. . => 。
class TonyFullAngleCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text
        for chr in AngleConf["full"]:
            res = res.replace(chr, AngleConf["full"][chr])
        self.view.replace(edit, self.view.sel()[0], res)


# --------------------------------


# TonyStringEscapeCommand 转义 e.g. " to \"
class TonyStringEscapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.replace('"', '\\"', text.count('"'))
        self.view.replace(edit, self.view.sel()[0], res)


# TonyStringUnescapeCommand 反转义 e.g. \" to "
class TonyStringUnescapeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.replace('\\"', '"', text.count('"'))
        self.view.replace(edit, self.view.sel()[0], res)


# TonyUrlEncodeCommand ...
class TonyUrlEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = urllib.parse.quote(text)
        self.view.replace(edit, self.view.sel()[0], res)


# TonyUrlDecodeCommand ...
class TonyUrlDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = urllib.parse.unquote(text)
        self.view.replace(edit, self.view.sel()[0], res)


# TonyUnicodeEncodeCommand ...
class TonyUnicodeEncodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.encode('unicode_escape').decode("utf-8")
        self.view.replace(edit, self.view.sel()[0], res)


# TonyUnicodeDecodeCommand ...
class TonyUnicodeDecodeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = text.encode('utf8').decode('unicode_escape')
        self.view.replace(edit, self.view.sel()[0], res)


# --------------------------------


# TonyJsonToGoCommand ...
class TonyJsonToGoCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        res = (JSON2Go()).Parse(json.loads(text))
        self.view.replace(edit, self.view.sel()[0], res)


# TonyMd5Command ...
class TonyMd5Command(sublime_plugin.TextCommand):
    def run(self, edit):
        text = ""
        for region in self.view.sel():
            text += self.view.substr(region)
        m1 = hashlib.md5(text.encode("utf8"))
        res = m1.hexdigest()
        self.view.replace(edit, self.view.sel()[0], res)


# --------------------------------


# TonyShowOpenFilesCommand 显示已打开文件列表
class TonyShowOpenFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.views = []
        tabs = []
        self.window = sublime.active_window()
        for view in self.window.views():
            filename = view.file_name()
            if filename is None:
                continue
            self.views.append(view)
            name = os.path.basename(filename)
            tabs.append([name, filename])
        self.window.show_quick_panel(tabs, self.select)

    def select(self, index):
        if index > -1:
            self.window.focus_view(self.views[index])


# --------------------------------


# SortOpenFilesListener 监听打开文件栏自动排序
class SortOpenFilesListener(sublime_plugin.EventListener):
    def on_post_save(self, view):
        if GetSetting("tony_open_files_sort") is not True:
            return
        window = view.window()
        active_view = window.active_view()
        views = []
        for item in window.views():
            filename = item.file_name() if item.file_name() else ""
            dirname = os.path.dirname(filename)
            group, _ = window.get_view_index(item)
            views.append([item, dirname, filename, group])
        views = sorted(views, key=operator.itemgetter(1, 2))
        for index in range(len(views)):
            view = views[index]
            if window.get_view_index(view[0]) == (view[3], index):
                continue
            window.set_view_index(view[0], view[3], index)
        window.focus_view(active_view)
        return

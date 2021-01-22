# -*- coding: utf-8 -*-

import re 


class JSON2Go():
    Content = ""
    GoInterface = "interface{}"
    Indent = 0

    def __init__(self):
        self.Append("type " + __class__.__name__ + " ")
        return

    def Parse(self, obj):
        if isinstance(obj, list):
            self.ParseSlice(obj)
        elif isinstance(obj, dict):
            self.ParseStruct(obj)
        else:
            self.Append(self.GetGoType(obj))
        return self.Content

    def ParseStruct(self, data):
        self.Indent += 1
        self.Append("struct {")
        self.Append("\n" + "    " * self.Indent)
        count = 0
        for key in data:
            count += 1
            self.Append(self.ToUpper(key) + " ")
            self.Parse(data[key])
            self.Append(' `json:"' + self.ToUnderline(key) + '"`')
            self.Append("\n")
            if count != len(data):
                self.Append("    " * self.Indent)
            else:
                self.Append("    " * (self.Indent-1))
        self.Indent -= 1
        self.Append("}")
        return

    def ParseSlice(self, data):
        # 遍历列表, 如果值类型不一致, 则为 interface{}
        objType = ""
        dataLen = len(data)
        if dataLen <= 0:
            objType = self.GoInterface
        else:
            for index in range(dataLen):
                thisType = self.GetGoType(data[index])
                if not objType:
                    objType = thisType
                elif objType != thisType:
                    objType = self.GoInterface
                    break

        self.Append("[]")
        if objType == "struct":
            # 如果元素类型为 struct, 需遍历列表中的每个对象, 将所有字段合并
            tmpStruct = {}
            for index in range(len(data)):
                for key in data[index]:
                    if key not in tmpStruct.keys():
                        tmpStruct[key] = data[index][key]
                    else:
                        # 如果临时字典中已存在该字段, 判断变量类型, 不一致则为 interface{}
                        if self.GetGoType(tmpStruct[key]) != self.GetGoType(data[index][key]):
                            tmpStruct[key] = None

            self.ParseStruct(tmpStruct)
        else:
            self.Append(objType)

        return

    # 解析单个变量对应的 Go 的类型值
    def GetGoType(self, val):
        if isinstance(val, str):
            return "string"
        elif isinstance(val, bool):
            return "bool"
        elif isinstance(val, int):
            if val % 1 == 0:
                if val > -2147483648 & val < 2147483647:
                    return "int"
                else:
                    return "int64"
            else:
                return "float64"
        elif isinstance(val, dict):
            return "struct"
        elif isinstance(val, list):
            return "slice"
        else:
            return self.GoInterface

    # 拼接 go struct
    def Append(self, data):
        self.Content += data

    # 变量转下划线
    def ToUnderline(self, text):
        p = re.compile(r'([a-z]|\d)([A-Z])')
        sub = re.sub(p, r'\1_\2', text).lower()
        return sub

    # 首字母转大写, 其余不变
    def ToUpper(self, text):
        return '{}{}'.format(text[0].upper(), text[1:])

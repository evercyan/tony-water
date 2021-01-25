<div align="center">

![tony-water](https://raw.githubusercontent.com/evercyan/cantor/master/resource/a6/a6658e4ee75fbcc60fe83abc5c31edb8.png)

一个 tony 带水的 sublime-text 插件

</div>

---

## How to install?

- Sublime 插件安装, 搜索 `Tony Water`
- MacOS 手动安装

```sh
cd ~/Library/Application\ Support/Sublime\ Text\ 3/Packages/
git clone https://github.com/evercyan/tony-water
```

---

## How to use?

- 编辑区, 右键

![tony-water-menu](https://raw.githubusercontent.com/evercyan/cantor/master/resource/d6/d68c788449654a1858b1d7fcad4df43b.png)

- 配置快捷键

具体 `command` 见 `Default.sublime-commands`

---

## Something else?

将 JSON 字符串翻译成 Golang struct, e.g.

```json
{
    "firstName": "ryan",
    "info": [
        1, 2, "3"
    ],
    "detailInfo": {
        "age": 20,
        "height": "172cm"
    },
    "som":[
        {
            "aaa": 1,
            "bbb": 4
        },
        {
            "bbb": "2",
            "ccc": [
                {
                    "a": [
                        "what"
                    ],
                    "b": {
                        "name": "1"
                    },
                    "c": "c"
                }
            ]
        }
    ]
}
```

```go
type JSON2Go struct {
    Som []struct {
        Bbb interface{} `json:"bbb"`
        Ccc []struct {
            A []string `json:"a"`
            C string `json:"c"`
            B struct {
                Name string `json:"name"`
            } `json:"b"`
        } `json:"ccc"`
        Aaa int `json:"aaa"`
    } `json:"som"`
    Info []interface{} `json:"info"`
    FirstName string `json:"first_name"`
    DetailInfo struct {
        Height string `json:"height"`
        Age int `json:"age"`
    } `json:"detail_info"`
}
```

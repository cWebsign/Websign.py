from .websign import *
from flask import Flask

def CreateControl(tag: ControlTag, sclass: str | None, id: str | None, text: str | None, subcontrols: list[Control] | None) -> Control:
    c = Control()

    c.Tag = tag
    c.ID = id
    c.Text = text
    c.SubControls = subcontrols

    c.Parent = None
    c.Type = None
    c.Class = None
    c.href = None
    c.CSS = None
    c.Data = None
    c.OnClick = 0
    c.OnClickJS = ""
    c.FormID = ""
    c.DisplayID = None

    return c

app = Flask(__name__)

@app.route('/hello')
def hello():
    head_element = CreateControl(ControlTag.HEAD_TAG, None, None, None, [
        CreateControl(ControlTag.TITLE_TAG, None, None, "My Website", None)
    ])

    body_element = CreateControl(ControlTag.BODY_TAG, None, None, None, [
        CreateControl(ControlTag.P_TAG, None, None, "Hi", None)
    ])

    template = ConstructTemplate([head_element, body_element], None)
    return template

if __name__ == "__main__":
    app.run(port=1337)

"""
    [ Test Results ]

    
<html>
<head>
<title>
My Website</title>
</head>
<body>
<p>
Hi</p>
</body>
</html>

"""
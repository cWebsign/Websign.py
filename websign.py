import enum

class ControlTag(enum.Enum):
    NO_TAG                              = 8490
    HTML_TAG                            = 8491
    HEAD_TAG                            = 8492
    BODY_TAG                            = 8493
    TITLE_TAG                           = 8494
    H1_TAG                              = 8495
    H2_TAG                              = 8496
    H3_TAG                              = 8497
    INPUT_TAG                           = 8498
    P_TAG                               = 8499
    DIV_TAG                             = 8500
    A_TAG                               = 8501
    PRE_TAG                             = 8502
    BUTTON_TAG                          = 8503
    FORM_TAG                            = 8504

class CSS():
    Class: str
    Data: list[str]
    Selector: int

class WJS():
    ValueType: int
    Elements: list
    action: int
    animation_id: str
    change_id: str

class Control():
    Parent: None
    Tag: ControlTag
    ID: str
    Type: str
    Text: str
    Class: list[str]
    href: str
    CSS: list[str]
    Data: str
    OnClick: int
    OnClickJS: str
    FormID: str
    DisplayID: str
    SubControls: None

def FindTag(q: str) -> ControlTag:
    for tag in ControlTag:
        if tag.name == q:
            return tag.name

    return ControlTag.NO_TAG

def ConstructCSS(css: list):
    buffer = "<style>\n"

    for style in css:
        if style.Selector:
            buffer += "."

        buffer += {style.Class} + " {\n"

        for st in style.Data:
            buffer += f"{st}\n"

        resp += "\n}\n"

    buffer += "</style>\n"


def ConstructTemplate(controls: list[Control], styles: list[CSS]) -> str:
    template = "<html>\n"

    if controls[0].Tag == ControlTag.HEAD_TAG:
        template += ConstructParent(controls[0], 0)
        template += ConstructCSS(styles)

    i = 0
    for control in controls:
        template += ConstructParent(control, 0)
        i += 1

    template += "</html>\n\n"

def ConstructParent(control: Control, sub: int):
    resp = f"<{control.Tag.name}"

    if sub == 0:
        if control.ID:
            resp += f"id=\"{control.ID}\" "

        if control.Type:
            resp += f"type=\"{control.Type}\" "

        if control.Data:
            resp += f"{control.Data} "

        if control.Class:
            resp += f"class=\"{control.CLass}\" "

        if control.href:
            resp += f" href=\"{control.href}\" "

        if control.CSS:
            resp += f" style=\""
            for g in control.CSS: resp += g
            resp += "\" "

        if control.OnClick or control.FormID:
            pass

        resp += f"{control.Tag.name}>\n"

    if control.Text:
        resp += control.Text

    SubTag = None
    
    if control.SubControls:
        for c in control.SubControls:
            resp += f"<{c.Tag.name}"

            if c.ID:
                resp += f"id=\"{c.ID}\" "

            if c.Type:
                resp += f"type=\"{c.Type}\" "

            if c.Data:
                resp += f"{c.Data} "

            if c.Class:
                resp += f"class=\"{c.CLass}\" "

            if c.href:
                resp += f" href=\"{c.href}\" "

            if c.CSS:
                resp += f" style=\""
                for g in c.CSS: resp += g
                resp += "\" "

            if c.OnClick or c.FormID:
                pass

            resp += f"{c.Tag.name}>\n"

            if c.Text:
                resp += c.Text

            if c.SubControls:
                resp += ConstructParent(c, 1)

    resp += f"</{control.Tag.name}>"


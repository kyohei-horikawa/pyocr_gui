from PIL import Image
import pyocr
import pyocr.builders
from os.path import basename


def image_text(file, lang='eng'):
    
    tools = pyocr.get_available_tools()
    tool = tools[0]

    txt = tool.image_to_string(
        Image.open('./images/' + file),
        lang=lang,
        builder=pyocr.builders.TextBuilder()
    )

    with open('./text/' + basename(file).split('.')[0] + '.txt', mode='w') as f:
        f.write(txt)

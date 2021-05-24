from pathlib import Path
from pdf2image import convert_from_path


def pdf_image(pdf_file, fmt='png', dpi=200):

    # pdf_file、img_pathをPathにする
    pdf_path = Path(pdf_file)
    image_dir = Path('./images')

    # PDFをImage に変換(pdf2imageの関数)
    pages = convert_from_path(pdf_path, dpi)

    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        file_name = "{}_{:02d}.{}".format(pdf_path.stem, i + 1, fmt)
        image_path = image_dir / file_name
        page.save(image_path, fmt)

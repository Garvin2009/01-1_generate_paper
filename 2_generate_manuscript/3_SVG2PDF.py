# import os
# from svglib.svglib import svg2rlg
# from reportlab.graphics import renderPDF

# allFileList = os.listdir("./Table")

# for file in allFileList:
#     drawing = svg2rlg("./Table/" + file)
#     renderPDF.drawToFile(drawing, './PDF/' + file +'.pdf')


from tqdm import tqdm
from os import listdir
import multiprocessing as mp
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import os

import info


def svg2pdf(file):
    drawing = svg2rlg(f"./Merge/{file}")
    renderPDF.drawToFile(drawing, f"./PDF/{file}.pdf")


if __name__ == "__main__":
    cpus = mp.cpu_count()  # count of CPU cores
    result_path = f'PDF' # 存放資料夾
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    print(f"Using {cpus = }")
    pool = mp.Pool(cpus)
    files = listdir("./Merge")
    for _ in tqdm(pool.imap_unordered(svg2pdf, files), total=info.TOTAL_PAGES):
        ...
    pool.close()
    pool.join()

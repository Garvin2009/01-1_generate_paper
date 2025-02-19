# genpaper
### 需建立虛擬環境，前往https://www.anaconda.com/download下載
### 安裝完成後輸入指令
```
conda create --name gen_paper python=3.8
```
### 切換資料夾至0_env_gen_paper
```
cd 0_env_gen_paper
```
### 安裝 requirements.txt 套件
```
pip install –r requirements.txt
```

### 切換資料夾至1_generate_CP950
```
cd ..
cd 1_generate_CP950
```

### 去除稿紙內重複的文字
```
python m1_compare_duplicate.py
```
### 產生CP950.json
```
python m2_generate_CP950.py
```
### 切換資料夾至2_generate_manuscript
```
cd ..
cd 2_generate_manuscript
```
### 製作包含 CP950 所有字元稿紙

![GITHUB](https://github.com/Circle472/script_ntut/raw/main/scripts_pku_file.jpg)

### 修改 info.py 程式碼
```python
TOTAL_PAGES = 57
# personal information below
ID = "STUDENT_ID"  # enter your ID here
NAME = "NAME_HERE"  # enter your name here
NUMBER = 0  # enter your number here
```

### 執行程式碼
#### 步驟一：生成 57 張 svg 稿紙
```
python 1_SVGtable.py
```
#### 步驟二：將 57 張 svg 檔案加上 QRcode
```
python 2_QR_add.py
```
#### 步驟三：將 57 張 svg 轉成 57 個 pdf 檔案
```
python 3_SVG2PDF.py
```
#### 步驟四：將 57 張 pdf 檔案合併成一個 pdf 檔案
```
python 4_PDFmerge.py
```
![GITHUB](https://github.com/Circle472/script_ntut/raw/main/scripts_pku_intro.jpg)

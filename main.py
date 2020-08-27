import requests
from datetime import datetime
import json
from PIL import Image, ImageDraw, ImageFont

date = ['월', '화', '수', '목', '금', '토', '일']
today = datetime.today().strftime("%Y%m%d")
KEY = ''
SC_CODE = ''
SCHUL_CODE = ''

r = requests.get('https://open.neis.go.kr/hub/mealServiceDietInfo?' + 'KEY=' + KEY + '&Type=json' + '&pIndex=1' + '&pSize=100' + '&ATPT_OFCDC_SC_CODE=' + SC_CODE + '&SD_SCHUL_CODE=' + SCHUL_CODE + '&MLSV_YMD=' + today)

gslist = json.loads(r.content.decode('utf8'))

gsstr = ''
if 'INFO-200' not in r.text:
    for i in gslist['mealServiceDietInfo'][1]['row']:
        if i['MMEAL_SC_NM'] == '조식':
            pass
        else:
            gsstr += i['MMEAL_SC_NM']
            gsstr += '\n\n'
            gsstr += str(i['DDISH_NM']).replace('<br/>', '\n')
            gsstr += '\n'
            gsstr += '\n'
else:
    gsstr = '오늘은 급식이 없습니다.'

font = 'font.ttf'

target_image = Image.new("RGB", (900, 1100), "#cceabb")
selectedFont = ImageFont.truetype(font, 50)
draw = ImageDraw.Draw(target_image)
draw.text((150, 100), gsstr, fill='#3f3f44', font=selectedFont)
target_image.save('./' + datetime.today().strftime("%Y년 %m월 %d일".encode('unicode-escape').decode()).encode().decode('unicode-escape') + ' ' + date[int(datetime.today().strftime("%w"))] + '.png')

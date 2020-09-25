from fastapi import FastAPI, APIRouter, Response
from starlette.responses import StreamingResponse
from lib.engine import cur_engine as s
from captcha.image import ImageCaptcha

import io
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random
capcha_router = APIRouter()



def out_refrash():
  str_key=s.param('str_key') or ''
  
  cnt=s.db.getvalue(
    select_fields='count(*)',
    table='capture',
    where='str_key=%s',
    values=[str_key],
    debug=1
  )
  
  if not cnt:
    return Response('Попытка подмены?',media_type='text/plain')


def out_key_or_refrash():
  str=''
  str_res=''


# Вывод капчи
@capcha_router.get('/capcha')
def out_capcha():
  action=s.param('action')
  print('action:',action)

  if action == 'refrash':
    result=out_refrash()
    if result: return result
  
  if (action == 'out_key') or (action == 'refrash'):
    out_key_or_refrash()

  image=ImageCaptcha(fonts=[],width=120,height=30, font_sizes=[25] ) # fonts=['/path/A.ttf', '/path/B.ttf']
  data=image.generate('12+15=') #.getvalue()
  return StreamingResponse(data, media_type="image/png")


def roll(image, delta):
    "Roll an image sideways"

    xsize, ysize = image.size

    delta = delta % xsize
    if delta == 0: return image

    part1 = image.crop((0, 0, delta, ysize))
    part2 = image.crop((delta, 0, xsize, ysize))
    image.paste(part2, (0, 0, xsize-delta, ysize))
    image.paste(part1, (xsize-delta, 0, xsize, ysize))

    return image

@capcha_router.get('/im-capcha')
def im_capcha():

  # по умолчанию
  capcha_settings={
    'noise_level':800,
    'width':100,
    'height':40,
    'bg_color':(255,255,255,255),
    'font_color':'#be0000',
    'font_size':20,
    'text_position':(10, 10)
    #'rotate':(-10,10)
  }

  if ('capcha_settings' in s.vars) and s.vars['capcha_settings']:
    for k in s.vars['capcha_settings']:
      #print('k/v',k)
      capcha_settings[k]=s.vars['capcha_settings'][k]

  image = Image.new('RGBA', (capcha_settings['width'], capcha_settings['height']),capcha_settings['bg_color'])
  draw = ImageDraw.Draw(image)
  font = ImageFont.truetype("./lib/capcha.ttf", capcha_settings['font_size'])
  #draw. ellipse((10,10,30,30), fill="red", outline="green")
  draw.text(capcha_settings['text_position'],"12 + 15",fill=capcha_settings['font_color'], font=font) # 
  #draw = draw.rotate(10, expand = 1) 

  # шум
  for numpix in range(0, capcha_settings['noise_level']):
      x=random.randint(0,int(image.size[0]-1))
      y=random.randint(0,int(image.size[1]-1))
      r=random.randint(0,255)
      g=random.randint(0,255)
      b=random.randint(0,255)
      image.putpixel((x,y),(r,g,b))
  #image = image.rotate(random.randint(-10,10)) 
  #image=roll(image,5)
  # выводим:
  imgByteArr = io.BytesIO()
  image.save(imgByteArr, format='PNG')
  imgByteArr = imgByteArr.getvalue()
  return StreamingResponse( io.BytesIO(imgByteArr), media_type="image/png")
  
import pyautogui as pag
import time

sWidth, sHeight = pag.size()
print((sWidth, sHeight))

def click_pingjiao():
    c = pag.locateOnScreen('pictures/pingjiao.png', confidence=0.95,
                           region=(int(sWidth/2), 0, sWidth, sHeight))
    pag.moveTo(c, duration=0.2)
    # pag.moveRel(150,0,duration=0.2)
    pag.click()
    time.sleep(1)

def click_nextpage():
    c = pag.locateOnScreen('pictures/nextpage.png', confidence=0.90,region=(int(sWidth/2), 0, sWidth, sHeight))
    pag.moveTo(c, duration=0.2)
    pag.moveRel(17, 0, duration=0.2)
    pag.click(c)
    # wait for downloading
    time.sleep(1)

def click_submit():
    c = pag.locateOnScreen('pictures/submit.png', confidence=0.8,
                        region=(1500, 900, sWidth, sHeight))
    pag.click(c)
    time.sleep(1)

def click_OK():
    # OK
    c = pag.locateOnScreen('pictures/OK.png', confidence=0.8)
    pag.click(c)
    time.sleep(1)

m_times = 6
for i in range(m_times):
    time.sleep(2)

    click_nextpage()
    click_nextpage()

    click_pingjiao()

    i = 0
    while i < 10:
        time.sleep(0.1)
        # pic='pictures/{num}.png'
        # pic=pic.format(num=i)
        pic = 'pictures/common.png'
        print(pic)
        c = pag.locateOnScreen(pic, confidence=0.85, region=(0, 0, 1000, 1000))
        pag.moveTo(c, duration=0.1)
        pag.moveRel(-45, 0, duration=0.1)
        pag.click()
        # 滚动距离很关键，需要调整大小，正好点完一个滑倒下一个的位置
        pag.scroll(-75)
        i += 1

    # 提交
    click_submit()
    # OK
    click_OK();

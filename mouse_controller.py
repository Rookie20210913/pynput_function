from pynput.mouse import Button,Controller
import time

mouse=Controller()

#輸出座標
pos=mouse.position
print(pos)

#相對移動
# removE=mouse.move(100,100)

#組合成一次點擊左鍵
mouse.press(Button.left)
mouse.release(Button.left)

#控制點擊次數
mouse.click(Button.left,1)

import pyautogui

def find_img(img, message):
    try:
        # Top right region of the screen on my large monitor
        return pyautogui.locateCenterOnScreen(img, confidence=0.8, region=(3000,0,438,660))
    except:
        print(message)
        return None

def click_btn(btn):
    pyautogui.moveTo(btn)
    pyautogui.click()


defense_btn = find_img("./assets/images/btn_defense_tab.png", "No Defense Tab, Has the game started?")

if defense_btn:
    print(defense_btn)
    click_btn(defense_btn)
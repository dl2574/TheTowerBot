# Build a Bot to farm Coins in The Tower game.
import pyautogui

def main():
    pyautogui.sleep(3)
    battle_btn = pyautogui.locateCenterOnScreen("./assets/images/btn_Battle.png")
    if battle_btn != None:
        pyautogui.moveTo(battle_btn)
        pyautogui.click()



if __name__ == "__main__":
    main()
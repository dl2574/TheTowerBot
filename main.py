# Build a Bot to farm Coins in The Tower game.
import pyautogui


def main():
    pyautogui.sleep(3)
    battle_btn = None
    base_reset_time = 30


    try:
        battle_btn = pyautogui.locateCenterOnScreen("./assets/images/btn_Battle.png", confidence=0.8)
    except:
        print("Battle Button not found...")

    if battle_btn != None:
        pyautogui.moveTo(battle_btn)
        pyautogui.click()


    while True:
        gem_btn = None
        float_btn = None
        retry_btn = None

        try:
            gem_btn = pyautogui.locateCenterOnScreen("./assets/images/btn_5_gem.png", confidence=0.8)
        except:
            print("No Gems.")

        try:
            float_btn = pyautogui.locateCenterOnScreen("./assets/images/btn_float_gem.png", confidence=0.8)
        except:
            print("No Gems.")

        try:
            retry_btn = pyautogui.locateCenterOnScreen("./assets/images/btn_Retry.png", confidence=0.8)  
        except:
            print("Retry Button not found. Sleeping...")

        if gem_btn != None:
            pyautogui.moveTo(gem_btn)
            pyautogui.click()

        if float_btn != None:
            pyautogui.moveTo(float_btn)
            pyautogui.click()
    
        if retry_btn != None:
            pyautogui.moveTo(retry_btn)
            pyautogui.click()
  

            print("Game Restarting!")

        pyautogui.sleep(base_reset_time)



if __name__ == "__main__":
    main()
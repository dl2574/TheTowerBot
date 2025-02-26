# Build a Bot to farm Coins in The Tower game.
import pyautogui


def main():
    pyautogui.sleep(3)
    base_reset_time = 30

    battle_btn = find_btn("./assets/images/btn_Battle.png", "Battle Button not found...")

    if battle_btn != None:
        click_btn(battle_btn)


    while True:
        gem_btn = find_btn("./assets/images/btn_5_gem.png", "No Gems.")
        float_btn = find_btn("./assets/images/btn_float_gem.png", "No Gems.")
        retry_btn = find_btn("./assets/images/btn_Retry.png", "Retry Button not found. Sleeping...")

        if gem_btn != None:
            click_btn(gem_btn)

        if float_btn != None:
            click_btn(float_btn)
            
        if retry_btn != None:
            click_btn(retry_btn)
            print("Game Restarting!")

        pyautogui.sleep(base_reset_time)

def find_btn(img, message):
    try:
        return pyautogui.locateCenterOnScreen(img, confidence=0.8)
    except:
        print(message)
        return None

def click_btn(btn):
    pyautogui.moveTo(btn)
    pyautogui.click()


if __name__ == "__main__":
    main()
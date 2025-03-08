# Build a Bot to farm Coins in The Tower game.
import pyautogui


def main():
    pyautogui.sleep(3)
    base_reset_time = 30

    battle_btn = find_img("./assets/images/btn_Battle.png", "Battle Button not found...")
    defense_btn = find_img("./assets/images/btn_defense_tab.png", "No Defense Tab, Has the game started?")

    if battle_btn != None:
        click_btn(battle_btn)



    while True:
        gem_btn = find_img("./assets/images/btn_5_gem.png", "No Gems.")
        float_btn = find_img("./assets/images/btn_float_gem.png", "No Gems.")
        retry_btn = find_img("./assets/images/btn_Retry.png", "Retry Button not found. Sleeping...")
        

        if gem_btn != None:
            click_btn(gem_btn)

        if float_btn != None:
            click_btn(float_btn)
            
        if retry_btn != None:
            click_btn(retry_btn)
            print("Game Restarting!")

        if defense_btn != None:
            defense_lbl = find_img("./assets/images/label_defense_upgrades.png", "Switching to the defense tab...")
            if defense_lbl == None:
                click_btn(defense_btn)
                pyautogui.move(0, -160)
            else:
                pyautogui.moveTo(3180, 470)
            pyautogui.scroll(100)
            pyautogui.click()         

        pyautogui.sleep(base_reset_time)

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


if __name__ == "__main__":
    main()
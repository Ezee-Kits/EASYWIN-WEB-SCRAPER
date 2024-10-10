from func import scrolling,saving_files,drop_duplicate,headless_selenium_init,saving_path_csv
from bs4 import BeautifulSoup
import time




def easywin_func():
    path = f'{saving_path_csv}/EASYWIN.csv'
    driver,wait,EC,By = headless_selenium_init()
    driver.get('https://easywin.ng/')
    time.sleep(15)
    driver.get('https://easywin.ng/')

    for x in range(1,10):
        upcoming = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#matchs > div.main_bottom > div.newSportLive.clearfix > div:nth-child(2) > a")))
        print(upcoming.text)
        if upcoming.text =='Upcoming':
            wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[6]/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[2]")))
            upcoming.click()
            break
        else:
            pass

    
    time.sleep(5)

    scrolling(driver=driver)

    matches = wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="sportList"]/div/div[2]')))
    matches = matches.text.replace('\n','!').split('!')
    print(matches)

    new_matches = []
    for x in matches:
        x = x.strip()
        if '+' in x or '•' in x:
            pass
        else:
            new_matches.append(x)

    time_value = []
    time_index = []
    for i,x in enumerate(new_matches):
        if ':' in x:
            indx = new_matches.index(x,i,len(new_matches))
            time_index.append(indx)
            time_value.append(x)

    # print(new_matches)
    # print(time_index)
    # print(time_value)

    for x in time_index:
        try:
            f_elem_indx = time_index.index(x)
            s_elem_indx = time_index.index(x) + 1

            if (time_index[s_elem_indx] - time_index[f_elem_indx]) == 6:
                all_info = new_matches[ time_index[f_elem_indx]:time_index[s_elem_indx] ]
                match_time = all_info[0]

                home_team = all_info[1]
                away_team = all_info[2]

                home_odd = float(all_info[3])
                draw_odd = float(all_info[4])
                away_odd = float(all_info[5])
                bookmaker = 'EASYWIN'

                data = {
                    'TIME':match_time,
                    'HOME TEAM':home_team,
                    'AWAY TEAM':away_team,

                    'HOME ODD': home_odd,
                    'DRAW ODD':draw_odd,
                    'AWAY ODD':away_odd,
                    'BOOKMAKER':bookmaker
                }
                saving_files(data=[data],path=path)
        except:
            pass

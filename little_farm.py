import pyautogui
import numpy as np
import cv2
import time
from datetime import datetime


# time.sleep(3)

def pokazuj(opis, ekran):
    cv2.imshow(opis, ekran)
    cv2.waitKey()
    cv2.destroyAllWindows()


# plik = 'marchew_do_zbioru.png'
caly_img = ''


def pobierz_screen():
    global caly_img
    myScreenshot = pyautogui.screenshot()
    # myScreenshot.save(r'Path to save screenshot\file name.png')
    myScreenshot.save(r'screen.png')

    caly_img = cv2.imread('screen.png', cv2.IMREAD_UNCHANGED)


pobierz_screen()

pokazuj('Pulpit', caly_img)


def wylogowany():
    wycinek_img = cv2.imread('wylogowany.png', cv2.IMREAD_UNCHANGED)
    w = wycinek_img.shape[1]
    h = wycinek_img.shape[0]
    result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)

    threshold = .90
    yloc, xloc = np.where(result >= threshold)
    miejsca = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        miejsca.append([int(x), int(y), int(w), int(h)])
        miejsca.append([int(x), int(y), int(w), int(h)])
    miejsca, weights = cv2.groupRectangles(miejsca, 1, 0.2)
    if len(miejsca) > 0:
        return True
    else:
        return False


def ruch(grafika, zwrot=False, opis=False):
    wycinek_img = cv2.imread(grafika, cv2.IMREAD_UNCHANGED)
    w = wycinek_img.shape[1]
    h = wycinek_img.shape[0]

    result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)

    threshold = .90
    yloc, xloc = np.where(result >= threshold)

    #   Wiele wyników
    miejsca = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        miejsca.append([int(x), int(y), int(w), int(h)])
        miejsca.append([int(x), int(y), int(w), int(h)])

    miejsca, weights = cv2.groupRectangles(miejsca, 1, 0.2)
    if opis:
        print(grafika.split('.')[0].replace('_', ' '), 'znaleziono:', len(miejsca))
    miejsca_centrum = []
    for tab in miejsca:
        x = tab[0]
        y = tab[1]
        # print(x, y, grafika)
        pyautogui.moveTo(x + w / 2, y + h / 2)
        miejsca_centrum.append([x + w / 4, y + h / 4])
        pyautogui.click()

        if grafika.split('.')[0] not in (
                'marchew', 'zboze', 'ogorki', 'truskawki', 'kukurydza', 'zasiej', 'podlej', 'zbierz'):
            if (x + w / 4, y + h / 4, grafika.split('_')[0]) in pola_total:
                pass
            else:
                pola_total.append((x + w / 4, y + h / 4, grafika.split('_')[0]))

        time.sleep(1)
    if len(miejsca_centrum) > 0 and zwrot:
        return miejsca_centrum
    return []


def ruch2(namiary, opis=False):
    pyautogui.moveTo(namiary[0], namiary[1])
    pyautogui.click()
    if opis:
        print('click:', namiary[0], namiary[1])
    time.sleep(1)


def wylogowanie():
    while True:
        tmp = ruch('wylogowanie1.png', True, True)
        time.sleep(1)
        pobierz_screen()
        if len(tmp) > 0:
            break
    while True:
        tmp = ruch('wylogowanie2.png', True, True)
        time.sleep(1)
        pobierz_screen()
        if len(tmp) > 0:
            break
    while True:
        tmp = ruch('wylogowanie3.png', True, True)
        time.sleep(1)
        pobierz_screen()
        if len(tmp) > 0:
            break
    while True:
        tmp = ruch('wylogowanie4.png', True, True)
        time.sleep(1)
        pobierz_screen()
        if len(tmp) > 0:
            break
    print('Witamy z powrotem')


def ile_obiektow_na_stronie(obiekt):
    """
    zliczanie ile jest obiektów na stronie
    :param obiekt: nazwa zdjęcia
    :return: ilość znalezionych obiektów
    """
    wycinek_img = cv2.imread(obiekt, cv2.IMREAD_UNCHANGED)
    w = wycinek_img.shape[1]
    h = wycinek_img.shape[0]

    result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)

    threshold = .90
    yloc, xloc = np.where(result >= threshold)

    #   Wiele wyników
    miejsca = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        miejsca.append([int(x), int(y), int(w), int(h)])
        miejsca.append([int(x), int(y), int(w), int(h)])

    miejsca, weights = cv2.groupRectangles(miejsca, 1, 0.2)
    return len(miejsca)


def obiekty_na_stronie(obiekt):
    """
    zliczanie ile jest obiektów na stronie
    :param obiekt: nazwa zdjęcia
    :return: ilość znalezionych obiektów
    """
    wycinek_img = cv2.imread(obiekt, cv2.IMREAD_UNCHANGED)
    w = wycinek_img.shape[1]
    h = wycinek_img.shape[0]

    result = cv2.matchTemplate(caly_img, wycinek_img, cv2.TM_CCOEFF_NORMED)

    threshold = .90
    yloc, xloc = np.where(result >= threshold)

    #   Wiele wyników
    miejsca = []
    for (x, y) in zip(xloc, yloc):
        cv2.rectangle(caly_img, (x, y), (x + w, y + h), (0, 255, 255), 2)
        miejsca.append([int(x), int(y), int(w), int(h)])
        miejsca.append([int(x), int(y), int(w), int(h)])

    miejsca, weights = cv2.groupRectangles(miejsca, 1, 0.2)
    return miejsca


def zmien_pole():
    pass


# pokazuj("Cały z prostokątem", caly_img)

# pliki = ('grass.png', 'grass2.png', 'grass3.png')
pliki_podlewanie = (
    'marchew_do_podlania.png', 'marchew_do_podlania2.png', 'zboze_do_podlania.png',
    'zboze_do_podlania2.png', 'ogorki_do_podlewania.png', 'truskawki_do_podlania.png', 'kukurydza_do_podlewania.png')
pliki_zbiory = ('marchew_do_zbioru.png', 'zboze_do_zbioru.png', 'ogorki_do_zbioru.png', 'truskawki_do_zbioru.png',
                'kukurydza_do_zbioru.png')

warzywa = ('marchew', 'zboze', 'ogorki', 'truskawki', 'kukurydza', 'rzodkiewka')

namiary = {element: () for element in warzywa}

pola_total = []

namiary_marchewki = []
namiary_zboze = []
namiary_ogorki = []

licz = 0
liczba_petli = 0
while True:
    try:
        liczba_petli += 1
        print(f'{datetime.now().strftime("%Y-%m-%d,%H:%M:%S")},{liczba_petli}')
        if wylogowany():
            print('Zostałeś wylogowany!')
            wylogowanie()
            # break
        ruch('woda_yes.png')
        #   podlewanie
        for warzywo in warzywa:
            plik = warzywo + '_do_podlania.png'
            ruch('podlej.png')
            ruch(plik)
            time.sleep(1)
            #   Dodać przezunięcie względem punktu 0,0
            # plik = warzywo + '_do_podlania.png'
            # lista = obiekty_na_stronie(plik)
            # if len(lista) > 0:
            #     for namiar in lista:
            #         ruch('podlej.png')
            #         ruch2((namiar[0], namiar[1]))
            # time.sleep(1)
        #   zbiory
        for warzywo in warzywa:
            plik = warzywo + '_do_zbioru.png'
            ruch('zbierz.png')
            namiary[warzywo] = ruch(plik, zwrot=True)

            time.sleep(1)
        ruch('woda_yes.png')
        #  sianie
        for warzywo in warzywa:
            if len(namiary[warzywo]):
                print(f'Do zasiania {warzywo}:', len(namiary[warzywo]))
                ruch('zasiej.png')
                # ruch('marchewka.png')
                ruch(warzywo + '.png')
                # for namiar in namiary_marchewki:
                for namiar in namiary[warzywo]:
                    ruch2(namiar)

                namiary[warzywo] = []

        pobierz_screen()
        print('Ilość pól:', len(pola_total))
        time.sleep(3)
        licz += 1
    except Exception as e:
        if input('Czy kontynuować (t/n)? ').strip() == 't':
            continue
        else:
            break
   

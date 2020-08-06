import time
import sqlite3
import os.path
import json
from datetime import date
import datetime
import random


class Search:  # первый аргумент - запрос юзера, второй - флаг games или news.
    global spis_genre, slovar, mat
    spis_genre = ['strategy', 'simylate', 'mmo', 'shooter', 'horror', 'adventure']
    slovar = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'e',
              'ж': 'zh', 'з': 'z', 'и': 'i', 'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
              'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h',
              'ц': 'c', 'ч': 'cz', 'ш': 'sh', 'щ': 'scz', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e',
              'ю': 'u', 'я': 'ja', 'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E',
              'Ж': 'ZH', 'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N',
              'О': 'O', 'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'H',
              'Ц': 'C', 'Ч': 'CZ', 'Ш': 'SH', 'Щ': 'SCH', 'Ъ': '', 'Ы': 'y', 'Ь': '', 'Э': 'E',
              'Ю': 'U', 'Я': 'YA', ',': '', '?': '', ' ': '_', '~': '', '!': '', '@': '', '#': '',
              '$': '', '%': '', '^': '', '&': '', '*': '', '(': '', ')': '', '-': '', '=': '', '+': '',
              ':': '', ';': '', '<': '', '>': '', '\'': '', '"': '', '\\': '', '/': '', '№': '',
              '[': '', ']': '', '{': '', '}': '', 'ґ': '', 'ї': '', 'є': '', 'Ґ': 'g', 'Ї': 'i',
              'Є': 'e', '—': ''}
    mat = ['6ля', '6лядь', '6лять', 'b3ъeб', 'cock', 'cunt', 'hui', 'хуи', 'e6aль', 'ebal', 'eblan', 'eбaл',
           'eбaть', 'eбyч', 'eбать', 'eбёт', 'eблантий', 'fuck', 'fucker', 'fucking', 'xyёв', 'xyй', 'xyя', 'xуе,xуй',
           'xую', 'zaeb', 'zaebal', 'zaebali', 'zaebat', 'архипиздрит', 'ахуел', 'ахуеть', 'бздение', 'бздеть',
           'бздех', 'бздецы', 'бздит', 'бздицы', 'бздло', 'бзднуть', 'бздун', 'бздунья', 'бздюха', 'бздюшка',
           'бздюшко', 'бля', 'блябу', 'блябуду', 'бляд', 'бляди', 'блядина', 'блядище', 'блядки', 'блядовать',
           'блядство', 'блядун', 'блядуны', 'блядунья', 'блядь', 'блядюга', 'блять', 'вафел', 'вафлёр', 'взъебка',
           'взьебка', 'взьебывать',
           'въеб', 'въебался', 'въебенн', 'въебусь', 'въебывать', 'выблядок', 'выблядыш', 'выеб', 'выебать',
           'выебен',
           'выебнулся', 'выебон', 'выебываться', 'вьебен', 'гандон', 'гондон', 'доебываться', 'долбоеб',
           'долбоёб',
           'долбоящер', 'дрисня', 'дрист', 'дристануть', 'дристать', 'дристун', 'дристуха', 'дрочелло',
           'дрочена',
           'дрочила', 'дрочилка', 'дрочистый', 'дрочить', 'дрочка', 'дрочун', 'е6ал', 'е6ут', 'еб твою мать',
           'ёб твою мать', 'ёбaн', 'ебaть', 'ебyч', 'ебал', 'ебало', 'ебальник', 'ебан', 'ебанамать',
           'ебанат',
           'ебаная', 'ёбаная', 'ебанический', 'ебанный', 'ебанныйврот', 'ебаное', 'ебануть', 'ебануться',
           'ёбаную',
           'ебаный', 'ебанько', 'ебарь', 'ебат', 'ёбат', 'ебатория', 'ебать', 'ебать-копать', 'ебаться',
           'ебашить',
           'ебёна', 'ебет', 'ебёт', 'ебец', 'ебик', 'ебин', 'ебись', 'ебическая', 'ебки', 'ебла', 'еблан',
           'ебливый',
           'еблище', 'ебло', 'еблыст', 'ебля', 'ёбн', 'ебнуть', 'ебнуться', 'ебня', 'ебошить', 'ебская',
           'ебский',
           'ебтвоюмать', 'ебун', 'ебут', 'ебуч', 'ебуче', 'ебучее', 'ебучий', 'ебучим', 'ебущ', 'ебырь',
           'елда',
           'елдак', 'елдачить', 'жопа', 'жопу', 'заговнять', 'задрачивать', 'задристать', 'задрота', 'зае6',
           'заё6',
           'заеб', 'заёб', 'заеба', 'заебал', 'заебанец', 'заебастая', 'заебастый', 'заебать', 'заебаться',
           'заебашить',
           'заебистое', 'заёбистое', 'заебистые', 'заёбистые', 'заебистый', 'заёбистый', 'заебись',
           'заебошить',
           'заебываться', 'залуп', 'залупа', 'залупаться', 'залупить', 'залупиться', 'замудохаться',
           'запиздячить',
           'засерать', 'засерун', 'засеря', 'засирать', 'засрун', 'захуячить', 'заябестая', 'злоеб',
           'злоебучая',
           'злоебучее', 'злоебучий', 'ибанамат', 'ибонех', 'изговнять', 'изговняться', 'изъебнуться', 'ипать',
           'ипаться', 'ипаццо', 'Какдвапальцаобоссать', 'конча', 'курва', 'курвятник', 'лох', 'лошарa',
           'лошара',
           'лошары', 'лошок', 'лярва', 'малафья', 'манда', 'мандавошек', 'мандавошка', 'мандавошки', 'мандей',
           'мандень', 'мандеть', 'мандища', 'мандой', 'манду', 'мандюк', 'минет', 'минетчик', 'минетчица',
           'млять',
           'мокрощелка', 'мокрощёлка', 'мразь', 'мудak', 'мудaк', 'мудаг', 'мудак', 'муде', 'мудель',
           'мудеть',
           'муди', 'мудил', 'мудила', 'мудистый', 'мудня', 'мудоеб', 'мудозвон', 'мудоклюй', 'на хер',
           'на хуй',
           'набздел', 'набздеть', 'наговнять', 'надристать', 'надрочить', 'наебать', 'наебет', 'наебнуть',
           'наебнуться', 'наебывать', 'напиздел', 'напиздели', 'напиздело', 'напиздили', 'насрать',
           'настопиздить',
           'нахер', 'нахрен', 'нахуй', 'нахуйник', 'не ебет', 'не ебёт', 'невротебучий', 'невъебенно',
           'нехира',
           'нехрен', 'Нехуй', 'нехуйственно', 'ниибацо', 'ниипацца', 'ниипаццо', 'ниипет', 'никуя', 'нихера',
           'нихуя', 'обдристаться', 'обосранец', 'обосрать', 'обосцать', 'обосцаться', 'обсирать', 'объебос',
           'обьебать обьебос', 'однохуйственно', 'опездал', 'опизде', 'опизденивающе', 'остоебенить',
           'остопиздеть',
           'отмудохать', 'отпиздить', 'отпиздячить', 'отпороть', 'отъебись', 'охуевательский', 'охуевать',
           'охуевающий',
           'охуел', 'охуенно', 'охуеньчик', 'охуеть', 'охуительно', 'охуительный', 'охуяньчик', 'охуячивать',
           'охуячить', 'очкун', 'падла', 'падонки', 'падонок', 'паскуда', 'педерас', 'педик', 'педрик',
           'педрила',
           'педрилло', 'педрило', 'педрилы', 'пездень', 'пездит', 'пездишь', 'пездо', 'пездят', 'пердануть',
           'пердеж',
           'пердение', 'пердеть', 'пердильник', 'перднуть', 'пёрднуть', 'пердун', 'пердунец', 'пердунина',
           'пердунья',
           'пердуха', 'пердь', 'переёбок', 'пернуть', 'пёрнуть', 'пи3д', 'пи3де', 'пи3ду', 'пиzдец', 'пидар',
           'пидарaс',
           'пидарас', 'пидарасы', 'пидары', 'пидор', 'пидорасы', 'пидорка', 'пидорок', 'пидоры', 'пидрас',
           'пизда',
           'пиздануть', 'пиздануться', 'пиздарваньчик', 'пиздато', 'пиздатое', 'пиздатый', 'пизденка',
           'пизденыш',
           'пиздёныш', 'пиздеть', 'пиздец', 'пиздит', 'пиздить', 'пиздиться', 'пиздишь', 'пиздища', 'пиздище',
           'пиздобол', 'пиздоболы', 'пиздобратия', 'пиздоватая', 'пиздоватый', 'пиздолиз', 'пиздонутые',
           'пиздорванец',
           'пиздорванка', 'пиздострадатель', 'пизду', 'пиздуй', 'пиздун', 'пиздунья', 'пизды', 'пиздюга',
           'пиздюк',
           'пиздюлина', 'пиздюля', 'пиздят', 'пиздячить', 'писбшки', 'писька', 'писькострадатель', 'писюн',
           'писюшка',
           'по хуй', 'по хую', 'подговнять', 'подонки', 'подонок', 'подъебнуть', 'подъебнуться', 'поебать',
           'поебень',
           'поёбываает', 'поскуда', 'посрать', 'потаскуха', 'потаскушка', 'похер', 'похерил', 'похерила',
           'похерили',
           'похеру', 'похрен', 'похрену', 'похуй', 'похуист', 'похуистка', 'похую', 'придурок', 'приебаться',
           'припиздень', 'припизднутый', 'припиздюлина', 'пробзделся', 'проблядь', 'проеб', 'проебанка',
           'проебать',
           'промандеть', 'промудеть', 'пропизделся', 'пропиздеть', 'пропиздячить', 'раздолбай', 'разхуячить',
           'разъеб',
           'разъеба', 'разъебай', 'разъебать', 'распиздай', 'распиздеться', 'распиздяй', 'распиздяйство',
           'распроеть',
           'сволота', 'сволочь', 'сговнять', 'секель', 'серун', 'серька', 'сестроеб', 'сикель', 'сила',
           'сирать',
           'сирывать', 'соси', 'спиздел', 'спиздеть', 'спиздил', 'спиздила', 'спиздили', 'спиздит',
           'спиздить',
           'срака',
           'сраку', 'сраный', 'сранье', 'срать', 'срун', 'ссака', 'ссышь', 'стерва', 'страхопиздище', 'сука',
           'суки',
           'суходрочка', 'сучара', 'сучий', 'сучка', 'сучко', 'сучонок', 'сучье', 'сцание', 'сцать', 'сцука',
           'сцуки',
           'сцуконах', 'сцуль', 'сцыха', 'сцышь', 'съебаться', 'сыкун', 'трахае6', 'трахаеб', 'трахаёб',
           'трахатель',
           'ублюдок', 'уебать', 'уёбища', 'уебище', 'уёбище', 'уебищное', 'уёбищное', 'уебк', 'уебки',
           'уёбки',
           'уебок',
           'уёбок', 'урюк', 'усраться', 'ушлепок', 'х_у_я_р_а', 'хyё', 'хyй', 'хyйня', 'хамло', 'хер',
           'херня',
           'херовато', 'херовина', 'херовый', 'хитровыебанный', 'хитрожопый', 'хуeм', 'хуе', 'хуё', 'хуевато',
           'хуёвенький', 'хуевина', 'хуево', 'хуевый', 'хуёвый', 'хуек', 'хуёк', 'хуел', 'хуем', 'хуенч',
           'хуеныш',
           'хуенький', 'хуеплет', 'хуеплёт', 'хуепромышленник', 'хуерик', 'хуерыло', 'хуесос', 'хуесоска',
           'хуета',
           'хуетень', 'хуею', 'хуи', 'хуй', 'хуйком', 'хуйло', 'хуйня', 'хуйрик', 'хуище', 'хуля', 'хую',
           'хуюл',
           'хуя',
           'хуяк', 'хуякать', 'хуякнуть', 'хуяра', 'хуясе', 'хуячить', 'целка', 'чмо', 'чмошник', 'чмырь',
           'шалава',
           'шалавой', 'шараёбиться', 'шлюха', 'шлюхой', 'шлюшка', 'ябывает']

    def comments(self, text):  # фильтр мата принимает на вход строку, возвращает ее же запиканную
        matt = ''
        global_len = 0
        polf = []
        for k in range(len(text)):
            polf.append(text[k])
        for lelemn in polf:
            if lelemn == '.':
                if polf[polf.index(lelemn) + 1] == ' ':
                    polf[polf.index(lelemn)] = ' . '
                else:
                    polf[polf.index(lelemn)] = ' .'
            elif lelemn == ',':
                if polf[polf.index(lelemn) + 1] == ' ':
                    polf[polf.index(lelemn)] = ' , '
                else:
                    polf[polf.index(lelemn)] = ' ,'
        polf = ''.join(polf)
        polf = polf.split(' ')
        for elem in polf:
            for j in range(len(elem)):
                matt += '*'
            if elem.lower() in mat:
                polf[polf.index(elem)] = matt
            matt = ''
        end = ' '.join(polf)
        return end
'''
    def search(self, reqst, games_or_news,
               id_user):  # фильтр по поиску, принимает сам запрос в поиск, флаг игры или новости, айди юзера
        end_spis = []  # словарь с рейтингом названий
        right_letters = 0
        games = []
        idd = 1
        genre = []
        tochno_end = []
        cursor, conn = db()
        if games_or_news == 'games':
            cursor.execute("SELECT COUNT(*) as count FROM games_game")
            counter = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT title FROM games_game")
        if games_or_news == 'news':
            cursor.execute("SELECT COUNT(*) as count FROM games_posts")
            counter = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT title FROM games_posts")
        for k in range(counter):
            #print(str(cursor.fetchone())[2:-3])
            games.append(str(cursor.fetchone())[2:-3])
        for elem in games:
            elem.lower()
            for el in range(len(elem)):
                if el < len(reqst):
                    if reqst[el] == elem[el]:
                        right_letters += 1
            if right_letters != 0:
                end_spis.append([elem, right_letters, idd])
            idd += 1
            right_letters = 0
        #print(end_spis)
        if games_or_news == 'games':
            for lelem in end_spis:
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (lelem[0],))
                if type(raiting(float(str(cursor.fetchone())[1:-2]))) is not str:
                    new_rait = int(raiting(float(str(cursor.fetchone())[1:-2])))
                if id_user != 0:
                    for word in spis_genre:
                        cursor.execute("SELECT ? FROM games_genre1 WHERE id = ?", (word, id_user))
                        if int(str(cursor.fetchone())[2:-3]) > genre[0]:
                            genre = [int(str(cursor.fetchone())[1:-2]), word]
                    cursor.execute("SELECT genre FROM games_game WHERE title = ?", (lelem[0],))
                    if genre[1] == str(cursor.fetchone())[1:-2]:
                        lelem[1] += 0, 3 * lelem[1]
                    lelem[1] += lelem[1] * new_rait / 6
                cursor.execute("SELECT author_id FROM games_game WHERE title = ?", (lelem[0],))
                cursor.execute("SELECT date_joined FROM games_account WHERE user_id = ?",
                               (int(str(cursor.fetchone())[1:-2]),))
                date_change = 10
                db_date = str(cursor.fetchone())[2:-3].split('-')
                date_old = datetime.datetime(int(db_date[0]), int(db_date[1]), int(db_date[2]))
                date_now = datetime.datetime.now()
                delta = date_now - date_old
                date_change -= delta.days
                top_date = 0
                if date_change > top_date:
                    top_date = date_change
                    lelem[1] += top_date * lelem[1] / 6
        for i in range(len(end_spis) + 1):
            for j in range(len(end_spis)):
                if j != i:
                    if j > i:
                        if end_spis[j][1] > end_spis[i][1]:
                            s = end_spis[j]
                            end_spis[j] = end_spis[i]
                            end_spis[i] = s
        for helem in end_spis:
            tochno_end.append(helem[2])
        conn.close()
        return tochno_end  # возвращает список айди новостей в нужном порядке

    def news(self):  # фильтр новостей, ничего не принимает, но возвращает список айди
        cursor, conn = db()
        cursor.execute("SELECT id FROM games_posts")
        lennn = len(cursor.fetchall())
        cursor.execute("SELECT id FROM games_posts")
        id_spis = []
        for k in range(lennn):
            id_spis.append([str(cursor.fetchone()[1:-2]), 1])
        for id in id_spis:
            cursor.execute("SELECT count_likes FROM games_posts WHERE id = ?", (id,))
            liked = (int(str(cursor.fetchone())[1:-2]))
            cursor.execute("SELECT count_dislikes FROM games_posts WHERE id = ?", (id,))
            disliked = (int(str(cursor.fetchone())[1:-2]))
            id_spis[id_spis.index(id)][1] = liked / disliked
        for i in range(len(id_spis) + 1):
            for j in range(len(id_spis)):
                if j != i:
                    if j > i:
                        if id_spis[j][1] > id_spis[i][1]:
                            s = id_spis[j]
                            id_spis[j] = id_spis[i]
                            id_spis[i] = s
        conn.close()
        return id_spis

    def add_clmn(self, name_genre):
        cursor, conn = db()
        cursor.execute("ALTER TABLE games_account ADD COLUMN '%s' integer" % name_genre)
        spis_genre.append(name_genre)
        conn.close()

    def maiiiin(self):  # фильтр игр , ничего не принимает, но возвращает список игр
        cursor, conn = db()
        games = list_games('games_game')
        for game in games:
            cursor.execute("SELECT rait FROM games_game WHERE id = ?", (game,))
            games[games.index(game)] = [game, (int(str(cursor.fetchone())[1:-2]))]
        for i in range(len(games) + 1):
            for j in range(len(games) - 1):
                if j != i:
                    if j > i:
                        if games[j][1] > games[i][1]:
                            s = games[j]
                            games[j] = games[i]
                            games[i] = s
        conn.close()
        return games

    def genre(self, type):
        cursor, conn = db()

    def translit(self, word, name_table):  # принимает название поста и таблицы
        cursor, conn = db()
        ss = []
        lett = 0
        for key in slovar:
            word = word.replace(key, slovar[key])
        cursor.execute("SELECT url FROM '%s'" % name_table)
        lenn = len(cursor.fetchall())
        cursor.execute("SELECT url FROM '%s'" % name_table)
        for elem in range(lenn):
            ss.append(str(cursor.fetchone())[2:-3])
        while word in ss:
            lett = int(lett)
            lett += 1
            lett = str(lett)
            word = word + lett
        return word

    def comments(self, text):  # фильтр мата принимает на вход строку, возвращает ее же запиканную
        matt = ''
        global_len = 0
        polf = []
        for k in range(len(text)):
            polf.append(text[k])
        for lelemn in polf:
            if lelemn == '.':
                if polf[polf.index(lelemn) + 1] == ' ':
                    polf[polf.index(lelemn)] = ' . '
                else:
                    polf[polf.index(lelemn)] = ' .'
            elif lelemn == ',':
                if polf[polf.index(lelemn) + 1] == ' ':
                    polf[polf.index(lelemn)] = ' , '
                else:
                    polf[polf.index(lelemn)] = ' ,'
        polf = ''.join(polf)
        polf = polf.split(' ')
        for elem in polf:
            for j in range(len(elem)):
                matt += '*'
            if elem.lower() in mat:
                polf[polf.index(elem)] = matt
            matt = ''
        end = ' '.join(polf)
        return end

    def stat(self,
             sex):  # проценты женской/мужской аудитории, принимает список булевых переменных по айди игры, список булевых переменных я сформирую сам, нужно будет только айди игры
        male = 0
        female = 0
        for bull in sex:
            if bull == True:
                male += 1
            else:
                female += 1
        proc_male = male / len(sex) * 100
        proc_female = female / len(sex) * 100
        return proc_male, proc_female


def db():  # функция для базы данных(моя внутренняя)
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor, conn


def raiting(game_id):  # функция для получения рейтинга
    cursor, conn = db()
    cursor.execute("SELECT rating FROM games_game WHERE id = ?", (game_id,))
    return str(cursor.fetchone())[1:-2]


def jsonchik(arg):
    file_name = r'C:/Users/user/PycharmProjects/vigames/back_to_front.json'
    with open(file_name, "w") as write_file:
        json.dump(arg, write_file)


def list_games(kwarg):  # функция для создания списка игр
    cursor, conn = db()
    cursor.execute("SELECT COUNT(*) FROM '%s' WHERE id" % kwarg)
    counter = int(str(cursor.fetchone())[1:-2])
    cursor.execute("SELECT id FROM '%s'" % kwarg)
    games = []
    for gm in range(counter):
        games.append(str(cursor.fetchone())[1:-2])
    return games


start_time = time.time()
print(Search.search(Search(), 'Запись 2', 'news', 0))
print("--- %s seconds ---" % (time.time() - start_time))
'''

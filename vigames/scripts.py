import time
import sqlite3
import os.path
import json
from datetime import date
import datetime
import random


class Search:  # первый аргумент - запрос юзера, второй - флаг games или news.
    global spis_genre, slovar
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
            cursor.execute("SELECT COUNT(*) as count FROM games_posts WHERE title")
            counter = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT title FROM games_posts")
        for k in range(counter):
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
        for lelem in end_spis:
            if games_or_news == 'games':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (lelem[0],))
            if games_or_news == 'news':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (lelem[0],))
            cursor.execute("SELECT rating FROM games_game WHERE id = ?", (int(str(cursor.fetchone())[1:-2]),))
            new_rait = (float(str(cursor.fetchone())[1:-2]))
            for word in spis_genre:
                cursor.execute("SELECT ? FROM games_genre WHERE id = ?", (word, id_user))
                if int(str(cursor.fetchone())[1:-2]) > genre[0]:
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
            for j in range(len(end_spis) - 1):
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

    def raiting(self, rt):
        cursor, conn = db()
        cursor.execute("SELECT rait FROM games_game")

    def news(self, id_user):  # фильтр новостей
        liked = 0
        disliked = 0
        cursor, conn = db()
        proc = []
        cursor.execute("SELECT id FROM games_posts")
        id_spis = cursor.fetchall()
        for id in id_spis:
            cursor.execute("SELECT liked FROM games_posts WHERE id = ?", (id,))
            liked = (int(str(cursor.fetchone())[1:-2]))
            cursor.execute("SELECT disliked FROM games_posts WHERE id = ?", (id,))
            disliked = (int(str(cursor.fetchone())[1:-2]))
            proc.append(liked / disliked)
        for word in spis_genre:
            cursor.execute("SELECT ? FROM games_account WHERE user_id = ?", (word, id_user))
        conn.close()

    def add_clmn(self, name_genre):
        cursor, conn = db()
        cursor.execute("ALTER TABLE games_account ADD COLUMN '%s' integer" % name_genre)
        spis_genre.append(name_genre)
        conn.close()

    def maiiiin(self):
        cursor, conn = db()
        games = list_games('games_game')
        for game in games:
            cursor.execute("SELECT rait FROM games_game WHERE id = ?", (game,))
            games[games.index(game)], games[0] = games[0], games[games.index(game)]
        conn.close()
        return games

    def genre(self, type):
        cursor, conn = db()

    def translit(self, word, name_table):  # название поста и таблицы
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
        print(ss)
        while word in ss:
            lett += 1
            lett = str(lett)
            word = word + lett
        return word


def db():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "db.sqlite3")
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    return cursor, conn


def jsonchik(arg):
    file_name = r'C:/Users/user/PycharmProjects/vigames/back_to_front.json'
    with open(file_name, "w") as write_file:
        json.dump(arg, write_file)


def list_games(kwarg):
    cursor, conn = db()
    cursor.execute("SELECT COUNT(*) FROM ? WHERE id", (kwarg,))
    counter = int(str(cursor.fetchone())[1:-2])
    cursor.execute("SELECT id FROM ?", (kwarg,))
    games = []
    for gm in range(counter):
        games.append(int(str(cursor.fetchone())[1:-2]))
    return games


start_time = time.time()
print(Search.translit(Search(), 'bestgame2', 'games_game'))
print("--- %s seconds ---" % (time.time() - start_time))

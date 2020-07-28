import time
import sqlite3
import os.path


class Search:                                       #первый аргумент - запрос юзера, третий - флаг games или news.
    def search(self, reqst, games_or_news):
        end_spis = []  # словарь с рейтингом названий
        right_letters = 0
        games = []
        bull = 0
        tochno_end = []
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "db.sqlite3")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        if games_or_news == 'games':
            cursor.execute("SELECT title FROM games_game")
        if games_or_news == 'news':
            cursor.execute("SELECT title FROM games_posts")
        for k in range(2):
            games.append(str(cursor.fetchone())[2:-3])
        for elem in games:
            elem.lower()
            for el in range(len(elem)):
                if el < len(reqst):
                    if reqst[el] == elem[el]:
                        right_letters += 1
            if right_letters != 0:
                end_spis.append([elem, right_letters])
            right_letters = 0
        for lelem in end_spis:
            if lelem[1] > bull:
                bull = lelem[1]
                end_spis[end_spis.index(lelem)], end_spis[0] = end_spis[0], end_spis[end_spis.index(lelem)]
        for pelem in end_spis:
            if games_or_news == 'games':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (pelem[0],))
            if games_or_news == 'news':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (pelem[0],))
            tochno_end.append(int(str(cursor.fetchone())[1:-2]))
        conn.close()
        return tochno_end


start_time = time.time()
print(Search.search(Search(), 'xcom', 'games'))
print("--- %s seconds ---" % (time.time() - start_time))

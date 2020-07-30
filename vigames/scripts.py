import time
import sqlite3
import os.path


class Search:  # первый аргумент - запрос юзера, второй - флаг games или news.
    global spis_genre
    spis_genre = ['strategy', 'rpg', 'f2p', 'shooter', 'racing', 'horror', 'stealth', 'sports', 'party',
                  'platform', 'puzzle', 'god_game', 'flight_simulation', 'fighting', 'beatemup', 'adventure',
                  'action']

    def search(self, reqst, games_or_news):
        end_spis = []  # словарь с рейтингом названий
        right_letters = 0
        games = []
        bull = 0
        rait = 0
        genre = 0
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
            if games_or_news == 'games':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (lelem[0],))
            if games_or_news == 'news':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (lelem[0],))
            cursor.execute("SELECT rait FROM games_game WHERE id = ?", (int(str(cursor.fetchone())[1:-2]),))
            if lelem[0] == bull and (int(str(cursor.fetchone())[1:-2])) > rait:
                for word in spis_genre:
                    cursor.execute("SELECT ? FROM games_user", (word,))
                    if int(str(cursor.fetchone())[1:-2]) > genre:
                        rait += 1
                        end_spis[end_spis.index(lelem)], end_spis[0] = end_spis[0], end_spis[end_spis.index(lelem)]
            if lelem[0] == bull and (int(str(cursor.fetchone())[1:-2])) > rait:
                rait = (int(str(cursor.fetchone())[1:-2]))
                end_spis[end_spis.index(lelem)], end_spis[0] = end_spis[0], end_spis[end_spis.index(lelem)]
        for pelem in end_spis:
            if games_or_news == 'games':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (pelem[0],))
            if games_or_news == 'news':
                cursor.execute("SELECT id FROM games_game WHERE title = ?", (pelem[0],))
            tochno_end.append(int(str(cursor.fetchone())[1:-2]))
        conn.close()
        return tochno_end

    def raiting(self, rt):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "db.sqlite3")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT rait FROM games_game")

    def news(self, rt, ):
        pass

    def add_clmn(self, name_genre):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "db.sqlite3")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("ALTER TABLE games_account ADD COLUMN '%s' integer" % name_genre)
        spis_genre.append(name_genre)
        conn.close()


start_time = time.time()
Search.add_clmn(Search(), 'fgjhgj')
print("--- %s seconds ---" % (time.time() - start_time))

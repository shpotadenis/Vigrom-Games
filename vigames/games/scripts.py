import time


class Search:
    def search(self, reqst, games):
        end_spis = {}  # словарь с рейтингом названий
        right_letters = 0
        retturn = []
        for elem in games:
            elem.lower()
            for el in range(len(elem)):
                if el < len(reqst):
                    if reqst[el] == elem[el]:
                        right_letters += 1
            end_spis[elem] = right_letters
            right_letters = 0
        for numm in end_spis:
            if numm >


s = []
for k in range(100000):
    s.append('hohoh')
start_time = time.time()
print(Search.search(Search(), 'xcom', s))
print("--- %s seconds ---" % (time.time() - start_time))

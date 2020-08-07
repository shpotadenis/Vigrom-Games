
def Search_engine(request, data):
    search_depth = 0.2    #Переменная, которая ограничивает выдачу. Должно быть минимум search_depth совпадений, чтобы статья появилась в поиске
    request = request.lower()
    relevance_id_dict = dict()
    relevanse_id_list = []

    set_str = set()
    slog = ''
    for i in request:   # Разбиваем строку на множество типа {м, мн, мно, нож, оже, жес, ест, ств, тво, во, о}
        slog += i
        if len(slog) >= 4:
            slog = slog[-3::]
        elif len(slog) <= 1:
            continue
        set_str.add(slog)
    set_str.add(request[-2::])

    for i in data:
        set_title = set()
        slog = ''
        for k in dict(i)['title'].lower():
            slog += k
            if len(slog) >= 4:
                slog = slog[-3::]
            elif len(slog) <= 1:
                continue
            set_title.add(slog)
        set_title.add(request[-2::])
        set_title.add(request[-1])

        relevance = len(set_str.intersection(set_title)) / len(set_title)
        if relevance in relevance_id_dict:
            relevance_id_dict[relevance].append(i)
        else:
            relevance_id_dict[relevance] = [i, ]
    '''
     Сортирует ключи словаря (количество совпадений) и формирует конечный список 
     с данными статьи/игры в порядке убывания релевантности
    '''
    for i in sorted(relevance_id_dict.keys(), reverse=True):
        if i >= search_depth:
            relevanse_id_list += relevance_id_dict[i]

    return relevanse_id_list



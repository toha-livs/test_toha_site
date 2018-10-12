from operator import itemgetter


test = ['.', ',', ':', ';', '!', '?', '(', ')']
test_str = '.,:;!?()'


def get_count_uqe(a):
    count_g = 0
    all_p = a.split(' ')
    count_a = 0
    for i in all_p:
        for g in test:
            if len(i) == 1:
                    if i == test_str:
                        all_p.pop(count_g)
            if g in i:
                all_p[count_a] = i.replace(g, '')
        count_a += 1
    for h in all_p:
        if h == '':
            all_p.pop(count_g)
        count_g += 1
    output = []
    for x in all_p:
        if x not in output:
            output.append(x)
    return len(output)


def get_list_posts(queryset):
    query_list = []
    for query in queryset:
        suma = get_count_uqe(query['body'])
        query['unique_count'] = suma
        query_list.append(query)
    newlist = sorted(query_list, key=itemgetter('unique_count'))
    newlist.reverse()
    return newlist


def get_for_api(list_dict):
    all = []
    for i in list_dict:
        all.append(i['body'])
    return all
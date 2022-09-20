from collections import deque


def make_graph(data):
    graph = {}
    for tuples in data:
        for names in tuples:
            graph[names] = []
    for i in range(len(data)):
        for k, v in graph.items():
            if k is data[i][0] and k in data[i]:
                v.append(data[i][1])
            elif k is data[i][1] and k in data[i]:
                v.append(data[i][0])
    return graph


def check_relation(data, first, second):
    graph = make_graph(data)

    s_deque = deque()
    s_deque += graph[first]
    searched = []
    while s_deque:
        person = s_deque.popleft()
        if not person in searched:
            if person is second:
                return True
            else:
                s_deque += graph[person]
                searched.append(person)
    return False


if __name__ == "__main__":
    net = (
        ("Ваня", "Лёша"), ("Лёша", "Катя"),
        ("Ваня", "Катя"), ("Вова", "Катя"),
        ("Лёша", "Лена"), ("Оля", "Петя"),
        ("Стёпа", "Оля"), ("Оля", "Настя"),
        ("Настя", "Дима"), ("Дима", "Маша"),
    )
    assert check_relation(net, "Петя", "Стёпа") is True
    assert check_relation(net, "Маша", "Петя") is True
    assert check_relation(net, "Ваня", "Дима") is False
    assert check_relation(net, "Лёша", "Настя") is False
    assert check_relation(net, "Стёпа", "Маша") is True
    assert check_relation(net, "Лена", "Маша") is False
    assert check_relation(net, "Вова", "Лена") is True

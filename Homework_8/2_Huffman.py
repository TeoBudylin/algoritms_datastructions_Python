def Huffman_code(input):
    #запишем в словарь частоты, какой символ сколько раз встречался
    freq = {}
    for el in input:
        if el not in freq:
            freq.update({el: 1})
        else:
            freq.update({el:(freq.get(el) + 1)})

    print(freq)
    # отсортируем наш словарь частот по возрастанию
    sorted_freq = {}
    sorted_frq_values = sorted(freq.values())
    for i in sorted_frq_values:
        for key in freq.keys():
            if freq[key] == i:
                sorted_freq[key] = freq[key]
    print(sorted_freq)
    q = sorted_freq.items()
    print(q)


    class Node:
        def __init__(self, value, left_ch=None, right_ch=None):
            self.value = value
            self.left_ch = left_ch
            self.right_ch = right_ch
    class Tree:
        def __init__(self, root):
            self.root = root

    # for el in q:
    node_1 = Node(q[0][0])
    node_2 = Node(q[1][0])
    node_3 = Node(q[0][1] + q[1][1], left_ch=node_1, right_ch=node_2)
    q[0] = node_3


Huffman_code('beep boop beer!')
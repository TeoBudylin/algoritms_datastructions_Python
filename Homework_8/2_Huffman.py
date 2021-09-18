def Huffman_code(input):
    #запишем в словарь частоты, какой символ сколько раз встречался
    freq = {}
    for el in input:
        if el not in freq:
            freq.update({el: 1})
        else:
            freq.update({el:(freq.get(el) + 1)})

    class Node:
        def __init__(self, left_ch=None, right_ch=None):
            self.left_ch = left_ch
            self.right_ch = right_ch
        def walk(self, code, acc):
            self.left_ch.walk(code, acc + '0')
            self.right_ch.walk(code, acc + '1')

    class Leaf:
        def __init__(self, value):
            self.value = value
        def walk(self, code, acc):
            code[self.value] = acc or '0'

    h=[]
    for ch, freq in freq.items():
        h.append((freq, len(h), Leaf(ch)))

    import heapq
    heapq.heapify(h)
    counter = len(h)
    while len(h) > 1:
        freq_1, _counter_1, left = heapq.heappop(h)
        freq_2, _counter_2, right = heapq.heappop(h)
        heapq.heappush(h, (freq_1 + freq_2, counter, Node(left, right)))
        counter += 1

    code={}
    [(_freq, _counter, root)] = h
    root.walk(code, '')

    print(code)

    codet = ''
    for el in input:
        codet += code.get(el)
    return codet

print(Huffman_code('beep boop beer!'))
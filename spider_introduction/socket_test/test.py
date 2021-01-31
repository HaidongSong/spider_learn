
# a = [1, 2, 3, 4, 5, 6, 7, 8]

# for x in range(1, len(a), 2):
#     print(x, end='|')
#
# b = a[0:len(a):2]
# print(b)
# import re
#
# a = 'ppx1pytho2python2pythonn3'
# b = re.findall('python*', a)
# print(b)

# origin = 0
# #
# #
# # def go(step):
# #     global origin
# #     new_pos = origin +step
# #     origin = new_pos
# #     return new_pos
# #
# #
# # print(go(2))
# # print(go(3))
# # print(go(5))


origin = 0


def factory(pos):
    def go(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


f = factory(origin)
print(f(2))
print(f.__closure__[0].cell_contents)
print(f(3))
print(f.__closure__[0].cell_contents)
print(f(5))
print(f.__closure__[0].cell_contents)

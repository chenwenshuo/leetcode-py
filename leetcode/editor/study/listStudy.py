# list1 = ['beijing', 'shanghai', 'tianjin', 'qingdao', 'heze']
#
# print(list1)
#
# print(sorted(list1))
#
# print(list1)
#
# print(sorted(list1, reverse=True))
#
# print(list1.reverse())
#
# print(list1)
#
# list1.reverse()
#
# print(list1)
#
# list1.sort()
# print(list1)
#
# list1.sort(reverse=True)
# print(list1)
#
# print(len(list1))
#
# print(list1[-1])
#
# for d in list1:
#     d = d + '1'
# # 不会改变
# print(list1)
#
# nums = list(range(1, 6))
# print(nums)
#
# nums1 = list(range(0, 11, 2))
# print(nums1)
#
# for i in range(1, 11):
#     nums1.append(i ** 2)
#
# print(nums1)
#
# print(min(nums1))
# print(max(nums1))
# print(sum(nums1))
#
# nums2 = [v ** 2 for v in range(1, 11)]
#
# print(nums2)


def test():
    nums3 = [a for a in range(1, 101)]
    print(nums3)
    nums4 = [a for a in range(1, 1000001)]
    print(sum(nums4))

    nums4 = [a for a in range(1, 21, 2)]
    print(nums4)

    nums4 = [a for a in range(3, 31, 3)]
    print(nums4)

    nums4 = [a ** 3 for a in range(1, 11)]

    for i in nums4:
        print(i)


def test2():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    print(players[0:3])
    print(players[1:4])
    print(players[:4])
    print(players[2:])
    print(players[-3:])
    pass


def test3():
    players = ['charles', 'martina', 'michael', 'florence', 'eli']
    p2 = players[:]
    print(p2)
    p2.append("test")
    print(p2)
    print(players)
    pass


def test4():
    yuanzu = (100, 200)
    # yuanzu[0]=0
    print(yuanzu)
    pass


def test5():
    te = {'a': 1, 'b': 2}
    te['c'] = 3
    del te['c']
    print(te)
    pass


def test6():
    user = {
        'name': 'whx',
        'age': 18,
        'email': 'xxx@lenovo.com'
    }
    print(user)
    for key, v in user.items():
        print(key)
        print(v)
    print(user.values())
    print(user.keys())

    print(user)
    pass


def test7():
    user1 = user = {
        'name': 'whx',
        'age': 18,
        'email': 'xxx@lenovo.com'
    }
    user2 = {
        'name': 'whx2',
        'age': 18,
        'email': 'xxx@lenovo.com'
    }
    user3 = {
        'name': 'whx3',
        'age': 18,
        'email': 'xxx@lenovo.com'
    }
    user_list = [user1, user2, user3]
    print(user_list)

    for user in user_list:
        print(user)

    favorite_places = {
        'user1': ['beijing', 'b'],
        'user2': ['shanghai', 'c']

    }

    for key, v in favorite_places.items():
        print(key ,':',v)
    pass


def test8():
    mes = input('please input:')
    print(mes)
    pass


if __name__ == '__main__':
    # test()
    test8()

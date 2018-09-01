import random


def initAry():
    nameList = ['贝贝', 'Ren', '星儿', 'kelly', 'lpl', '心怡', '幸福', '梦', '李', 'Anne', '七柚的柚子', 'KidsYa'
        , '女少', 'Klitschko', 'Ar', 'Najin', '陈天树', 'Chikara', 'Lester', '小小风茗', '汤达人红烧牛肉面'
        , 'The', '腾腾', '晚安', 'Asterisk', 'Good_Nine9', '开心果', 'Sandm', '0 error', '池影落', '余炳炫'
        , '坚定的锡兵', '天志', '死了才要爱', '北鱼', '我有冒险的梦', '张章', 'BGYU', '陌路丶memory', 'Kaleidoscope'
        , 'Bob', '等风来', '魏舞阳', 'Tyl', '丰芑', 'FORZA,米兰', '什么什么名字', '董陆木木木', '（&.&）'
        , '李昭星', '1234', '李俊洁 ', '静 ', '可可可可可悦 ', '划啊划~ ', 'IcarusWing ', '阿紫皮皮旦 '
        , '金小秀 ', '莉莉 ', '薛定谔放我出去 ', '雪国蓝梦 ', 'z宇、 ', '李章鱼 ', '就要看你皮 ', '世界级宝贝 '
        , '王璐^ ', '刘艺伟 ', 'Clara ', '江正经 ', '待木叶下 ', '初晓迟暮 ', '北梦 ', 'Seekhow ', 'F', 'never more '
        , 'Hamilton ', 'gone ', '罗高庭 ', '文红皓 (SN1006) ', '汪鸣 (Robin) ', '周鹤洋 (梦渡)', '刘星池 (今夜星辰) ']
    return nameList


if __name__ == '__main__':
    Ary = initAry()
    print(Ary[random.randint(0, len(Ary)-1)])
    print(Ary[random.randint(0, len(Ary)-1)])

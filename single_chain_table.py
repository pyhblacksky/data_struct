
# 定义链表节点类
class Node(object):
    '''
    data 节点保存数据
    _next 下一个节点
    '''
    def __init__(self, item):
        self.data = item
        self.next = None

class chain_table(object):
    '''
    构造单链表
    '''
    def __init__(self, headnode=None):
        """初始化一个单链表默认结点"""
        self.head = headnode

    def isEmpty(self):
        """判断链表是否为空"""
        return self.head == None

    def length(self):
        """链表长度"""
        """定义游标来指向当前head"""
        cur = self.head
        """定义计数变量来记录长度，初始值设置为0"""
        count = 0
        while cur != None:
            cur = cur.next
            count += 1
        return count


    def append_node(self, item):
        '''
        末尾追加一个结点
        定义游标使游标指向末尾结点即可
        :param node:
        :return:
        '''
        cur = self.head
        if cur == None:
            self.head = Node(item)
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)

    # 指定位置插入结点
    def insert_pos(self, pos, item):
        if not isinstance(pos, int):
            raise TypeError("位置参数必须为整数")
        cur = self.head
        if self.length() <= pos:
            raise TypeError("超出索引范围")
        if pos == 0:   # 插入头结点之前
            next_node_next = self.head
            self.head = Node(item)
            self.head.next = next_node_next
            return True
        count = 0
        while cur != None:
            """当前next地址"""
            next_cur = cur.next
            if count == pos - 1:
                next_node = cur.next
                insert_node = Node(item)
                insert_node.next = next_cur
                cur.next = insert_node
                return True
            cur = cur.next
            count += 1


    def remove_node(self, item):
        """移除一个结点"""
        cur = self.head
        """使用双游标标记一前一后结点"""
        pre = None
        while cur != None:
            if cur.data == item:
                """处理头结点和列表只有一个元素的特殊情况"""
                if cur == self.head:
                    self.head = cur.next
                    return True
                else:
                    pre.next = cur.next
                    return True
            else:
                pre = cur
                cur = cur.next

    def search_node(self, item):
        """查看结点是否存在"""
        cur = self.head
        while cur != None:
            if cur.data == item:
                return True
            cur = cur.next
        return False

    def list_each(self):
        """遍历单链表"""
        cur = self.head
        while cur != None:
            print(cur.data, end='')
            if cur.next != None:
                print("-->", end='')
            cur = cur.next

    def view(self):
        node = self.head
        linkstr = ""
        while node is not None:
            if node.next is not None:
                linkstr = linkstr + str(node.data) + "-->"
            else:
                linkstr += str(node.data)
            node = node.next
        print(linkstr)


if __name__ == '__main__':

    obj = chain_table()
    obj.append_node("first")
    obj.append_node("second")
    obj.append_node("third")
    obj.view()
    print("The chain_table length : ", obj.length())

    obj.insert_pos(2, "one")
    obj.view()
    print("The chain_table length : ", obj.length())

    obj.remove_node("second")
    obj.view()
    print("The chain_table length : ", obj.length())
    obj.list_each()


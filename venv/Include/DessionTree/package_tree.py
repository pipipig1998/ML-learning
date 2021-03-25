from treelib import Tree,Node
if __name__ == '__main__':
    # 树的创建，每个节点都有唯一的identifier作为标记，可以手动指定
    tree=Tree()
    # 增加树的节点,tag是树输出时的显示，identifier是唯一标志，根节点可以不指定父
    tree.create_node(tag='root',identifier='root',data=0)
    tree.create_node(tag='1_child',identifier='1_child',data=1,parent='root')
    tree.create_node(tag='2_child', identifier='2_child', data=2,parent='root')
    tree.create_node(tag='3_child', identifier='3_child', data=3,parent='1_child')

    # 树的粘贴，需要注意的是这个nid是tree的identifier，不是tree2的
    tree2 = Tree()
    tree2.create_node(tag='tutu', identifier='tutu', data=0)
    tree.paste(nid='root',new_tree=tree2)

    # 删除树的节点
    tree.remove_node('tutu')
    # 移动树的节点
    tree.move_node('3_child','root')
    # 打印树的结构
    tree.show()
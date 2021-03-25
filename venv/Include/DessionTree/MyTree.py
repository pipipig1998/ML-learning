
# 层次遍历树，找到父节点，然后在父节点后边添加{value:{}}
def insert(root,parent,value):
    if parent in root.keys():
        root[parent].update({value:{}})
    else:
        for v in root.values():
            insert(v,parent,value)
# 删除一个节点
def delete(root,key):
    if key in root.keys():
        root.pop(key)
    else:
        for v in root.values():
            delete(v,key)
# 修改树节点的值，但是他这里是hash值所以只能变相的pop出来然后形成更新后的索引
def myupdate(root,oldkey,key):
    if oldkey in root.keys():
        root.update({key:root.pop(oldkey)})
    else:
        for v in root.values():
            myupdate(v,oldkey,key)
def show(root):
    print(root)
if __name__ == '__main__':
    root={'root':{}}
    insert(root,'root','fist_child')
    insert(root,'root','second_child')
    insert(root,'fist_child','ff_child')
    myupdate(root,'ff_child','update')
    show(root)

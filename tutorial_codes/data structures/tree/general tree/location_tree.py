class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        while self.parent:
            level += 1
            self = self.parent
        return level
    
    def print_tree(self,level):
        curr = self.get_level()
        if curr > level:
            return
        spaces = '   '*curr
        prefix = spaces + "|__" if self.parent else ""
        print(prefix +self.data)
        if len(self.children) > 0 :
            for child in self.children:
                child.print_tree(level)




def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")
    usa = TreeNode("USA")
    
    root.add_child(india)
    root.add_child(usa)

    gujarat = TreeNode("Gujarat")
    karnataka = TreeNode("Karnataka")

    india.add_child(gujarat)
    india.add_child(karnataka)

    gujarat.add_child(TreeNode("Ahmedabd"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka.add_child(TreeNode("Bangalore"))
    karnataka.add_child(TreeNode("Mysore"))

    new_jersey = TreeNode("New Jersey")
    california = TreeNode("California")
    usa.add_child(new_jersey)
    usa.add_child(california)

    new_jersey.add_child(TreeNode("Princeton"))
    new_jersey.add_child(TreeNode("Trenton"))
    
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    return root

if __name__ == '__main__':
    root = build_location_tree()
    root.print_tree(1)
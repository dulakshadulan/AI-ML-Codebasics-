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
    
    def print_tree(self):
        spaces = '   '*self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(prefix +self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Electronics")

    laptops = TreeNode("Laptops")
    laptops.add_child(TreeNode("Mac"))
    laptops.add_child(TreeNode("Acer"))
    laptops.add_child(TreeNode("Msi"))

    phones = TreeNode("Phones")
    phones.add_child(TreeNode("iPhone"))
    phones.add_child(TreeNode("Samsung"))
    phones.add_child(TreeNode("Google Pixel"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Sony")) 

    root.add_child(laptops)
    root.add_child(phones)
    root.add_child(tv)

    print(tv.get_level())

    return root



if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()



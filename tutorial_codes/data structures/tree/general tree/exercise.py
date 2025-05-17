class TreeNode:
    def __init__(self,name, designation):
        self.name = name
        self.designation = designation
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
    
    def print_tree(self,structure):
        if structure == "both":
            value = f'{self.name} ({self.designation})'

            

        elif structure == "name":
            value = self.name
        
        elif structure == "designation":
            value = self.designation
        
        spaces = '   '*self.get_level()
        prefix = spaces + "|__" if self.parent else ""
        print(f'{prefix}{value}')
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(structure)


def build_management_tree():
    root = TreeNode("Nilupul", "CEO")


    cto = TreeNode("Chinmay","CTO")
    head = TreeNode("Gels","HR Head")

    root.add_child(cto)
    root.add_child(head)

    inf_h = TreeNode("Vishwa", "Infrastructure Head")
    app_h = TreeNode("Aamir","Application Head")

    cto.add_child(inf_h)
    cto.add_child(app_h)

    cm = TreeNode("Dhaval", "Cloud Manager")
    am = TreeNode("Abhijit","App Manager")
    inf_h.add_child(cm)
    inf_h.add_child(am)

    rm = TreeNode("Peter","Recruitment Manager")
    pm = TreeNode("Waqas", "Policy Manager")
    head.add_child(rm)
    head.add_child(pm)

    return root

if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("name") # prints only name hierarchy
    root_node.print_tree("designation") # prints only designation hierarchy
    root_node.print_tree("both") # prints both (name and designation) hierarchy


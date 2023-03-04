class TreeNode:
    def __init__(self,place):
        self.place = place
        self.children=[]
        self.parent = None
        
    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self,level):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        print(prefix,self.place)
        if self.get_level() <= level-1:
            for child in self.children:
                child.print_tree(level)
        
def build_location_tree():
    root = TreeNode('Global')

    #india ____________________________________
    india = TreeNode('india')
    root.add_child(india)

        #gujarat __________________________________
    gujarat = TreeNode('Gujarat')
    india.add_child(gujarat)
    gujarat.add_child(TreeNode('Ahmedabad'))
    gujarat.add_child(TreeNode('Baroda'))

        #Karnataka_________________________________
    karnataka = TreeNode('Karnataka')
    india.add_child(karnataka)
    karnataka.add_child(TreeNode('Bangluru'))
    karnataka.add_child(TreeNode('Mysore'))


    #USA_____________________________________
    usa = TreeNode('USA')
    root.add_child(usa)

        #New Jersey__________________________________
    nj = TreeNode('New Jersey')
    usa.add_child(nj)
    nj.add_child(TreeNode('Princeton'))
    nj.add_child(TreeNode('Trenton'))

        #California__________________________________
    cal = TreeNode('California')
    usa.add_child(cal)
    cal.add_child(TreeNode('San Francisco'))
    cal.add_child(TreeNode('Mountain View'))
    cal.add_child(TreeNode('Palo Alto'))




    return root


if __name__ =='__main__':
    root = build_location_tree()
    root.print_tree(3)
    pass
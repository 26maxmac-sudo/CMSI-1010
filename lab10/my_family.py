class Person:
    def __init__(self, name, born=None, died=None, mom=None, dad=None, sibling=None):
        self.name = name
        self.born = born
        self.died = died
        self.mom = mom
        self.dad = dad
        self.sibling = sibling
        if sibling is not None and sibling.sibling is None:
            sibling.sibling = self
  
    def is_sibling_of(self, other):
        same_mom = self.mom is not None and other.mom is not None and self.mom is other.mom
        same_dad = self.dad is not None and other.dad is not None and self.dad is other.dad
        # Half or full, we don't care
        return same_mom or same_dad


    def __str__(self):
        span = f"({self.born or '?'}-{self.died or '?'})"
        mom = f"{self.mom.name if self.mom is not None else '?'}"
        dad = f"{self.dad.name if self.dad is not None else '?'}"
        sibling = f"{self.sibling.name if self.sibling is not None else '?'}"
        return f"{self.name} {span} mom: {mom}, dad: {dad}, sibling: {sibling}"

    def print_family_tree(self, prefix="", level=0):
        """Print the family tree starting from this person."""
        indent = "    " * level
        print(f"{prefix}{self.name} {self.born or '?'}-{self.died or '?'}")
        if self.mom:
            self.mom.print_family_tree(f"  {indent}mom: ", level + 1)
        if self.dad:
            self.dad.print_family_tree(f"  {indent}dad: ", level + 1)

Richard = Person("Richard MacDonald", born=1926, died=2003)
Mariane = Person("Mariane MacDonald", born=1941)
Don = Person("Don MacDonald", born=1940, died=1996)
Mary = Person("Mary MacDonald", born=1942, died=2017)
Melissa = Person("Melissa MacDonald", born=1973, mom=Mariane, dad=Don)
Morgan = Person("Morgan MacDonald", born=1968, mom=Mary, dad=Richard)
meghan = Person("Meghan MacDonald", born="2000", mom=Melissa, dad=Morgan, sibling=max)
max = Person("Max MacDonald", born="2004", mom=Melissa, dad=Morgan, sibling=meghan)

print(Melissa)

from lsystem import Grammar
from lsysrules import lrules, laxiom

if __name__ == "__main__":
        
    fractal_tree = Grammar(laxiom, lrules)
    print(fractal_tree.produce(3))
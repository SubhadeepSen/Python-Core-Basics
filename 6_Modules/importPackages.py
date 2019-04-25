#import the module one
from packageOne import one
#import module one with alias
from packageOne import one as mainPackage

#import the module two
from packageOne.packageTwo import two
#import module two with alias
from packageOne.packageTwo import two as subPackage

one.one();
mainPackage.one();

two.two();
subPackage.two();

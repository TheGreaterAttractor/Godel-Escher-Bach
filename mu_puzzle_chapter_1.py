#"Can you produce MU?" is the puzzle. To begin with, you will be supplied with a string.
# Not to keep you in suspense, that string will be MI. Then you will be told some rules, with which you can change one 
# string into another.
# RULE I: If you possess a string whose last letter is I, you can add on a U at the end. 
# RULE II: Suppose you have Mx. Then you may add Mxx to your collection
# RULE III: If III occurs in one of the strings in your collection, you may make a new string with U in place of III
# RULE IV: If UU occurs inside one of your strings, you can drop it. 

# attempt
from random import randrange, choice
from random  import choice as choose

class Formalism:
    axiom = 'MI'
    theorems = []

    #---------------
    #utility methods
    @staticmethod
    def shortest_string(s):
        return sorted(s, key=len)[0]

    @staticmethod
    def last_char_of(s,c):
        return s[len(s)-1] == c

    @staticmethod
    def is_Mx(s):
        return s[0] == 'M' and len(s) >1 

    @staticmethod
    def triple_I_occurs_in(s):
        return True if s.find('III') > 0 else False
    @staticmethod
    def double_U_occurs_in(s):
        return True if s.find('UU') > 0 else False
    
    #---------------
    #rule methods
    @staticmethod
    def append_U(s):
            return s+'U' 

    @staticmethod
    def duplicate_suffix(s):
        return s + s[1:]

    @staticmethod
    def replace_triple_I_with_U(s, count = 1):
        return s.replace('III', 'U', count)
    
    @staticmethod
    def drop_double_U(s):
        return s.replace('UU','',1)

    # method to determine the applicable rules given a string (theorem)
    def applicable_rules(self,s):
        rules = []
        if self.last_char_of(s,'I'):
            #rule 1 is applicable
            rules.append(self.append_U)

        if self.is_Mx(s):
            #rule 2 is applicable
            rules.append(self.duplicate_suffix)

        if self.triple_I_occurs_in(s):
            #rule 3 is applicable
            rules.append(self.replace_triple_I_with_U)

        if self.double_U_occurs_in(s):
            #rule 4 is applicable
            rules.append(self.drop_double_U)
        return rules

    def __repr__(self):
        return 'Formalism->Axiom:{}, theorems:{}'.format(self.axiom, self.theorems)

    #print out a certain number of valid strings(theorems)
    def churn_theorems(self, n):

        #the base string (axiom) is the first theorem
        self.theorems.append(self.axiom)

        for i in range(n):
            #get a list of the rules applicable to the current theorem
            rules = self.applicable_rules(self.theorems[i])

            #choose a rule at random and apply
            result = choose(rules)(self.theorems[i])

            #the string 'MIU' is particularly problematic because beyond it only rule 2 is applicable till infinity
            #so i avoid it
            while result == 'MIU':
                choice = randrange(0,len(rules))
                result = rules[choice](self.theorems[i])
            self.theorems.append(result)


my_formalism = Formalism()
my_formalism.churn_theorems(4)
print(my_formalism)





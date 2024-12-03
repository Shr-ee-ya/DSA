class Solution(object):
    def addSpaces(self, s, spaces):
        res=[]
        i=0  
        for j in spaces:
            res.append(s[i:j])
            res.append(" ")  
            i=j 
        res.append(s[i:])
        return "".join(res)


        
       




        '''
        for i in range(len(spaces)):  # cause everytime we add a space 
            spaces[i]=spaces[i]+i     # the index value where space needs to be added also increases by one 

        for i in spaces:
            s=" ".join([s[:i], s[i:]]) 
        return s
    '''

    '''  for i in spaces:
            s.insert(i," ")
        return "".join(s) ''' 

        
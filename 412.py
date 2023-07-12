class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        storage = []
        i=1
        for c in range(n):

            if i%3==0 and i%5==0:
                storage.append("FizzBuzz")
            
            elif i%3 ==0:
                storage.append("Fizz")
            
            elif i%5==0:
                storage.append("Buzz")
            
            else:
                storage.append(str(i))
            i+=1
        return(storage)
    
    
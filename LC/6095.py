class Solution(object):
    def strongPasswordCheckerII(self, password):
        """
        :type password: str
        :rtype: bool
        """
        lowercase = "qwertyuiopasdfghjklzxcvbnm"
        isLower = False
        uppercase = "QWERTYUIOPASDFGHJKLZXCVBNM"
        isUpper = False
        digit = "1234567890"
        isDigit = False
        special = "!@#$%^&*()-+"
        isSpecial = False

        if len(password) < 8:
            return False
        
        for i in password:
            if i in lowercase:
                isLower = True
            if i in uppercase:
                isUpper = True
            if i in digit:
                isDigit = True
            if i in special:
                isSpecial = True
        
        if ((not isLower) or (not isUpper) or (not isDigit) or (not isSpecial)):
            return False
        
        cur = password[0]
        for i in range(1,len(password)):
            if password[i] == cur:
                return False
            cur = password[i]
        return True


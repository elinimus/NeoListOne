"""
    neolist.py
    
    @version     0.11
    @author      Stoyan Elinov <info@elinimus.org>
    @copyright   2016 Stoyan Elinov
    @license     {@link  https://opensource.org/licenses/MIT}

"""
import inspect


class NeoListOne():
    """
    Implements different statements 
    in the place of the indexing operation
    """
    
    
    def __init__(self, hn=None, statement=None):
        """
        initializes the list
        
        """
        self.list=[]
        
        if not (hn or statement):
            pass
            
        elif isinstance(hn, int) and not statement:
            self.list = [0 for i in range(hn)]
            
        elif isinstance(hn, list):
            self.list = hn
            
        elif isinstance(hn, tuple):
            self.list = list(hn)
            
        elif isinstance(hn, int) and isinstance(statement, str):
            for x in range(hn):
                self.list.append(eval(statement))
                
        else:
            raise TypeError("Wrong type of the first argument." +
                             "Check the docs")
                
                
    def __setitem__(self, key, value):
        """
        dispatching the commands of writing operations
        
        """
        if isinstance(key, int):
                self.list[key] = value  # standard list behaviour
                return
                
        # filter function is supplied in the brackets
        if callable(key):
            self._func_filter_set(key, value) 
            return
                
        command = key = key.strip()
                
        if str(command)[:5] == 'slice':
            for x in range(len(self.list))[key]:
                self.list[x] = value
                
        elif command[:6] == 'append':
            self._append(key, value)
            
        elif command[:6] == 'insert':
            self._insert(key, value)
            
        elif command[:4] == 'push':
            self.list.append(value)
            return value
            
        else:
            return self._filter_set(key, value)
            
            
    def __getitem__(self, key):
        """
        dispatching the commands of reading or
        serving operations
        
        """
        if isinstance(key, int):
                return self.list[key]   # standard list behaviour
        
        # filter function is supplied in the brackets        
        if callable(key):
            return self._func_filter_get(key)
            
                
        FIRST_ELEMENT = 0
        LAST_ELEMENT = -1
        
        s = key.split(':')
        command = s[FIRST_ELEMENT].strip()
        
        if command[:5] == 'count':
            return self._count(key)

        elif command[:6] == 'delete':
            self._delete(key)

        elif command[:5] == 'index':
            return self._index(key)

        elif command[:3] == 'len':
            return len(self.list)

        elif command[:7] == 'popleft':
            # must be before 'pop'
            r = self.list[FIRST_ELEMENT]
            del self.list[FIRST_ELEMENT]
            return r

        elif command[:3] == 'pop':
            r = self.list[LAST_ELEMENT]
            del self.list[LAST_ELEMENT]
            return  r
            
        elif command[:7] == 'descend':
            self.list.reverse()
            
        elif command[:6] == 'ascend':
            self.list.sort()
            
        elif command[:7] == 'reverse':
            self.list.reverse()
            
        elif command[:4] == 'sort':
            self.list.sort()
            
        else:
            return self._filter_get(key)
            
            
    @staticmethod        
    def _contain_x(expr):
        """
        checks if expr contains 'x'
        
        """
        FIRST_CHAR = 0
        if expr.index('x') or expr[FIRST_CHAR] == 'x':
            return True
        return False
        
        
    @staticmethod        
    def _contain_y(expr):
        """
        checks if expr contains 'y'
        
        """
        FIRST_CHAR = 0
        if expr.index('y') or expr[FIRST_CHAR] == 'y':
            return True
        return False
        
            
    def _append(self, key, value):
        """
        appends values to the end of the list
        
        """
        FIRST_CHAR = 0
        ONE_EXPRESSION = FIRST_EXPRESSION = 1
        TWO_EXPRESSIONS = SECOND_EXPRESSION = 2
        THREE_EXPRESSIONS = THIRD_EXPRESSION = 3
        # x - index
        # y - value
        
        s = key.split(':')
        
        if len(s) == ONE_EXPRESSION:
            self.list.append(value)
            
        if len(s) == TWO_EXPRESSIONS and not callable(value):
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]):
                    if isinstance(value, (list, tuple)):
                        for x in range(len(value)):
                            # weird construction so that the
                            # returned 0 to be != False 
                            if not (eval(s[FIRST_EXPRESSION]) is False):
                                self.list.append(value[x])
                    else:
                        UPPER_LIMIT = s[FIRST_EXPRESSION].split('<')[1]
                        try:
                            for x in range(int(UPPER_LIMIT)):
                                self.list.append(value)
                        except ValueError:
                            raise UnimplementedError
            except ValueError:
                try: 
                    if self._contain_y(s[FIRST_EXPRESSION]):
                        if isinstance(value, (list, tuple)):    
                            for x in range(len(value)):
                                y = value[x]
                                if eval(s[FIRST_EXPRESSION]):
                                    self.list.append(y)
                        else:
                            y = value
                            if eval(s[FIRST_EXPRESSION]):
                                self.list.append(y)
                            
                except ValueError:
                    if s[FIRST_EXPRESSION] == '':
                        self.list.append(value)
            
                    
        elif len(s) == TWO_EXPRESSIONS and callable(value):
            try: 
                if  self._contain_x(s[FIRST_EXPRESSION]):
                    UPPER_LIMIT = s[FIRST_EXPRESSION].split('<')[1]
                    for x in range(int(UPPER_LIMIT)):
                        self.list.append(value(x,None))
            except ValueError:
                filename, linenum, funcname = \
                inspect.getframeinfo(inspect.currentframe())[:3] 
                print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
                                
        elif len(s) == THREE_EXPRESSIONS and not callable(value):
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]) and \
                   self._contain_y(s[SECOND_EXPRESSION]):
                        
                        for x in range(len(value)):
                            y = value[x]
                            if  eval(s[FIRST_EXPRESSION]) and \
                                eval(s[SECOND_EXPRESSION]):
                                self.list.append(y)
            except ValueError:
                filename, linenum, funcname = \
                inspect.getframeinfo(inspect.currentframe())[:3] 
                print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
                    
        elif len(s) == THREE_EXPRESSIONS and callable(value):
            try: 
                if  self._contain_x(s[FIRST_EXPRESSION]):
                    UPPER_LIMIT = s[FIRST_EXPRESSION].split('<')[1]
                    for x in range(int(UPPER_LIMIT)):
                        y = value(x,None)
                        if eval(s[SECOND_EXPRESSION]):
                            self.list.append(y)
            except ValueError:
                filename, linenum, funcname = \
                inspect.getframeinfo(inspect.currentframe())[:3] 
                print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
        
                
    def _count(self, key):
        """
        counts instances of a value
        
        """
        TWO_EXPRESSIONS = 2
        FIRST_EXPRESSION = 1
        
        s = key.split(':')[1]
        
        if len(s) != TWO_EXPRESSIONS or \
           s[FIRST_EXPRESSION].strip() == '':
            raise ValueError("Missing a value to count. Syntax: " +
                             "name['count: number']")
        
        try:
            key = int(s[1])
        except:
            pass
        
        cnt = 0    
        for x in range(len(self.list)):
            if self.list[x] == key:
                cnt +=1
        
        return cnt
        
        
    def _delete(self,key):
        """
        deletes elements from the list
        
        """
        FIRST_CHAR = 0
        ONE_EXPRESSION = FIRST_EXPRESSION = UPPER_LIMIT = 1
        TWO_EXPRESSIONS = SECOND_EXPRESSION = 2
        THREE_EXPRESSIONS = THIRD_EXPRESSION = 3
        FOUR_EXPRESSIONS = 4
        # x - index
        # y - value
        
        s = key.split(':')
        
        if len(s) == ONE_EXPRESSION:
            del self.list[:]
            
        elif len(s) == TWO_EXPRESSIONS:
            if s[FIRST_EXPRESSION].strip() == '':
                del self.list[:]
            else:
                try:
                    if isinstance(int(s[FIRST_EXPRESSION]), int):
                        del self.list[int(s[FIRST_EXPRESSION])]
                except ValueError:
                    try:
                        if self._contain_y(s[FIRST_EXPRESSION]):
                            z=0
                            for x in range(len(self.list)):
                                x -=z
                                y = self.list[x]
                                if eval(s[FIRST_EXPRESSION]):
                                    z +=1 #to avoid 'out of range' error
                                    del self.list[x]
                                
                    except ValueError:
                        filename, linenum, funcname = \
                        inspect.getframeinfo(inspect.currentframe())[:3] 
                        print(("Uknown Expression @ file:{}, line: {},"+
                              "function: {}").format(filename, \
                                                    linenum, funcname))
                
        elif len(s) == THREE_EXPRESSIONS:
            first = second = third = None
            try:
                first = int(s[FIRST_EXPRESSION])
            except ValueError:
                pass
            try:
                second = int(s[SECOND_EXPRESSION])
            except ValueError:
                pass
            
            del self.list[slice(first, second, third)]
                     
        elif len(s) == FOUR_EXPRESSIONS:
            first = second = third = None
            try:
                first = int(s[FIRST_EXPRESSION])
            except ValueError:
                pass
            try:
                second = int(s[SECOND_EXPRESSION])
            except ValueError:
                pass
            try:
                third = int(s[THIRD_EXPRESSION])
            except ValueError:
                pass
                
            del self.list[slice(first, second, third)]
            
        else:
            raise UnimplementedError
            
            
    def _insert(self, key, value):
        """
        inserts element into index position
        
        """
        TWO_EXPRESSIONS = 2
        FIRST_EXPRESSION = 1
        
        s = key.split(':')
        if len(s) != TWO_EXPRESSIONS:
            raise ValueError("Problems with the argument")
        try:
            x = int(s[FIRST_EXPRESSION])
        except ValueError:
            print('The argument value should be an integer')
        
        self.list.insert(x, value)
        
        
    def _index(self, key):
        """
        returns the smallest index of a value
        
        """
        # x - index
        # y - value
        TWO_EXPRESSIONS = 2
        FIRST_EXPRESSION = 1
        
        s = key.split(':')
        if len(s) != TWO_EXPRESSIONS or \
           s[FIRST_EXPRESSION].strip() == '':
            raise ValueError("Missing a value to count. Syntax:" +
                             "name['index: value']")
        
        SECOND_EXPRESSION = s[1].strip()
        
        for x in range(len(self.list)):
            if not isinstance(self.list[x], str):
                r = str(self.list[x])
            else:
                r = self.list[x]
            if SECOND_EXPRESSION == r:
                return x
        return None
        
        
    def _filter_set(self, key, value):
        """
        In-place index:value read filters
        
        """
        FIRST_EXPRESSION = FIRST_CHAR = 0
        ONE_EXPRESSION = SECOND_EXPRESSION = 1
        TWO_EXPRESSIONS  = 2
        # x - index
        # y - value
        
        s = key.split(':')
        t = [] # temporary list

        if len(s) == ONE_EXPRESSION:
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]):
                    if callable(value):
                        for x in range(len(self.list)):
                            if eval(s[FIRST_EXPRESSION]):
                                self.list[x] = value(x,self.list[x])
                    else:
                        for x in range(len(self.list)):
                            if eval(s[FIRST_EXPRESSION]):
                                self.list[x] = value
            except ValueError:
                try: 
                    if self._contain_y(s[FIRST_EXPRESSION]):
                        if callable(value):
                            for x in range(len(self.list)):
                                y = self.list[x]
                                if eval(s[FIRST_EXPRESSION]):
                                    self.list[x] = value(x,y)
                        else:
                            for x in range(len(self.list)):
                                y = self.list[x]
                                if eval(s[FIRST_EXPRESSION]):
                                    self.list[x] = value
                except ValueError:
                    filename, linenum, funcname = \
                    inspect.getframeinfo(inspect.currentframe())[:3] 
                    print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
                    
        elif len(s) == TWO_EXPRESSIONS:
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]) and \
                   self._contain_y(s[SECOND_EXPRESSION]):
                    if callable(value):
                        for x in range(len(self.list)):
                            y = self.list[x]
                            if eval(s[FIRST_EXPRESSION]) and \
                               eval(s[SECOND_EXPRESSION]):
                                self.list[x] = value(x,y)
                    else:
                        for x in range(len(self.list)):
                            y = self.list[x]
                            if eval(s[FIRST_EXPRESSION]) and \
                               eval(s[SECOND_EXPRESSION]):
                                self.list[x] = value
            except ValueError:
                    filename, linenum, funcname = \
                    inspect.getframeinfo(inspect.currentframe())[:3] 
                    print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
        else:
            raise UnimplementedError
         
            
    def _filter_get(self, key):
        """
        In-place index:value write filters
        
        """
        FIRST_EXPRESSION = FIRST_CHAR = 0
        ONE_EXPRESSION = SECOND_EXPRESSION = 1
        TWO_EXPRESSIONS  = 2
        # x - index
        # y - value
        
        s = key.split(':')
        t = []  # temporary list
        
        
        if len(s) == ONE_EXPRESSION:
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]):
                    for x in range(len(self.list)):
                        if eval(s[FIRST_EXPRESSION]):
                            t.append(self.list[x])
                    return t
            except ValueError:
                try: 
                    if self._contain_y(s[FIRST_EXPRESSION]):
                        for x in range(len(self.list)):
                            y = self.list[x]
                            if eval(s[FIRST_EXPRESSION]):
                                t.append(y)
                        return t
                except ValueError:
                    filename, linenum, funcname = \
                    inspect.getframeinfo(inspect.currentframe())[:3] 
                    print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
        elif len(s) == TWO_EXPRESSIONS:
            try: 
                if self._contain_x(s[FIRST_EXPRESSION]) and \
                   self._contain_y(s[SECOND_EXPRESSION]):
                    for x in range(len(self.list)):
                        y = self.list[x]
                        if eval(s[FIRST_EXPRESSION]) and \
                           eval(s[SECOND_EXPRESSION]):
                            t.append(y)
                    return t
            except ValueError:
                    filename, linenum, funcname = \
                    inspect.getframeinfo(inspect.currentframe())[:3] 
                    print(("Uknown Expression @ file: {}, line: {}," +
                    "function: {}").format(filename, linenum, funcname))
        else:
           raise UnimplementedError
           
           
    def _func_filter_set(self, key, value):
        """
        Function index:value write filter
        
        """
        if callable(value):
            for x in range(len(self.list)):
                y = self.list[x]
                if key(x,y):
                    self.list[x] = value(x,y)
        else:
            for x in range(len(self.list)):
                y = self.list[x]
                if key(x,y):
                    self.list[x] = value
        
        
    def _func_filter_get(self, key):
        """
        Function index:value read filter
        
        """
        t = []
        for x in range(len(self.list)):
            y = self.list[x]
            if key(x,y):
                t.append(self.list[x])
        return t
            
            
    def __len__(self):
        """
        returns the length of the list for len() operation
        """
        return len(self.list)
    
    
    def __repr__(self):
        # prints the list
        return str(self.list)
        

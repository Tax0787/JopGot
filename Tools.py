from os import system as s #system shell
from os import chdir as cd #can use cd
'''
i, p, o, e, v = input, print, open, exec, eval

======================================================================= [ each classes helps ] =============================================================================

E i5 chi1d c1a55 0f "Exception"
Shell3... hmm... see the menual to help()

====================================================================== [ lambda Function helps ] ===========================================================================

clr : c13ar 73rmina1 di5p1ay
child_class : makin9 a chi1d c1a55 4 7yp3 Func7i0n
error : makin9 a c1a55 E 4 3rr0r c1a55

============================================================================================================================================================================

WARNING : this module use the match-case If you'r python Version is Under the 3.9, then USE the tax0787's TaxLib310PlugIn (https://github.com/Tax0787Reborn/TaxLib310PlugIn)
'''
i, p, o, e, v = input, print, open, exec, eval #short-names
clr = lambda : s('clear') #clear display
child_class = lambda name, mom : type(name, (mom,), {}) #type(NAME, TUPLE-__SUPER__(), __DICT__) to make class, type function is meta-class
E = child_class('E',Exception) #make an 'E'rror class
error = lambda name : child_class(name, E) #make error-class by E
class Shell3:
    '''
    Shell3 is third shell apps

    ========= [ class ] ==========

    NoMode = error('NoMode')

    ========== [ TIPS ] ==========

    Show more 2 "help(Shell3.__init__)"
    
    '''
    NoMode = error('NoMode') #Make Error Class
    def __init__(self, QnA_Q = '> ', default = 'py'):
        '''
        making a 5h3113 App 0bj3c7
        QnA_Q : 57rin9 da7a 2 qu357
        defaults : (d3fau175 5h311) k3y w0rd5
        \t3xamp13 7ha7 d3fau15:
        \t\t1) py : py7h0n 5h311
        \t\t2) py-value : py7h0n 5h311 r37urn5 1i57 da7a5 wi7h 3va1-5h311
        \t\t3) os-shell : U'r 05'5 d3fau17 5h311.
        \t\t\tN.B. 7ip 4. 05-5h311 5p3cia1 105ic
        \t\t\t\texit i5 ju57 5h311 3xi7
        \t\t\t\tcd i5 chdir(chan93 dir3c70ry)
        \t\t\t\tcd 5up0r7 "cd..", "cd.", "cd/"(0n1y in 1ik3-Unix or Unix) 1ik3 Wind0w5

        # ===================== [ TIPS ] ============================================================== #
        If U wan7 3xi7 in 5h311 m0d3 "py, py-value", 7ha7 c0mmand is "break" b3cau53 0f 7h3 "while-roop"

        # ============================================================================================= #

        AHAHAHAHAHAHAHA Only Choosen Guys CAN UNDER STAND (Writer is mad bruh ~ lololoolololololol!)
        Tips : Use Chat-GPT (https://chat.openai.com) to help Translate the leet(1337)-style
        '''
        assert isinstance(QnA_Q,str), "QnA_Q must be string data to quest" #KeyWordArgument management, type
        assert isinstance(default,str), "default means default shell key words, see the doc-string to help(Shell3.__init__)" #same
        
        self.__main_shell = default #HIDDEN VALUES
        self.__Q = QnA_Q #same, only minen lol
    def shl(self):
        '''
        5h311 05-5h311 

        SEE THE MENUAL BY help(Shell3.__init__) PLEASE
        
        73rmina1-05-5h311
        '''
        while 1: #Infinity - Roop
            req = i(self.__Q) #Interupt
            if req == 'exit': #like-base-condition to input
                break
            elif req[:3] == 'cd ': #Chdir Losic
                cd(req[3:])
            elif req[:3] == 'cd..': #Win Chdir Losic
                cd('..')
            elif req[:3] == 'cd.': #Win Chdir Losic
                cd('.')
            elif req[:3] == 'cd/': #Like-Win Chdir Losic
                cd('/')
            s(req) #defaultv
    def pys(self):
        '''
        5h311 py

        short and only one-line code... , ...but also add some Quest str~
        
        Py7h0n-3X3C-5h311
        '''
        while 1:e(i(self.__Q))  #Infinity - Roop & { execute | Interupt } --> exectue Interupt value
    def psv(self):
        '''
        5h311 py-va1u3

        d3v by ba53d "self.pys"
        
        Py7h0n-3VA1-5h311
        '''
        ret = []
        while 1:  #Infinity - Roop
            req = i(self.__Q) #Interupt
            if req == 'break': #like-base-condition to input
                break
            ret.append(v(req)) #default, but append
        return ret #return all value
    def __spec__(self):
        '''
        r37urn 5p3c char
        "<BZ3's-Shell3App at ~, can use it to Function and default mode is ~... oh input msg is calso ~, Function at ~>"
        '''
        x, y = id(self), id(self.__call__)
        return f"<BZ3's-Shell3App at {x}, can use it to Function and default mode is {self.__main_shell}... oh input msg is calso {self.__Q}, Function at {y}>"
    def __call__(self, not_main_mode = False):
        '''
        3x3c 7h3 5h311 app 2 [match case]

        WARNING : If you'r python Version is Under the 3.9, then USE the tax0787's TaxLib310PlugIn (https://github.com/Tax0787Reborn/TaxLib310PlugIn)
        '''
        assert not not_main_mode or isinstance(not_main_mode,str), "not-main-mood argv must be bool or str" #KeyWordArgument management, False or True String Data
        if not_main_mode: #mode setting
            mode = not_main_mode #Special case
        else:
            mode = self.__main_shell #default
        match mode: #match command case
            case 'py': #shell py-value
                self.pys()
            case 'py-value': #shell py-value
                return self.psv()
            case 'os-shell': #shell os-shell
                self.shl()
            case _: #Error at the mode, None Mode so raise Error
                raise self.NoMode(f'no mode named {mode}, see the menual the help(Shell3.__init__)')

main = Shell3() #both test and main shell

if __name__ == "__main__": main()

class string_preparer:

    char_to_int_dictionary = {
        '1':10,'2':11,'3':12,'4':13,'5':14,'6':15,'7':16,'8':17,'9':18,'0':19,
        'a':20,'b':21,'c':22,'d':23,'e':24,'f':25,'g':26,'h':27,'i':28,'j':29,
        'k':30,'l':31,'m':32,'n':33,'o':34,'p':35,'q':36,'r':37,'s':38,'t':39,
        'u':40,'v':41,'w':42,'x':43,'y':44,'z':45,'A':46,'B':47,'C':48,'D':49,
        'E':50,'F':51,'G':52,'H':53,'I':54,'J':55,'K':56,'L':57,'M':58,'N':59,
        'O':60,'P':61,'Q':62,'R':63,'S':64,'T':65,'U':66,'V':67,'W':68,'X':69,
        'Y':70,'Z':71,'`':72,'~':73,'!':74,'@':75,'#':76,'$':77,'%':78,'^':79,
        '&':80,'*':81,'(':82,')':83,'-':84,'=':85,'_':86,'+':87,'[':88,']':89,
        '\\':90,';':91,"'":92,',':93,'.':94,'/':95,'{':96,'}':97,'|':98,':':99,
        '"':5,'<':6,'>':7,'?':8,' ':9
    }   #   Keep track of 1, 2, 3, 4, and 5 values in int_to_char as they might cause problems
    
    int_to_char_dictionary = {
        10:'1',11:'2',12:'3',13:'4',14:'5',15:'6',16:'7',17:'8',18:'9',19:'0',
        20:'a',21:'b',22:'c',23:'d',24:'e',25:'f',26:'g',27:'h',28:'i',29:'j',
        30:'k',31:'l',32:'m',33:'n',34:'o',35:'p',36:'q',37:'r',38:'s',39:'t',
        40:'u',41:'v',42:'w',43:'x',44:'y',45:'z',46:'A',47:'B',48:'C',49:'D',
        50:'E',51:'F',52:'G',53:'H',54:'I',55:'J',56:'K',57:'L',58:'M',59:'N',
        60:'O',61:'P',62:'Q',63:'R',64:'S',65:'T',66:'U',67:'V',68:'W',69:'X',
        70:'Y',71:'Z',72:'`',73:'~',74:'!',75:'@',76:'#',77:'$',78:'%',79:'^',
        80:'&',81:'*',82:'(',83:')',84:'-',85:'=',86:'_',87:'+',88:'[',89:']',
        90:'\\',91:';',92:"'",93:',',94:'.',95:'/',96:'{',97:'}',98:'|',99:':',
        5:'"',6:'<',7:'>',8:'?',9:' '
    }

    char_danger_list = ['"', '<', '>', '?', ' ']

    long_string_list = []

    #   Initialize the string_preparer class and update it's internal state to include the list of strings being worked with
    def __init__(self, input_list : list = []):
        self.long_string_list = input_list

    #   Change the internal string list to the new list being worked with
    def change_list(self, input_list : list):
        self.long_string_list = input_list

    #   Loads a list of strings directly from a file into the internal long_string_list
    def load_strings_from_file(self, filename : str):
        new_file = open(filename)
        new_file_contents = new_file.read()
        self.long_string_list = new_file_contents.splitlines()
        print("# # # strings have been read from the file # # #")

    #   Convert the strings in the internal long_string_list to a long list of integers
    def char_to_int(self):
        new_string_list = []
        for string in self.long_string_list:
            new_string = ""
            for char in string:
                if char not in self.char_danger_list:
                    new_string += str(self.char_to_int_dictionary.get(char))
                else:
                    new_string += "0" + str(self.char_to_int_dictionary.get(char))
            new_string_list.append(int(new_string))
        self.long_string_list = new_string_list
        print("# # # characters have been converted to ints # # #")

    #   Converts the integer lists in the internal long_string_list to a long list of strings
    def int_to_char(self):
        new_string_list = []
        for integer in self.long_string_list:
            new_string = ""
            integer = str(integer)
            if len(integer) % 2 == 1:
                integer = "0" + integer
            for index in range(0, len(integer) - 1, 2):
                if integer[index] == "0":
                    new_string += str(self.int_to_char_dictionary.get(int(integer[index + 1])))
                else:
                    new_string += str(self.int_to_char_dictionary.get(int(integer[index:index+2])))
            new_string_list.append(new_string)
        self.long_string_list = new_string_list
        print("# # # integers have been converted into chars # # #")

    #5749031938723424835760026927546025422525208852926037982313899470

    #   Splits the length 64 integers into 8 length 8 integers based solely on location (arbitrary)
    def split_ints(self):
        for i in range(len(self.long_string_list)):
            integer_string = str(self.long_string_list[i])
            if len(integer_string) % 2 == 1:
                integer_string = "0" + integer_string
            eight_part_list = [
                int(integer_string[0:8]),
                int(integer_string[8:16]),
                int(integer_string[16:24]),
                int(integer_string[24:32]),
                int(integer_string[32:40]),
                int(integer_string[40:48]),
                int(integer_string[48:56]),
                int(integer_string[56:64])
            ]
            self.long_string_list[i] = eight_part_list
        print("# # # Integers have been split # # #")

    def combine_ints(self):
        for i in range(len(self.long_string_list)):
            new_string = ""
            for small_int in self.long_string_list[i]:
                small_int_string = str(small_int)
                if len(small_int_string) % 2 == 1:
                    small_int_string = '0' + small_int_string
                new_string += small_int_string
            new_integer = int(new_string)
            self.long_string_list[i] = new_integer
        print("# # # integers have been combined # # #")

    #   Returns the internal list of strings
    def get_string_list(self):
        return self.long_string_list
            
            
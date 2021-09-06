from random import randint, seed

class string_generator:

    character_list = [
        '1','2','3','4','5','6','7','8','9','0',
        'a','b','c','d','e','f','g','h','i','j',
        'k','l','m','n','o','p','q','r','s','t',
        'u','v','w','x','y','z','A','B','C','D',
        'E','F','G','H','I','J','K','L','M','N',
        'O','P','Q','R','S','T','U','V','W','X',
        'Y','Z','`','~','!','@','#','$','%','^',
        '&','*','(',')','-','=','_','+','[',']',
        '\\',';',"'",',','.','/','{','}','|',':',
        '"','<','>','?',' '
    ]

    long_string_list = []
    
    seed = 0

    #   When Initialized the user sets the psuedo random seed for the string_generator to use
    def __init__(self, seed : int = 1):
        self.seed = seed

    #   If the user wants to change the seed of the pseudo-random number generator this function takes care of it
    def change_random_seed(self, seed : int):
        self.seed = seed

    #   This function generates a number of random 32-length strings (default=500,000) which the string_generator then stores as internal variables
    def generate_strings(self, num_strings : int = 500000):
        seed(self.seed)
        for i in range(0 , num_strings):
            print(i)
            new_string = ""
            for j in range(0, 32):
                new_string += self.character_list[randint(0, len(self.character_list) - 1)]
            if new_string in self.long_string_list:
                i -= 1
            else:
                self.long_string_list.append(new_string)
        print("# # # New Set of Strings Generated # # #")

    #   This function exports the internal long_string_list to a text file of parameter name
    def export_to_file(self, file_name : str):
        new_file = open(file_name + ".txt", "w")
        long_string_string = ""
        for string in self.long_string_list:
            long_string_string += string + '\n'
        new_file.write(long_string_string)
        new_file.close()
        print("# # # Strings have been exported to " + file_name + ".txt # # #")

    #   This function resets the internal state of the string_generator to prevent possible clutter from running generate_strings multiple times
    def reset_internal_state(self):
        self.long_string_list = []
        self.seed = 1
        print("# # # Internal state has been reset # # #")
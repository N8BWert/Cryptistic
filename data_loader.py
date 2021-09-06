import numpy
import string_preparer

class data_loader():

    plaintext_strings = []

    encryptedtext_strings = []

    dataset = None

    def __init__(self, plaintext_string_preparer : string_preparer, encryptedtext_string_preparer : string_preparer):
        try:
            self.plaintext_strings = plaintext_string_preparer.get_string_list()
        except:
            self.plaintext_strings = None
        try:
            self.encryptedtext_strings = encryptedtext_string_preparer.get_string_list()
        except:
            self.encryptedtext_strings = None

    #   Updates the internal plaintext_strings and encryptedtext_strings based on the inputted string_preparers
    def update_internal_strings(self, plaintext_string_preparer : string_preparer, encryptedtext_string_preparer : string_preparer):
        self.plaintext_strings = plaintext_string_preparer.get_string_list()
        self.encryptedtext_strings = encryptedtext_string_preparer.get_string_list()

    #   Creates the file that will be used as a dataset when load_dataset is called
    def create_dataset(self, filename : str):
        dataset_string = ""
        for i in range(len(self.plaintext_strings)):
            for small_int in self.plaintext_strings[i]:
                dataset_string += str(small_int) + ','
            for tiny_int in self.encryptedtext_strings[i]:
                dataset_string += str(tiny_int) + ','
            dataset_string = dataset_string[0:len(dataset_string)-1]
            dataset_string += '\n'
            if i% 10 == 0:
                print(i)
        dataset_file = open(filename + ".txt", 'w')
        dataset_file.write(dataset_string)
        print("# # # Dataset has been created as a txt file # # #")

    #   Loads the dataset that was created with create_dataset, which is then returned as X and Y
    def load_dataset_to_variables(self, filename : str):
        self.dataset = numpy.loadtxt(filename + '.txt', delimiter = ',')
        X = self.dataset[:,0:8]
        Y = self.dataset[:,8:16]
        print("# # # Training dataset has been loaded into the internal state # # #")
        print("# # # The X and Y dataset are now being returned # # #")
        return X, Y
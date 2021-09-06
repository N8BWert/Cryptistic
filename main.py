import string_generator
import string_preparer
import data_loader
from keras.models import Sequential
from keras.layers import Dense, LeakyReLU
from keras.callbacks import ModelCheckpoint
import os

if __name__ == '__main__':
    loader = data_loader.data_loader(None, None)

    X, Y = loader.load_dataset_to_variables("dataset")

    model = Sequential()
    model.add(Dense(300, input_dim = 8, kernel_initializer = 'he_uniform', activation = LeakyReLU(alpha = 0.01)))
    model.add(Dense(300, kernel_initializer = 'he_uniform', activation = LeakyReLU(alpha = 0.01)))
    model.add(Dense(300, kernel_initializer = 'he_uniform', activation = LeakyReLU(alpha = 0.01)))
    model.add(Dense(8, kernel_initializer = 'he_uniform', activation = LeakyReLU(alpha = 0.01)))

    del(loader)

    model.load_weights("weights.best.hdf5")

    model_json = model.to_json()
    with open("model.json", "w") as json_file:
        json_file.write(model_json)

    #   Experiment with CategoricalCrossentropy, SparseCategoricalCrossentropy, Poisson, and KLDivergence loss functions
    #model.compile(loss = 'mae', optimizer = 'Nadam', metrics = ['accuracy'])

    #filepath = "weights.best.hdf5"
    #checkpoint = ModelCheckpoint(filepath, monitor = 'accuracy', verbose = 1, save_best_only = True, mode = 'max')
    #callbacks = [checkpoint]

    #model.fit(X, Y, epochs = 5000, use_multiprocessing = True, workers = 100, batch_size = 1000, callbacks=callbacks)

    #_, accuracy = model.evaluate(X, Y)
    #print('Accuracy: %.2f' % (accuracy * 100))
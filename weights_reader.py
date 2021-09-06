import h5py
f = h5py.File("weights.best.hdf5", "r")

biases_0_1 = list(f.get('model_weights').get('dense').get('dense').get('bias:0'))
kernels_0_1 = list(f.get('model_weights').get('dense').get('dense').get('kernel:0'))

biases_1_2 = list(f.get('model_weights').get('dense_1').get('dense_1').get('bias:0'))
kernels_1_2 = list(f.get('model_weights').get('dense_1').get('dense_1').get('kernel:0'))

biases_2_3 = list(f.get('model_weights').get('dense_2').get('dense_2').get('bias:0'))
kernels_2_3 = list(f.get('model_weights').get('dense_2').get('dense_2').get('kernel:0'))

biases_3_f = list(f.get('model_weights').get('dense_3').get('dense_3').get('bias:0'))
kernels_3_f = list(f.get('model_weights').get('dense_3').get('dense_3').get('kernel:0'))

def num_negpos_biases(bias_values_list : list):
    num_negs, num_pos, num_zeroes = 0, 0, 0
    for bias_value in bias_values_list:
        if bias_value < 0:
            num_negs += 1
        elif bias_value > 0:
            num_pos += 1
        else:
            num_zeroes += 1
    return(num_negs, num_pos, num_zeroes)

def num_negpos_kernels(kernel_values_list : list):
    num_negs, num_pos, num_zeroes = 0, 0, 0
    for weight_values in kernel_values_list:
        for weight in weight_values:
            if weight < 0:
                num_negs += 1
            elif weight > 0:
                num_pos += 1
            else:
                num_zeroes += 1
    return(num_negs, num_pos, num_zeroes)

def num_danger_list(minimum_number, maximum_number, weight_list_list):
    num_less = 0
    for weight_list in weight_list_list:
        for weight_values in weight_list:
            for weight in weight_values:
                if weight > minimum_number and weight < maximum_number:
                    num_less += 1
                    print(weight)
    return(num_less)

if __name__ == '__main__':
    bias_neg_0_1, bias_pos_0_1, bias_zeroes_0_1 = num_negpos_biases(biases_0_1)
    kernel_neg_0_1, kernel_pos_0_1, kernel_zeroes_0_1 = num_negpos_kernels(kernels_0_1)
    print(bias_neg_0_1, bias_pos_0_1, bias_zeroes_0_1)
    print(kernel_neg_0_1, kernel_pos_0_1, kernel_zeroes_0_1)
    bias_neg_1_2, bias_pos_1_2, bias_zeroes_1_2 = num_negpos_biases(biases_1_2)
    kernel_neg_1_2, kernel_pos_1_2, kernel_zeroes_1_2 = num_negpos_kernels(kernels_1_2)
    print(bias_neg_1_2, bias_pos_1_2, bias_zeroes_1_2)
    print(kernel_neg_1_2, kernel_pos_1_2, kernel_zeroes_1_2)
    bias_neg_2_3, bias_pos_2_3, bias_zeroes_2_3 = num_negpos_biases(biases_2_3)
    kernel_neg_2_3, kernel_pos_2_3, kernel_zeroes_2_3 = num_negpos_kernels(kernels_2_3)
    print(bias_neg_2_3, bias_pos_2_3, bias_zeroes_2_3)
    print(kernel_neg_2_3, kernel_pos_2_3, kernel_zeroes_2_3)
    bias_neg_3_f, bias_pos_3_f, bias_zeroes_3_f = num_negpos_biases(biases_3_f)
    kernel_neg_3_f, kernel_pos_3_f, kernel_zeroes_3_f = num_negpos_kernels(kernels_3_f)
    print(bias_neg_3_f, bias_pos_3_f, bias_zeroes_3_f)
    print(kernel_neg_3_f, kernel_pos_3_f, kernel_zeroes_3_f)
    print(bias_neg_0_1 + bias_pos_0_1)
    print(bias_neg_1_2 + bias_pos_1_2)
    print(bias_neg_2_3 + bias_pos_2_3)
    print(bias_neg_3_f + bias_pos_3_f)
    print(kernel_neg_0_1 + kernel_pos_0_1)
    print(kernel_neg_1_2 + kernel_pos_1_2)
    print(kernel_neg_2_3 + kernel_pos_2_3)
    print(kernel_neg_3_f + kernel_pos_3_f)
    weight_list_list = [kernels_0_1, kernels_1_2, kernels_2_3, kernels_3_f]
    minimum_number = -1/10101
    maximum_number = -1/99999999
    danger_items = num_danger_list(minimum_number, maximum_number, weight_list_list)
    print(danger_items)
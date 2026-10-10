#!/usr/bin/env python3
"""Print classification results and optional misclassification details."""


def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """Print summary statistics and requested classification errors."""
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format(
        'N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    print("\nPercentage Statistics:")
    for key, value in results_stats_dic.items():
        if key.startswith('pct'):
            print("{:20}: {:5.1f}".format(key, value))

    if (print_incorrect_dogs and
            results_stats_dic['n_correct_dogs'] +
            results_stats_dic['n_correct_notdogs'] !=
            results_stats_dic['n_images']):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for result in results_dic.values():
            if sum(result[3:]) == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    result[0], result[1]))

    if (print_incorrect_breed and
            results_stats_dic['n_correct_dogs'] !=
            results_stats_dic['n_correct_breed']):
        print("\nINCORRECT Dog Breed Assignment:")
        for result in results_dic.values():
            if sum(result[3:]) == 2 and result[2] == 0:
                print("Real: {:>26}   Classifier: {:>30}".format(
                    result[0], result[1]))

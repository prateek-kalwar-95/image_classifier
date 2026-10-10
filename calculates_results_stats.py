#!/usr/bin/env python3
"""Calculate summary statistics for image-classification results."""


def calculates_results_stats(results_dic):
    """Return counts and percentages calculated from the results dictionary."""
    results_stats_dic = {
        'n_images': len(results_dic),
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_notdogs': 0,
        'n_correct_breed': 0
    }

    for result in results_dic.values():
        if result[2] == 1:
            results_stats_dic['n_match'] += 1

        if result[3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            if result[4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            if result[2] == 1:
                results_stats_dic['n_correct_breed'] += 1
        elif result[4] == 0:
            results_stats_dic['n_correct_notdogs'] += 1

    results_stats_dic['n_notdogs_img'] = (
        results_stats_dic['n_images'] - results_stats_dic['n_dogs_img']
    )

    n_images = results_stats_dic['n_images']
    n_dogs = results_stats_dic['n_dogs_img']
    n_notdogs = results_stats_dic['n_notdogs_img']
    results_stats_dic['pct_match'] = (
        results_stats_dic['n_match'] / n_images * 100.0 if n_images else 0.0
    )
    results_stats_dic['pct_correct_dogs'] = (
        results_stats_dic['n_correct_dogs'] / n_dogs * 100.0 if n_dogs else 0.0
    )
    results_stats_dic['pct_correct_breed'] = (
        results_stats_dic['n_correct_breed'] / n_dogs * 100.0 if n_dogs else 0.0
    )
    results_stats_dic['pct_correct_notdogs'] = (
        results_stats_dic['n_correct_notdogs'] / n_notdogs * 100.0
        if n_notdogs else 0.0
    )

    return results_stats_dic

"""
This module provides a function for calculating the Word Error Rate (WER) between a reference text and a hypothesis 
text. The WER is calculated as the number of edits (insertions, deletions, and substitutions) needed to transform 
the hypothesis text into the reference text, divided by the number of words in the reference text.

This module defines the following function:
    - wer(reference, hypothesis): Calculate the WER between a reference text and a hypothesis text.
"""

import numpy as np
from .errorhandler import error_handler


def wer(reference, hypothesis) -> float:
    """
    This function will calculate the overall Word Error Rate for the entire reference and hypothesis texts.

    Parameters
    ----------
    reference : str, list or numpy array
        The ground truth transcription of a recorded speech or the expected output of a live speech.
    hypothesis : str, list or numpy array
        The text generated by a speech-to-text algorithm/system which will be compared to the reference text.

    Raises
    ------
    ValueError
        if the two input parameters do not contain the same amount of elements.
    AttributeError
        if input text is not a string, list or np.ndarray data type.

    Returns
    -------
    np.float64
        This function will return a single Word Error Rate, which is calculated as the number of edits (insertions,
        deletions and substitutions) divided by the number of words in the reference text.

    Examples
    --------
    >>> wer_example_1 = wer('i love cold pizza', 'i love pizza')
    >>> print(wer_example_1)
    0.25

    >>> ref = ['i love cold pizza','the sugar bear character was popular']
    >>> hyp = ['i love pizza','the sugar bare character was popular']
    >>> wer_example_2 = wer(ref, hyp)
    >>> print(wer_example_2)
    0.2
    """
    try:
        word_error_rate_breakdown = error_handler(reference, hypothesis)
    except (ValueError, AttributeError) as err:
        print(f"{type(err).__name__}: {str(err)}")
        return None
    if isinstance(word_error_rate_breakdown[0], np.ndarray):
        transform_word_error_rate_breakdown = np.transpose(
            word_error_rate_breakdown.tolist()
        )
        total_words = np.sum(transform_word_error_rate_breakdown[2])
        wer_result = np.sum(transform_word_error_rate_breakdown[1]) / max(
            total_words, 1
        )
    else:
        wer_result = word_error_rate_breakdown[0]
    return wer_result

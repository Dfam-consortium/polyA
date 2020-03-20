from polyA import (
    CharacterPositions,
    SubstitutionMatrix,
    calculate_score,
    fill_align_score_matrix,
)
from pytest import mark


char_positions: CharacterPositions = {
    "A": 0,
    "M": 7,
    "H": 11,
    "V": 12,
    "N": 10,
    "Y": 4,
    "S": 8,
    "T": 5,
    "C": 3,
    "R": 1,
    "X": 13,
    "K": 6,
    "W": 9,
    "G": 2,
}

sub_matrix: SubstitutionMatrix = [
    8,
    1,
    -6,
    -13,
    -14,
    -15,
    -11,
    -2,
    -10,
    -3,
    -1,
    -1,
    -1,
    -27,
    2,
    2,
    1,
    -13,
    -13,
    -14,
    -6,
    -5,
    -5,
    -5,
    -1,
    -1,
    -1,
    -27,
    -2,
    3,
    10,
    -13,
    -13,
    -13,
    -1,
    -8,
    -1,
    -8,
    -1,
    -1,
    -1,
    -27,
    -13,
    -13,
    -13,
    10,
    3,
    -2,
    -8,
    -1,
    -1,
    -8,
    -1,
    -1,
    -1,
    -27,
    -14,
    -13,
    -13,
    1,
    2,
    2,
    -5,
    -6,
    -5,
    -5,
    -1,
    -1,
    -1,
    -27,
    -15,
    -14,
    -13,
    -6,
    1,
    8,
    -2,
    -11,
    -10,
    -3,
    -1,
    -1,
    -1,
    -27,
    -9,
    -5,
    -1,
    -9,
    -6,
    -2,
    -1,
    -9,
    -5,
    -5,
    -1,
    -1,
    -1,
    -27,
    -2,
    -6,
    -9,
    -1,
    -5,
    -9,
    -9,
    -1,
    -5,
    -5,
    -1,
    -1,
    -1,
    -27,
    -8,
    -4,
    -1,
    -1,
    -4,
    -8,
    -4,
    -4,
    -1,
    -8,
    -1,
    -1,
    -1,
    -27,
    -3,
    -6,
    -10,
    -10,
    -6,
    -3,
    -6,
    -6,
    -10,
    -3,
    -1,
    -1,
    -1,
    -27,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -27,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -27,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -1,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -27,
    -1,
    -1,
    -27,
]


# GCCTTGCGAGGTGGGTCACGNCANNTGTAATCCCACTAATTTGGCCGGCCGAGGGTGGC
# GCCGGGCGCGGTGGCTCGCGCC---TGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGC
# G
# G


def test_calculate_score():

    seq1 = "GCCTTGCGAGGTGGGTCACGNCANNTGTAATCCCACTAATTTGGCCGGCCGAGGGTGGC"
    prev1 = "G"
    seq2 = "GCCGGGCGCGGTGGCTCGCGCC---TGTAATCCCAGCACTTTGGGAGGCCGAGGCGGGC"
    prev2 = "G"
    score = calculate_score(
        seq1, seq2, prev1, prev2, char_positions, sub_matrix
    )
    assert score == 0


def test_fill_align_score_matrix():
    # TODO: We need to use a fixture for this to avoid complicating the test
    pass

import unittest

from code import revcomp, get_codons, codon_to_amino, get_prots

class TestRevComp(unittest.TestCase):
    def test__empty_string(self):
        self.assertEqual("", revcomp(""))
    def test_one_char(self):
        self.assertEqual("T", revcomp("A"), "failed to convert A")
        self.assertEqual("A", revcomp("T"), "failed to convert T")
        self.assertEqual("G", revcomp("C"), "failed to convert C5")
        self.assertEqual("C", revcomp("G"), "failed to convert G")
    def test_general_case(self):
        self.assertEqual("TACGGTAT", revcomp("ATACCGTA"))

class TestOtherFunctions(unittest.TestCase):
    def test_get_codons(self):
        tests = [
                dict(
                    dna = '',
                    expected = [],
                    comment = "empty string"),
                dict(
                    dna = 'AAGGTCTTTCCGCCATCC',
                    expected = 'AAG GTC TTT CCG CCA TCC'.split(),
                    comment = "multiple of three"),
                dict(
                    dna = 'AAGGTCTTTCCGCCATCCCC',
                    expected = 'AAG GTC TTT CCG CCA TCC'.split(),
                    comment = "not multiple of three"),
                ]

        for test in tests:
            dna = test['dna']
            expected = test['expected']
            comment = test['comment']
            self.assertEqual(get_codons(dna), expected, comment)

    def test_codon_to_amino(self):
        tests = [
                [[], '', 'empty string'],
                ['ATA CAA'.split(), 'IQ'],
                ['ATA CAC CAA'.split(), 'IHQ'],
                ]
        for codons, amino, *comment in tests:
            self.assertEqual(codon_to_amino(codons), amino, *comment)

    def test_get_prots(self):
        amino = "FD_MJKFDBJMDFLKFD_SKGMKLJDSLK_LJGFMDSK_LG_FDM_KLMYYY"
        prots =    "MJKFDBJMDFLKFD_   MKLJDSLK_    MDSK_     M_".split()
        self.assertEqual(get_prots(amino), prots)
        
if __name__ == '__main__':
    unittest.main()


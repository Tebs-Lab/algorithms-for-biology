import unittest
import sys
import os

# Trick to avoid adding this module to the path forever or via the shell. 
dirname = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
sys.path.append(dirname)

from exercises.classify_functions_code import reverse_compliment, count_occurance
from solutions.optimize_functions_code import unique_kmers as optimized_unique_kmers, count_kmers as optimized_count_kmers
from solutions.find_kmer_clumps_code import clumping_kmers

'''
These tests are not exhaustive/comprehensive, just be aware of that.
'''

class TestGenomeFunctions(unittest.TestCase):

    def test_reverse_compliment(self):
        '''
        This function takes a string representing a dna sequence 
        as input, and returns its reverse complement.
        '''
        cases = [
            ('', ''),
            ('A', 'T'),
            ('T', 'A'),
            ('C', 'G'),
            ('G', 'C'),
            ('ATCG', 'CGAT')
        ]

        for sequence, expected_result in cases:
            result = reverse_compliment(sequence)
            failure_message = f'Failed on input sequence: {sequence}, expected result: {expected_result}, actual_result: {result}'
            self.assertEqual(result, expected_result, failure_message) 


    def test_count_occurance(self):
        '''
        This function accepts two strings, one representing the genome
        of an organism (or a part of the genome) and another representing
        some smaller DNA/RNA pattern. It returns the number of times this
        pattern occurs within the provided genome.
        '''
        cases = [
            ('G', 'G', 1),
            ('AAA', 'A', 3),
            ('AAA', 'AA', 2),
            ('TAGTAGTAG', 'TAG', 3),
            ('AATAATAT', 'AT', 3),
            ('ATCGATCG', 'ATCG', 2),
        ]
        
        for genome, pattern, expected_result in cases:
            result = count_occurance(genome, pattern)
            failure_message = f'Failed on input genome: {genome}, pattern: {pattern}, expected result: {expected_result}, actual_result: {result}'
            self.assertEqual(result, expected_result, failure_message)

    def test_unique_kmers(self):
        '''
        This function takes in a string representing the genome of an
        organism (or section of a genome) and an integer value k. It 
        returns a list of all the unique substrings of length k
        (often called k-mers) contained in that genome.

        But the runtime is simply O(GK), and is completely independent of 
        the value U (the number of unique k-mers)
        '''
        pass
        # genome, k


    def test_count_kmers(self):
        '''
        This function accepts a string representing a genome
        and an integer k. It returns a dictionary which maps
        each occurring k-mer to the number of times that k-mer
        occurs within the genome.

        Instead of finding the unique k-mers and then counting them
        one by one, we just look at the genome once and keep a running
        count of ALL the k-mers at the same time!

        Note that it is almost identical to the above function!
        '''
        pass
        # genome, k
    

    def test_clumping_kmers(self):
        '''
        This function finds clusters of k-mers in a genome.

        * Accepts as input:
            * `genome` — a string representing the genome of an organism.
            * `kmer_length` - an integer representing the length of the k-mers to be considered for clumping.
            * `window_size` — an integer representing the size of the "region of interest".
            * `min_kmer_count` – an integer representing the minimum number of duplicate k-mers found within `window_size` of each other to be considered a cluster.
        
        * Returns as output:
            * A dictionary mapping all the k-mers that satisfy the clustering criteria to a list of all the start locations within `genome` for those clusters.
            * Each position in the list should be a start location of the k-mer satisfying the clustering criteria.
                * For example, consider the genome `'ATATGATGATAT'` the 3-mer `'ATG'` a `window_length` of 10, and a `min_kmer_count`of 2.
                * In reality, we could map this window to all the positions `[0, 1, 2]` — but all of these positions contain the SAME cluster, and the most relevant of those positions is `2` because it is the start of the first copy of our k-mer `'ATG'`. 
                    * Including positions 0 and 1 in our solution would be both redundant and less useful in subsequent analysis. 
        '''
        pass
        # genome, kmer_length, window_length, min_kmer_count


if __name__ == "__main__":
    unittest.main()
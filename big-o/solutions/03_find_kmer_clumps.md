# Finding K-mer Clusters Solution

This code solves the problem as described in the exercise writeup:

```python
def clumping_kmers(genome, kmer_length, window_length, min_kmer_count):
    # Collect all the unique kmers and where they occur
    kmers = {}
    for start_position in range(len(genome) - kmer_length + 1):
        kmer = genome[start_position:start_position+kmer_length]
        if kmer not in kmers:
            kmers[kmer] = []
        
        kmers[kmer].append(start_position)

    # For each kmer and it's locations determine if they meet
    # the min-count within the window length.
    candidate_kmers = {}
    for kmer, locations in kmers.items():
        if len(locations) < min_kmer_count:
            continue

        cluster_window_start_points = []
        
        start_pos = 0
        start_val = locations[start_pos]
        for end_pos in range(0, len(locations)):
            end_val = locations[end_pos]

            # advance the start position until it's
            # within window_length of the end pos
            while (end_val + kmer_length) - start_val >= window_length:
                start_pos += 1
                start_val = locations[start_pos]

            # if there are at least min_kmer_count in this window
            # it's a candidate
            if (end_pos - start_pos) + 1 > min_kmer_count:
                cluster_window_start_points.append(start_val) 

        # If we found at least one window for this kmer, add them.
        if len(cluster_window_start_points) > 0:
            candidate_kmers[kmer] = cluster_window_start_points
    
    return candidate_kmers
```

The Big O for this program is O(GK). The initial section of the code which finds all the k-mer start locations dominates the runtime, although the second section has more code it is similarly bounded by O(GK) since it can only every execute once per k-mer location in the Genome (that is, the size of `kmers` will be at maximum G*K) and each location is considered once in that section of code. 

Some useful debugging test cases can be found here: [http://bioinformaticsalgorithms.com/data/debugdatasets/replication/ClumpFindingProblem.pdf](http://bioinformaticsalgorithms.com/data/debugdatasets/replication/ClumpFindingProblem.pdf)
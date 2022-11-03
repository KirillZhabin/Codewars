def crossover(chromosome1, chromosome2, index):
    chr1 = chromosome1[:index] + chromosome2[index:]
    chr2 = chromosome2[:index] + chromosome1[index:]
    return [chr1, chr2]
class StrandsDNA:
    def __init__(self):
        self.all_strands = []

    def add_strands(self, strands):
        '''
        Adds new strands to list of strands (to attribute 'all_strands').
        '''
        self.all_strands.append(strands)
    
    def get_max_strands(self):
        '''
        Returns strands with max length.
        '''
        strand_length = 0
        max_strands = []

        for element in self.all_strands:
            if len(element) >= strand_length:
                strand_length = len(element)

        for item in self.all_strands:
            if item not in max_strands:
                if len(item) == strand_length:
                    max_strands.append(item)

        dna_list = sorted(max_strands)

        result = ''
        for dna in dna_list:
            result += dna + ' '
        
        return result

dna = StrandsDNA()

dna.add_strands('AAB')
dna.add_strands('AGGHE')
dna.add_strands('AB')
dna.add_strands('AMMMN')
dna.add_strands('AANNN')
dna.add_strands('AGGHE')
dna.add_strands('ACDE')

print(dna.get_max_strands())

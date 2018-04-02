moniamond = [[2,2,2]]

diamond = [[1,2,1,2]]

triamond = [[0,2,1,1,2], [1,1,2,0,2], [1,2,0,2,1], [0,2,1,1,2]]

tetriamond = [[-1,2,1,1,1,2], [0,1,2,0,1,2], [0,2,0,2,0,2], [0,2,1,0,2,1], [-1,2,1,1,1,2]]

expected_maxima = (1..8).to_a.map { |k| (5**k - 1) / 2 }

def pseudo_horner(seq)
  seq.reduce(0) { |value, t| 5*value + t} #unique integer representation in 5-nary
end

def reversible_pseudo_horner(seq)
  [pseudo_horner(seq),pseudo_horner(seq.reverse)].min
end

def canonical_index(seq)
  result = seq.length.times.to_a.map do |index|
    reversible_pseudo_horner(seq.rotate(index))
  end.min
  return (result)
end

def next_index(index,seq)
  (index + 1) % seq.length
end

def cyclic_grow(seq, results_so_far)
  result = []
  seq.each_with_index do |value, index|
    my_next = next_index(index, seq)
    my_after_next = next_index(index + 1, seq)
    next_value = seq[my_next]

    if value != -2
      new_seq = seq.dup
      if next_value != -2
        new_seq[index] -= 1
        new_seq[my_next] -= 1
        new_seq.insert(my_next,2)
      else
        new_seq[index] -= 1
        new_seq[my_after_next] -= 1
        new_seq.delete_at(my_next)
      end
      if results_so_far.add?(canonical_index(new_seq))
        result.push(new_seq)
      end
    end
  end
  result
end

def grow_all(collection, set)
  collection.map {|sequence| cyclic_grow(sequence, set)}.flatten(1)
end

tetriamond.map {|k| canonical_index(k)}.display
puts

# tetriamond[0].display
# puts
# puts
# test_seq1 = [1,1,1,2,-2,2,1]
# test_seq1.display
# puts
# cyclic_grow(test_seq1).display
# puts
# puts
# puts
# test_seq2 = [-2,2,1,1,1,1,2]
# test_seq2.display
# puts
# cyclic_grow(test_seq2).display
# puts
# puts
# puts
# test_seq3 = [2,1,1,1,1,2,-2]
# test_seq3.display
# puts
# cyclic_grow(test_seq3).display
# puts
# puts
# puts
# test_seq4 = [0,2,-2]
# test_seq4.display
# puts
# cyclic_grow(test_seq4).display
# puts
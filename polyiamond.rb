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
      if next_value == -2
        new_seq[index] -= 1
        new_seq[my_after_next] -= 1
        new_seq.delete_at(my_next)
      else
        new_seq[index] -= 1
        new_seq[my_next] -= 1
        new_seq.insert(my_next,2)
      end
      if results_so_far.add?(canonical_index(new_seq))
        result.push(new_seq)
      end
    end
  end
  result
end

def concave_grow(seq, results_so_far)
  result = []
  seq.each_with_index do |value, index|
    current_seq = seq.rotate(index)
    if current_seq[0] > 0
      result.push current_seq
    end
  end
  puts result.display
  output = result.map do |value|
    new_value = []
    flag = false
    if value[1] === 0
      new_value += [value.shift - 1, 1]
      value.shift
    else
      new_value += [value.shift - 1, 2]
    end
    while value[0] === 0
      flag = true
      new_value.push 0
      value.shift
    end
    new_value += flag ? [1, value.shift - 1] : [value.shift - 1]
    new_value += value
    new_value
  end
  output
end


def grow_all(collection, set)
  collection.map {|sequence| cyclic_grow(sequence, set)}.flatten(1).sort_by do |seq|
    canonical_index(seq)
  end
end

concave_grow([2,1,0,1,2,0,0], []).display
puts
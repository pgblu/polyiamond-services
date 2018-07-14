require_relative 'polyiamond'
require 'set'

MONIAMONDS = [[2,2,2]]
polyiamond_set = Set.new([MONIAMONDS])
puts "number of moniamonds: #{MONIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"

DIAMONDS = grow_all(MONIAMONDS, polyiamond_set)
puts "number of diamonds: #{DIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"

TRIAMONDS = grow_all(DIAMONDS, polyiamond_set)
puts "number of triamonds: #{TRIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"
TETRIAMONDS = grow_all(TRIAMONDS, polyiamond_set)
puts "number of tetriamonds: #{TETRIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"
PENTIAMONDS = grow_all(TETRIAMONDS, polyiamond_set)
puts "number of pentiamonds: #{PENTIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"
HEXIAMONDS = grow_all(PENTIAMONDS, polyiamond_set)
puts "number of hexiamonds: #{HEXIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"
HEPTIAMONDS = grow_all(HEXIAMONDS, polyiamond_set)
puts "number of heptiamonds: #{HEPTIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"
OCTIAMONDS = grow_all(HEPTIAMONDS, polyiamond_set)
puts "number of octiamonds: #{OCTIAMONDS.count}\npolyiamond_set: #{polyiamond_set.count}"

puts
puts
[TRIAMONDS, TETRIAMONDS, PENTIAMONDS, HEXIAMONDS, HEPTIAMONDS, OCTIAMONDS].each do |collection|
  collection.display
  puts
end

MY_OCTIAMONDS = []
puts;puts
PENTIAMONDS.each_with_index do |shape, idx|

  puts idx + 1
  MY_OCTIAMONDS[idx] = grow_all(grow_all(cyclic_grow(shape, Set.new()), Set.new()), Set.new())
  puts "Octiamonds grown from #{shape}: "
  MY_OCTIAMONDS[idx].display
  puts
  puts "There are a total of #{MY_OCTIAMONDS[idx].count} octiamonds grown from this pentiamond"
  puts
  puts
end

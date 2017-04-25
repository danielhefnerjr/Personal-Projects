#!/bin/ruby

n = gets.strip.to_i
clouds = gets.strip.split(' ').map(&:to_i)

$jumps = Hash.new(Float::INFINITY)
def num_jumps(clouds,i)
    if i >= clouds.length-1
        return 0
    end
    
    if clouds[i] == 1
        return Float::INFINITY
    end
    
    if $jumps[i] == Float::INFINITY
        $jumps[i] = [num_jumps(clouds,i+1),num_jumps(clouds,i+2)].min + 1
    end
    return $jumps[i]
end

puts num_jumps(clouds,0)
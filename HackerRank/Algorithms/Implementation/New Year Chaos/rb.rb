#!/bin/ruby

T = gets.strip.to_i
for a0 in (0..T-1)
    n = gets.strip.to_i
    q = gets.strip
    q = q.split(' ').map(&:to_i)
    # your code goes here
    
    too = false
    for i in 0..q.length-1
        s = q[i]
        if s-1-i > 2
            puts 'Too chaotic'
            too = true
            break
        end
    end
    
    if !too
        total_swaps = 0
        curr_swapped = true
        while curr_swapped
            curr_swapped = false
            for i in (0..q.length-2).reverse_each
                 if q[i] > q[i+1]
                     q[i],q[i+1] = q[i+1],q[i]
                     total_swaps += 1
                     curr_swapped = true
                 end
            end
        end
        
        puts total_swaps
    end
end

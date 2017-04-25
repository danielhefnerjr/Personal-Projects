#!/bin/ruby

def try_permutation(a,i,k)
    #if i == a.length-1
    #    return a
    #end
    
    while i < a.length && a[i] != i+1
        i += 1
    end
    
    if i == a.length
        return a
    else
    # try left
    #if a[i] == i+1
        if (i-k) >= 0 && a[(i-k)] == (i-k)+1
            a[i], a[(i-k)] = a[(i-k)],a[i]
            p = try_permutation(a,i+1,k)
            if p
                return p
            else
                a[i], a[(i-k)] = a[(i-k)],a[i]
            end
        end

        # try right
        if (i+k) < a.length && a[(i+k)] == (i+k)+1
            a[i], a[(i+k)] = a[(i+k)],a[i]
            p = try_permutation(a, i+1,k)
            return p if p
        end
    end
    
    return nil
end

t = gets.strip.to_i
for a0 in (0..t-1)
    n,k = gets.strip.split(' ')
    n = n.to_i
    k = k.to_i
    
    #p = try_permutation((1..n).to_a,0,k)
    na = false
    a = (1..n).to_a
    if k == 0
        puts a.join(' ')
        next
    end
    a.each_index { |i|
        next if a[i] != i+1
        
        if i+k < a.length && a[i+k] == i+k+1
            a[i],a[i+k] = a[i+k],a[i]
        else
            na = true
            break
        end
    }
    
    if ! na
        puts a.join(' ')
    else
        puts -1
    end
end

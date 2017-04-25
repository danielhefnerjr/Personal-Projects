#!/bin/ruby

t = gets.strip.to_i
for a0 in (0..t-1)
    R,C = gets.strip.split(' ')
    R = R.to_i
    C = C.to_i
    G = Array.new(R)
    for g_i in (0..R-1)
        G[g_i] = gets.strip
    end
    r,c = gets.strip.split(' ')
    r = r.to_i
    c = c.to_i
    P = Array.new(r)
    for p_i in (0..r-1)
        P[p_i] = gets.strip
    end
    
    match = false
    for g_i in (0..R-1)
       for g_j in (0..C-1)
           if G[g_i][g_j] == P[0][0]
               match = true
               for p_i in (0..r-1)
                   for p_j in (0..c-1)
                       if G[g_i+p_i][g_j+p_j] != P[p_i][p_j]
                           match = false
                           break
                       end
                   end
                   if match == false
                       break
                   end
               end
               if match
                   break
               end
           end
       end
        if match
            break
        end
    end
    
    if match
        puts 'YES'
    else
        puts 'NO'
    end
end

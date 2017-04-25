#!/usr/bin/ruby
def  insertionSort(ar) 
    i = 1
    while i < ar.length
        if ar[i] < ar[i-1]
            j = i-1
            e = ar[i]
            while j >= 0 && ar[j] > e
                ar[j+1] = ar[j]
                j -= 1             
            end
            ar[j+1] = e
        end
        puts ar.join(' ')
        i += 1 
    end
end
cnt = gets.to_i
ar = gets.strip.split(" ").map! {|i| i.to_i}
insertionSort(ar)

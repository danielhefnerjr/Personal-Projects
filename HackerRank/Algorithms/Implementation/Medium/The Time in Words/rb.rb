#!/bin/ruby

h = gets.strip.to_i
m = gets.strip.to_i

ones = ['one','two','three','four','five','six','seven','eight','nine']
teens = ['eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
hour = ''
next_hour = ''
if h < 10
    hour = ones[h-1]
    next_hour = h == 9 ? 'ten' : ones[h]
elsif h == 10
    hour = 'ten'
    next_hour = 'eleven'
else
    hour = h == 11 ? 'eleven' : 'twelve'
    next_hour = h == 11 ? 'twelve' : 'one'
    
end

s = ''
if m == 15 || m == 30 || m == 45
    if m == 15
        s = 'quarter past ' + hour
    elsif m == 30
        s = 'half past ' + hour
    else
        s = 'quarter to ' + next_hour
    end
else
    if m == 0
        s = hour + ' o\' clock'    
    elsif m < 30
        if m > 20
            s << 'twenty ' + ones[(m % 10)-1] + ' minutes'
        elsif m > 10
            s << teens[m-11] + ' minutes'
        elsif m == 10
            s << 'ten minutes'
        else
            s << ones[m-1]
        end
        s << ' past ' + hour
    else
        m = 60 - m
        if m > 20
            s << 'twenty ' + ones[(m % 10)-1] + ' minutes'
        elsif m > 10
            s << teens[m-11] + ' minutes'
        elsif m == 10
            s << 'ten minutes'
        else
            s << ones[m-1] + ' minutes'
        end
        s << ' to ' + next_hour
    end
end

puts s
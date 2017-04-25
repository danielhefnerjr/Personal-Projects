#!/bin/ruby

n = gets.strip.to_i
s = gets.strip
k = gets.strip.to_i

puts s.gsub(/([[:alpha:]])/) { |c| c >= 'a' ? ((c.ord - 97 + k) % 26 + 97).chr : ((c.ord - 65 + k) % 26 + 65).chr }
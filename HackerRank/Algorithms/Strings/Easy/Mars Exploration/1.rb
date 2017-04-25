#!/bin/ruby

s = gets.strip
sos = 'SOS' * (s.size/3)
puts (0..s.size-1).map {|i| s[i] != sos[i] }.count true
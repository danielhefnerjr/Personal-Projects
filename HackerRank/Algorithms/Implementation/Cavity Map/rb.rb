#!/bin/ruby

n = gets.strip.to_i
grid = Array.new(n)
for grid_i in (0..n-1)
    grid[grid_i] = gets.strip.split('').map &:to_i
end

cavs = []
for i in 1..n-2
   for j in 1..n-2
       cavs << [i,j] if grid[i][j-1]  < grid[i][j] \
                           && grid[i-1][j] < grid[i][j] \
                           && grid[i+1][j] < grid[i][j] \
                           && grid[i][j+1] < grid[i][j]
   end
end

cavs.each {|i,j| grid[i][j] = 'X'}

grid.each {|row|
    puts row.join('')
}
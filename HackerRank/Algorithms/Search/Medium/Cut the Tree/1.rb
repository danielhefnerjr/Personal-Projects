# INCORRECT SOLUTION

# tree structure:
# each node is a list where 0 -> value
#                           1 -> list of child nodes

# solution: At each edge tree_diff is the result of subtracting twice the total of the subtree being cut from the tree's total sum.
#           -> Recursively find the minimum value of this difference.  Check the value of cutting the whole left subtree, the whole right subtree,
#              then recurse to the left and right children.

def dfs(t,tot)
	return Float::INFINITY if !t
	return Float::INFINITY if t[1].size == 0
    [(tot-2*sum(t[1][0])).abs,(tot-2*sum(t[1][1])).abs,dfs(t[1][0],tot),dfs(t[1][1],tot)].min
end

def sum(t)
	return 0 if !t
    t.flatten.map {|v| @vv[v]}.inject :+ 
end

def insertAt(t,v,r)
	return false if !t
	# if inserting at root, build the initial tree structure (root value and empty child list)
    if r == nil
        t << v
        t << []
    else
        if t[0] == r
            if t[1][0] == nil
                t[1][0] = [v,[]]
            else
                t[1][1] = [v,[]]    
            end
            
            return true
        else
            return (t[1][0] ? insertAt(t[1][0],v,r) : false) || (t[1][1] ? insertAt(t[1][1],v,r) : false)
        end
    end
end

def isIn(t,v)
    t.flatten.include? v
end

n = gets.strip.to_i
@vv = gets.strip.split.map &:to_i
t = []
insertAt(t,0,nil)
(n-1).times do
    v1,v2 = gets.strip.split.map {|v| v.to_i - 1} 
    if !isIn(t,v2)
        insertAt(t,v2,v1)
    else
        insertAt(t,v1,v2)
    end
end

puts dfs(t,sum(t))
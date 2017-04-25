def permutations(s)
	perms(s,s,'')
end

def perms(s,rem,curr)
	if s.length == curr.length
		puts curr
		return
	end
	
	for c in rem.split('')
		perms(s,(rem.split('') - [c]).join, rem+c)
	end
end

permutations('abcd')
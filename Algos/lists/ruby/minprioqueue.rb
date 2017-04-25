class Element 
	include Comparable

    attr_accessor :val, :priority
  
    def initialize(val, priority)
        @val, @priority = val, priority
    end
  
    def <=>(other)
        @priority <=> other.priority
    end

end

class MinPriorityQueue
    def initialize
        @elements = [nil]
    end
  
	def empty?
		@elements.size <= 1
	end
	def << (element)
		push(element)
	end
	
    def push (element)
        @elements << element
        bubbleUp(@elements.size-1)
    end
    
    def bubbleUp(index)
        parent_index = index/2
        
        return if index <= 1
        
        return if @elements[parent_index] <= @elements[index]
        
        @elements[index], @elements[parent_index] = @elements[parent_index], @elements[index]
        
        bubbleUp(parent_index)
    end
    
    def pop
        @elements[1], @elements[-1] = @elements[-1], @elements[1]
        min = @elements.pop
        bubbleDown(1)
        min
    end
    
    def bubbleDown(index)
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        
        return if left_child_index > @elements.size - 1
        
        if right_child_index < @elements.size && @elements[right_child_index] < @elements[left_child_index]
            child_index = right_child_index
        else        
            child_index = left_child_index
        end
        
        return if @elements[index] <= @elements[child_index]
        
        @elements[index], @elements[child_index] = @elements[child_index], @elements[index]
        
        bubbleDown(child_index)
    end
end
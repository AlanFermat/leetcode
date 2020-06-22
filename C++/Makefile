CXX_FLAGS=-std=c++11 -O2 -Wall -Wextra


# The c++ compiler to invoke
CXX=clang++
all: leetcode

clean:
	rm -f *.o
	rm -f leetcode

%.o: %.cpp
	$(CXX) -c $(CXX_FLAGS) $< -o $@

leetcode: 1054.o
	$(CXX) $(CXX_FLAGS) -o $@ $^ 

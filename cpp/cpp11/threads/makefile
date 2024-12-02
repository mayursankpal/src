CC		= gcc
CXX		= g++
SOURCE	= sample.cpp
TARGET	= sample
LDFLAGS	= -g -std=c++17 -Wall -pthread

$(TARGET)	: $(SOURCE)
	$(CXX) $(LDFLAGS) $(SOURCE) -o $(TARGET)

clean	:
	rm -rf $(TARGET) *.o a.out
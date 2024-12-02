CC		= gcc
CXX		= g++
SOURCE	= sample.cpp
TARGET	= sample
LDFLAGS	= -g -std=c++17 -Wall -pthread
INCDIR	= /home/mayursankpal/third_party/boost_1_86_0

$(TARGET)	: $(SOURCE)
	$(CXX) $(LDFLAGS) -I $(INCDIR) $(SOURCE) -o $(TARGET)

clean	:
	rm -rf $(TARGET) *.o a.out
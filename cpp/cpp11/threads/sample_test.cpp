#include <gtest/gtest.h>
#include <thread>



//write main() for Init googletest
int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}
TEST(SampleTest, HelloWorld) {
    EXPECT_EQ(1 + 1, 2);
}

// //write test case for sample.cpp

// // Declare the thread function and global variable from sample.cpp
// extern void thread_func(bool flag);
// extern int global;

// TEST(SampleTest, ThreadFunction) {
//     // Create threads
//     std::thread th1(thread_func, false);
//     std::thread th2(thread_func, true);

//     // Join threads
//     th1.join();
//     th2.join();

//     // Check the global variable
//     EXPECT_EQ(global, 10);
// }
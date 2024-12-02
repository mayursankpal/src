#include <iostream>
#include <thread>
#include <mutex>
#include <condition_variable>

using namespace std;

std::mutex mx;
std::condition_variable cv;

int global = 1;


void thread_func(bool even)
{
	while(global < 10){
	std::unique_lock lck(mx);
		if(even && global%2 == 0)
		{	
			std::cout << "Thread No : " << this_thread::get_id() << std::endl;
			global++;
			cv.notify_all();
		}
		else{
			std::cout << "Thread No : " << this_thread::get_id() << std::endl;
			global++;
		}
	}
}

int main()
{
	std::thread th1(thread_func, false);
	std::thread th2(thread_func, true);

	th1.join();
	th2.join();

	return 0;
}


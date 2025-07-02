#include <iostream>

using namespace std;

class base{

    private :
        int m_count;
    public :
        base(){}
        ~base(){}

        virtual void set(int input){
            m_count = input ;
        }

        virtual void display(){
            std::cout << "m_count value : " << m_count << std::endl;
        }
};

class der : public base{

    private :

        int m_derivedCount;
    public:

        void set(int input){
            m_derivedCount = input;
        }
        void display(){
            std::cout << "m_derivedCount value : " << m_derivedCount << std::endl;
        }
        void funshow(){
            std::cout << "funshow m_derivedCount : " << m_derivedCount << std::endl;
        }
};

int main()
{
    base * ptr = new der();

    ptr->set(21);

    ptr->display();
    der obj;
    obj.funshow();
}
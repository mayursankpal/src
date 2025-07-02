#include <iostream>
#include <fstream>
#include <xml/parser>
#include <xml/serializer>

using namespace std;
using namespace xml;

enum gender{ male, 
female};

int main(int argc, char* argv[])
{
    std::ifstream ifs(argv[1]);
    xml::parser p(ifs, argv[1]);

    p.next_expect (parser::start_element,
                 "person",
                 content::complex);
    
    string n = p.element ("name");
    short a = p.element<short> ("age");
    //gender g = p.element<gender> ("gender");
    p.next_expect (parser::end_element);

  return 0;
}
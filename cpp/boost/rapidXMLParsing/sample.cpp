#include <boost/property_tree/ptree.hpp>
#include <boost/property_tree/xml_parser.hpp>
#include <iostream>

namespace pt = boost::property_tree;

int main() {
    std::string xml_str = R"(
        <?xml version="1.0" encoding="utf-8"?>
        <tv>
            <series>
                <name>Breaking Bad</name>
                <genre>crime</genre>
                <year>2008-2013</year>
                <creator>Vince Gilligan</creator>
                <imdb>9.4</imdb>
                <stream>Netflix</stream>
            </series>
            <!-- ... more series ... -->
        </tv>
    )";

    pt::ptree tv_tree;
    try {
        std::stringstream ss(xml_str);
        pt::read_xml(ss, tv_tree);
    } catch (pt::xml_parser_error& e) {
        std::cout << "Failed to parse the XML string: " << e.what() << std::endl;
    }

    // Iterate over the parsed tree
    for (const auto& p : tv_tree.get_child("tv")) {
        std::cout << "[" << p.first << "]" << std::endl;
        for (const auto& c : p.second) {
            std::cout << "Tag: [" << c.first.data() << "], Value: [" << c.second.data() << "]" << std::endl;
        }
    }

    return 0;
}

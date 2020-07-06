#include <iostream>
#include <vector>
#include <sstream>
#include <vector>
#include <string>

using namespace std;

class String{
  
  public:
    string s;

  public:
    
    String(string inp){
    s = inp;
    }

    String to_lower() const {
      // constructor
      //string dest(s);
      string dest = s;
      transform(s.begin(), s.end(), dest.begin(), ::tolower);
      /*
       * cout << "orig str:" << s << endl;
      cout << dest << endl;
      */
      // constructor
      // return dest also works, make it explicit/easier to understnd
      // new String object is created - RAII - constructor called when u create an object and init the memory
      // obj = String(dest) -> Python
      String obj(dest);
      return obj;
    }

    vector<String> split(const char delim) const{
      vector<String> dest;
      stringstream ss(s);
      string item;
      while (getline(ss, item, delim)) {
         dest.push_back(item);
         // elems.push_back(std::move(item)); // if C++11 (based on comment from @mchiasson)
          }
        return dest;
    }
};

int main(){
  string outp = {"Hello World"};
  cout << outp << endl;
  String obj(outp);
  String _lower = obj.to_lower();
  vector<String> _split = _lower.split(' ');
  //vector<string> _split = _lower.split(' ');
  cout << "Lower case: " << _lower.s << endl;
  //cout << "Split string: " << _split << endl;
  for(auto &ch : _split){
    cout << ch.s  << endl;
  }
}
//g++ -std=c++11 adapter.cpp && ./a.out

//incomplete as fk


#include <iostream>
#include <vector>
#include <algorithm>

std::string user_names[] = {"Admin", "usr1", "usr2", "usr3", "support"};
std::string pass_words[] = {"root123", "whyme", "superpass", "pass123", "zxy@147"};
std::vector<std::string> user_inputs;
int n_elem = sizeof(user_names) / sizeof(user_names[0]);

bool usernmae_chk (std::string& usrname){
    auto x = std::find(user_names, user_names+ 5, usrname);
    int idx = x - user_names;
    if (idx >= n_elem){
        user_inputs.push_back(usrname);
        std::cout << "Wrong user name!" << '\n';
        return 1;
    }
    return 0;
}


int main (){
    for (int i = 0; i < 3; i++){
            std::string usrname;
            std::cout << "Username: ";
            std::cin >> usrname;

            bool flg = usernmae_chk(usrname);
            if (bool){
                if(i == 2){
                    std::cout << "Too many wrong attemps!" << "\n";
                    std::cout  << "Failed attempts: ";
                    for (std::string names : user_inputs){
                        std::cout << names << " ";
                    }
                    std::cout  << "\n";
                }
                continue;
            }
            else{
                std::string pass;
                std::cout << "Password: ";
                std::cin >> pass;
                if (pass_words[idx] != pass){
                    std::cout << "Access denied!, Wrong password." << "\n";
                    continue;
                }
                else{
                    std::cout << "Access granted!" << "\n";
                    break;
                } 
            }
    }

}
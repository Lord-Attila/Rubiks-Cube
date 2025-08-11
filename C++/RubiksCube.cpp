#include <algorithm>
#include <iostream>
#include <string>
#include <array>
#include <unordered_map>
#include <vector>


class RubiksCube {
public:
    std::string last_move;
    std::string solution;
    std::string state;
    const std::array<std::string, 8> CorrectCornerPosition = {"wob", "wbr", "wgo", "wrg", "yrb",
        "ybo", "ygr", "yog"};

    RubiksCube() {
        last_move = "";
        solution = "";
        state = "gggggggggwwwwwwwwwrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy";
    }

    explicit RubiksCube(const std::string& state) {
        last_move = "";
        solution = "";
        this->state = state;
    }

    RubiksCube(const std::string& state, const std::string& last_move, const std::string& solution) {
        this->last_move = last_move;
        this->solution = solution;
        this->state = state;
    }

    void r() {
        std::string current_state = state;
        static const std::array<int,54> r_mapping = {
            0, 1, 51, 3, 4, 48, 6, 7, 45, //green
            9, 10, 2, 12, 13, 5, 15, 16, 8, //white
            24, 21, 18, 25, 22, 19, 26, 23, 20, //red
            27, 28, 29, 30, 31, 32, 33, 34, 35, //orange
            17, 37, 38, 14, 40, 41, 11, 43, 44, //blue
            36, 46, 47, 39, 49, 50, 42, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(r_mapping)/sizeof(r_mapping[0]); i++) {
            current_state[i] = state[r_mapping[i]];
        }
        state = current_state;
        solution += "R";
        last_move = "R";
    }

    void r(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> r_mapping = {
            0, 1, 51, 3, 4, 48, 6, 7, 45, //green
            9, 10, 2, 12, 13, 5, 15, 16, 8, //white
            24, 21, 18, 25, 22, 19, 26, 23, 20, //red
            27, 28, 29, 30, 31, 32, 33, 34, 35, //orange
            17, 37, 38, 14, 40, 41, 11, 43, 44, //blue
            36, 46, 47, 39, 49, 50, 42, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(r_mapping)/sizeof(r_mapping[0]); i++) {
            current_state[i] = state[r_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "R";
            last_move = "R";
        }
    }

    void r2() {
        r(false);
        r(false);
        solution += "R2";
        last_move = "R2";
    }

    void rprime() {
        r(false);
        r(false);
        r(false);
        solution += "R'";
        last_move = "R'";
    }

    void l() {
        std::string current_state = state;
        static const std::array<int,54> l_mapping = {
            9, 1, 2, 12, 4, 5, 15, 7, 8, //green
            44, 10, 11, 41, 13, 14, 38, 16, 17, //white
            18, 19, 20 ,21, 22, 23, 24, 25, 26, //red
            33, 30, 37, 34, 31, 28, 35, 32, 29, //orange
            36, 37, 53, 39, 40, 50, 42, 43, 37, //blue
            45, 46, 6, 48, 49, 3, 51, 52, 0 //yellow
        };
        for (int i = 0; i<sizeof(l_mapping)/sizeof(l_mapping[0]); i++) {
            current_state[i] = state[l_mapping[i]];
        }
        state = current_state;
        solution += "L";
        last_move = "L";
    }

    void l(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> l_mapping = {
            9, 1, 2, 12, 4, 5, 15, 7, 8, //green
            44, 10, 11, 41, 13, 14, 38, 16, 17, //white
            18, 19, 20 ,21, 22, 23, 24, 25, 26, //red
            33, 30, 37, 34, 31, 28, 35, 32, 29, //orange
            36, 37, 53, 39, 40, 50, 42, 43, 37, //blue
            45, 46, 6, 48, 49, 3, 51, 52, 0 //yellow
        };
        for (int i = 0; i<sizeof(l_mapping)/sizeof(l_mapping[0]); i++) {
            current_state[i] = state[l_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "L";
            last_move = "L";
        }
    }

    void l2() {
        l(false);
        l(false);
        solution += "L2";
        last_move = "L2";
    }

    void lprime() {
        l(false);
        l(false);
        l(false);
        solution += "L'";
        last_move = "L'";
    }

    void f() {
        std::string current_state = state;
        static const std::array<int,54> f_mapping = {
            6, 3, 0, 7, 4, 1, 8, 5, 2, //green
            9, 10, 11, 12, 13, 14, 35, 32, 29, //white
            15, 19, 20, 16, 22, 23, 17, 25, 26, //red
            27, 28, 53, 30, 31, 52, 33, 34, 51, //orange
            36, 37, 38, 39, 40, 41, 42, 43, 44, //blue
            45, 46, 47, 48, 49, 50, 24, 21, 18 //yellow
        };
        for (int i = 0; i<sizeof(f_mapping)/sizeof(f_mapping[0]); i++) {
            current_state[i] = state[f_mapping[i]];
        }
        state = current_state;
        solution += "F";
        last_move = "F";
    }

    void f(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> f_mapping = {
            6, 3, 0, 7, 4, 1, 8, 5, 2, //green
            9, 10, 11, 12, 13, 14, 35, 32, 29, //white
            15, 19, 20, 16, 22, 23, 17, 25, 26, //red
            27, 28, 53, 30, 31, 52, 33, 34, 51, //orange
            36, 37, 38, 39, 40, 41, 42, 43, 44, //blue
            45, 46, 47, 48, 49, 50, 24, 21, 18 //yellow
        };
        for (int i = 0; i<sizeof(f_mapping)/sizeof(f_mapping[0]); i++) {
            current_state[i] = state[f_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "F";
            last_move = "F";
        }
    }

    void f2() {
        f(false);
        f(false);
        solution += "F2";
        last_move = "F2";
    }

    void fprime() {
        f(false);
        f(false);
        f(false);
        solution += "F'";
        last_move = "F'";
    }

    void b() {
        std::string current_state = state;
        static const std::array<int,54> b_mapping = {
            0, 1, 2, 3, 4, 5, 6, 7, 8, //green
            20, 23, 26, 12, 13, 14, 15, 16, 17, //white
            18, 19, 45 ,21, 22, 46, 24, 25, 47, //red
            11, 28, 29, 10, 31, 32, 9, 34, 35, //orange
            42, 39, 36, 43, 40, 37, 44, 41, 38, //blue
            33, 30, 27, 48, 49, 50, 51, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(b_mapping)/sizeof(b_mapping[0]); i++) {
            current_state[i] = state[b_mapping[i]];
        }
        state = current_state;
        solution += "B";
        last_move = "B";
    }

    void b(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> b_mapping = {
            0, 1, 2, 3, 4, 5, 6, 7, 8, //green
            20, 23, 26, 12, 13, 14, 15, 16, 17, //white
            18, 19, 45 ,21, 22, 46, 24, 25, 47, //red
            11, 28, 29, 10, 31, 32, 9, 34, 35, //orange
            42, 39, 36, 43, 40, 37, 44, 41, 38, //blue
            33, 30, 27, 48, 49, 50, 51, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(b_mapping)/sizeof(b_mapping[0]); i++) {
            current_state[i] = state[b_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "B";
            last_move = "B";
        }
    }

    void b2() {
        r(false);
        r(false);
        solution += "B2";
        last_move = "B2";
    }

    void bprime() {
        b(false);
        b(false);
        b(false);
        solution += "B'";
        last_move = "B'";
    }

    void u() {
        std::string current_state = state;
        static const std::array<int,54> u_mapping = {
            18, 19, 20, 3, 4, 5, 6, 7, 8, //green
            15, 12, 9, 16, 13, 10, 17, 14, 11, //white
            36, 37, 38 ,21, 22, 23, 24, 25, 26, //red
            0, 1, 2, 30, 31, 32, 33, 34, 35, //orange
            27, 28, 29, 39, 40, 41, 42, 43, 44, //blue
            45, 46, 47, 48, 49, 50, 51, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(u_mapping)/sizeof(u_mapping[0]); i++) {
            current_state[i] = state[u_mapping[i]];
        }
        state = current_state;
        solution += "U";
        last_move = "U";
    }

    void u(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> u_mapping = {
            18, 19, 20, 3, 4, 5, 6, 7, 8, //green
            15, 12, 9, 16, 13, 10, 17, 14, 11, //white
            36, 37, 38 ,21, 22, 23, 24, 25, 26, //red
            0, 1, 2, 30, 31, 32, 33, 34, 35, //orange
            27, 28, 29, 39, 40, 41, 42, 43, 44, //blue
            45, 46, 47, 48, 49, 50, 51, 52, 53 //yellow
        };
        for (int i = 0; i<sizeof(u_mapping)/sizeof(u_mapping[0]); i++) {
            current_state[i] = state[u_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "U";
            last_move = "U";
        }
    }

    void u2() {
        u(false);
        u(false);
        solution += "U2";
        last_move = "U2";
    }

    void uprime() {
        u(false);
        u(false);
        u(false);
        solution += "U'";
        last_move = "U'";
    }

    void d() {
        std::string current_state = state;
        static const std::array<int,54> d_mapping = {
            0, 1, 2, 3, 4, 5, 33, 34, 35, //green
            9, 10, 11, 12, 13, 14, 15, 16, 17, //white
            18, 19, 20 ,21, 22, 23, 6, 7, 8, //red
            27, 28, 29, 30, 31, 32, 42, 43, 44, //orange
            36, 37, 38, 39, 40, 41, 24, 25, 26, //blue
            47, 50, 53, 46, 49, 52, 45, 48, 51 //yellow
        };
        for (int i = 0; i<sizeof(d_mapping)/sizeof(d_mapping[0]); i++) {
            current_state[i] = state[d_mapping[i]];
        }
        state = current_state;
        solution += "D";
        last_move = "D";
    }

    void d(const bool& record) {
        std::string current_state = state;
        static const std::array<int,54> d_mapping = {
            0, 1, 2, 3, 4, 5, 33, 34, 35, //green
            9, 10, 11, 12, 13, 14, 15, 16, 17, //white
            18, 19, 20 ,21, 22, 23, 6, 7, 8, //red
            27, 28, 29, 30, 31, 32, 42, 43, 44, //orange
            36, 37, 38, 39, 40, 41, 24, 25, 26, //blue
            47, 50, 53, 46, 49, 52, 45, 48, 51 //yellow
        };
        for (int i = 0; i<sizeof(d_mapping)/sizeof(d_mapping[0]); i++) {
            current_state[i] = state[d_mapping[i]];
        }
        state = current_state;
        if (record) {
            solution += "D";
            last_move = "D";
        }
    }

    void d2() {
        d(false);
        d(false);
        solution += "D2";
        last_move = "D2";
    }

    void dprime() {
        d(false);
        d(false);
        d(false);
        solution += "D'";
        last_move = "D'";
    }

    void print() const {
        for (int i = 0; i<state.length()/3; i+=3) {
            std::cout << state.substr(i,3) << std::endl;
        }
    }

    void reset_solution() {
        solution = "";
    }

    void reset_last_move() {
        last_move = "";
    }

    bool is_solved() const {
        if (state == "gggggggggwwwwwwwwwrrrrrrrrrooooooooobbbbbbbbbyyyyyyyyy") {
            return true;
        } else {
            return false;
        }
    }

    const std::string& get_last_move() const {
        return last_move;
    }

    const std::string& get_state() const {
        return state;
    }

    const std::string& get_solution() const {
        return solution;
    }

    void scramble(std::string& scramble){
        const std::string delimiter = " ";
        std::vector<std::string> moves;
        while (!scramble.empty()) {
            std::string token = scramble.substr(0, scramble.find(delimiter));
            moves.push_back(token);
            scramble.erase(0, scramble.find(delimiter) + 1);
        }
        static const std::unordered_map<std::string, void (RubiksCube::*)()> move_map = {
            {"R", &RubiksCube::r}, {"R'", &RubiksCube::rprime}, {"R2", &RubiksCube::r2},
            {"L", &RubiksCube::l}, {"L'", &RubiksCube::lprime}, {"L2", &RubiksCube::l2},
            {"F", &RubiksCube::f}, {"F'", &RubiksCube::fprime}, {"F2", &RubiksCube::f2},
            {"U", &RubiksCube::u}, {"U'", &RubiksCube::uprime}, {"U2", &RubiksCube::u2},
            {"D", &RubiksCube::d}, {"D'", &RubiksCube::dprime}, {"D2", &RubiksCube::d2},
            {"B", &RubiksCube::b}, {"B'", &RubiksCube::bprime}, {"B2", &RubiksCube::b2}
        };
        for (const std::string& move : moves) {
            auto it = move_map.find(move);
            if (it != move_map.end()) {
                (this->*(it->second))();
            }
        }
    }

    void random_scramble() {
        const std::array<std::string, 18> moves = {
            "R", "R'", "R2", "L", "L2", "L'",
            "D", "D'", "D2",  "U", "U'", "U2",
            "F", "F'", "F2", "B", "B2", "B'"
        };
        std::string scramble;
        int random_number = 4 + std::rand() % 25;
        for (int i = 0; i<random_number; i++) {
            int random_number2 = std::rand() % 19;
            scramble += moves[random_number2];
            scramble += " ";
        }
        this->scramble(scramble);
    }

    bool g1_white_yellow() const {
        bool result = true;
        std::string white_face = state.substr(0,9); //might be pos 9 idk
        std::string yellow_face = state.substr(45, 9);
        result = result && (white_face.find('g') != std::string::npos)
            && (white_face.find('r') != std::string::npos)
            && (white_face.find('o') != std::string::npos)
            && (white_face.find('b') != std::string::npos);
        result = result && (yellow_face.find('g') != std::string::npos)
            && (yellow_face.find('r') != std::string::npos)
            && (yellow_face.find('o') != std::string::npos)
            && (yellow_face.find('b') != std::string::npos);
        bool green =
        bool blue =
        bool orange =
        bool red =
        result = result && blue && orange && green && red;
        return result;

    }

    bool g1_blue_green() const {

    }

    bool g1_red_orange() const {

    }
};

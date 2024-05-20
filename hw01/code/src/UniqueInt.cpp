#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

void process_file(const std::string& input_file_path, const std::string& output_file_path) {
    std::vector<bool> seen(2047, false);

    std::ifstream input_file(input_file_path);
    if (!input_file.is_open()) {
        std::cerr << "Error: Unable to open input file." << std::endl;
        return;
    }

    std::string line;
    while (std::getline(input_file, line)) {
        line.erase(std::remove_if(line.begin(), line.end(), ::isspace), line.end()); // Remove whitespace
        if (!line.empty()) {
            if (line.find(' ') == std::string::npos) {
                try {
                    int num = std::stoi(line);
                    if (-1023 <= num && num <= 1023) {
                        seen[num + 1023] = true;
                    }
                } catch (const std::invalid_argument& e) {
                    // Ignore invalid entries
                } catch (const std::out_of_range& e) {
                    // Ignore out-of-range entries
                }
            }
        }
    }
    input_file.close();

    std::ofstream output_file(output_file_path);
    if (!output_file.is_open()) {
        std::cerr << "Error: Unable to open output file." << std::endl;
        return;
    }

    for (int i = 0; i < seen.size(); ++i) {
        if (seen[i]) {
            output_file << (i - 1023) << '\n';
        }
    }
    output_file.close();
}

int main() {
    std::string current_dir = __FILE__;
    current_dir = current_dir.substr(0, current_dir.find_last_of("/\\"));

    std::string input_file_path = current_dir + "/../../sample_inputs/sample_01.txt";
    std::string output_file_path = current_dir + "/../../sample_results/sample_01.txt_result.txt";

    process_file(input_file_path, output_file_path);

    return 0;
}

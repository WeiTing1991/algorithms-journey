#include <string>

using namespace std;

class Solution {
 public:
  bool isPalindrome(string s) {
    int start = 0;
    int end = s.size() - 1;
    while (start <= end) {
      if (!isalnum(s[start])) {
        start++;
        continue;
      }
      if (!isalnum(s[end])) {
        end--;
        continue;
      }
      if (tolower(s[start]) != tolower(s[end]))
        return false;
      else {
        start++;
        end--;
      }
    }
    return true;
  }
};

int main() {
    string s = " ";
    string s2 = "A man, a plan, a canal: Panama";
    string s3 = "race a car";

    Solution solution;
    solution.isPalindrome(s);
    solution.isPalindrome(s2);
    solution.isPalindrome(s3);
    return 0;
}


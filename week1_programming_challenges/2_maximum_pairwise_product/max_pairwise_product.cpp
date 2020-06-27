#include<cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

long long MaxPairwiseProductFast(const std::vector<long long>& numbers) {
    int max_1 = -1;
    int max_2 = -1;
    int n = numbers.size();
    for(int i=0;i<n;i++){
      if((max_1 == -1) || (numbers[i]>numbers[max_1])){
        max_1 = i;
      }
    }
    for(int j = 0; j<n; j++){
      if((j != max_1) && ((max_2 == -1) || (numbers[j] > numbers[max_2]))) {
        max_2 = j;
      }
    }
    return numbers[max_1]*numbers[max_2];
}

int main() {
  int n;
  std::cin >> n;
  std::vector<long long> numbers(n);
  for (int i = 0; i < n; ++i) {
    std::cin >> numbers[i];
  }

  std::cout << MaxPairwiseProductFast(numbers) << "\n";
  return 0;
}

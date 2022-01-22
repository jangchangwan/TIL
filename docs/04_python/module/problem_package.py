from my_package.math import tools
from my_package.statistics.tools import standard_deviation as sd # as를 통해 함수를 별명으로 부를수 있다.
# print(dir(tools))


print('#############################')
print('my_max() 함수 호출 :',tools.my_max(2,3))
print('#############################')
print('자연상수 e 출력 : ',tools.e)
print('#############################')
print('PI 호출 :',tools.pi)


print('#############################')
print('standard_deviation 함수 호출 :',sd([1,2,3,4,5]))


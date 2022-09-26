# def find_mirror_num(n: int) -> int:
#     result = count = 0
#     while True:
#         if str(result)[::-1] == str(result):
#             count = count + 1
#             if count == n:
#                 return result
#         result = result + 1
#
# print(find_mirror_num(2))
# print(find_mirror_num(10))
# print(find_mirror_num(100))

# param1 = {
#             "access_token": "access_token"
#         }
# param2={
#     "id": "department_id"
# }
# print(dict(param1,**param2))

def solution(nums: str) -> str:
    b = nums.split(" ")
    print(b)
    c = list(map(int, b))
    return str(max(c))+" "+str(min(c))

print(solution("1 2 3 4 5"))
print(solution("1 2 -3 4 5"))
print(solution("1 9 3 4 -5"))
print(solution("1 2 3"))
print(solution("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
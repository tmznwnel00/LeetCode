class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        first_fruit, first_num, first_cont = -1, 0, 0
        second_fruit, second_num, second_cont = -1, 0, 0
        answer = 0

        for fruit in fruits:
            if fruit == first_fruit:
                first_num += 1
                first_fruit, second_fruit = second_fruit, first_fruit
                first_num, second_num = second_num, first_num
                first_cont, second_cont = second_cont, 1
            elif fruit == second_fruit:
                second_num += 1
                second_cont += 1
            else:
                answer = max(answer, first_num + second_num)
                
                first_fruit, first_num, first_cont, second_fruit, second_num, second_cont = second_fruit, second_cont, second_cont, fruit, 1, 1
            # print(fruit, first_fruit, second_fruit, answer)
        answer = max(answer, first_num + second_num)
        return answer


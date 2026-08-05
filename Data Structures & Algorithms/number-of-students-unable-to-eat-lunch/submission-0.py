class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        n = len(students)
        stud_eat_one = sum(students)
        count = {0:n - stud_eat_one,1:stud_eat_one}
        for elt in sandwiches:
            if count[elt]>0:
                count[elt]-=1
            else:
                return count[1-elt]
        return 0


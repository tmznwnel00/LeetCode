class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        check = set([])
        str_list = []
        str_dict = {}
        for i in range(len(s1)):
            if s1[i] in check and s2[i] in check:
                if str_dict[s1[i]] == str_dict[s2[i]]:
                    continue
                else:
                    index1 = str_dict[s1[i]]
                    index2 = str_dict[s2[i]]
                    l1 = str_list[str_dict[s1[i]]]
                    l2 = str_list[str_dict[s2[i]]]
                    l3 = l1
                    l4 = l2
                    str_list[index1] = list(set(l1 + l2))
                    str_list[index2] = list(set(l2 + l3))
                    if index1 > index2:
                        for j in l3:
                            str_dict[j] = index2
                    else:
                        for j in l4:
                            str_dict[j] = index1
                            
            elif s1[i] == s2[i]:
                continue
            elif s1[i] in check and s2[i] not in check:
                index = str_dict[s1[i]]
                l = str_list[index]
                l.append(s2[i])
                str_dict[s2[i]] = index
                check.add(s2[i])
            elif s2[i] in check and s1[i] not in check:
                index = str_dict[s2[i]]
                l = str_list[index]
                l.append(s1[i])
                str_dict[s1[i]] = index
                check.add(s1[i])
            else:
                l = [s1[i], s2[i]]
                str_list.append(l)
                str_dict[s1[i]] = len(str_list) - 1
                str_dict[s2[i]] = len(str_list) - 1
                check.add(s1[i])
                check.add(s2[i])
        answer = ''
        for j in range(len(str_list)):
            str_list[j] = sorted(str_list[j])
        for i in baseStr:
            if i in check:
                answer += min(str_list[str_dict[i]])
            else:
                answer += i
            
        return answer
        
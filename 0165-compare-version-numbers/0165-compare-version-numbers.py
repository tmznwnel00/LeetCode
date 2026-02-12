class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for i in range(max(version1.count('.'), version2.count('.')) + 1):
            try:
                v1, v2 = int(version1.split('.')[i]), int(version2.split('.')[i])
            except:
                if version1.count('.') > version2.count('.'):
                    if int(version1.split('.')[i]) != 0:
                        return 1
                    else:
                        continue
                else:
                    if int(version2.split('.')[i]) != 0:
                        return -1
                    else:
                        continue
            
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1

        return 0
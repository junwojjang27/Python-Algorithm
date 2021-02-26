def groupAnagrams(strs):
    
    strs_chg = []   

    for a in strs:  #알파벳 순으로 정렬한 뒤 저장.
        temp = list(a)
        strs_chg.append(''.join(sorted(temp)))

    strs_dict = {}

    for a in strs_chg:     #알파벳 순으로 정렬한 리스트를 딕셔너리에 저장.
        if a in strs_dict:
            strs_dict[a] += 1
        else:
            strs_dict[a] = 1

    sort_list = list(strs_dict.keys())  #딕셔너리 키로 리스트를 만듬

    final_list = []

    #최종적으로 리스트에 애너그램을 그룹화해서 집어넣고 final_list에 집어넣음.
    for a in sort_list:     
        temp_2 = []
        i = 0
        for b in strs_chg:
            if b == a:
                temp_2.append(strs[i])
            i += 1
        final_list.append(sorted(temp_2))
        
    return final_list

if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print(groupAnagrams(strs))



"""
import collections 하여 (collections 모듈)
collections.defaultdict()를 활용가능
딕셔너리와 비슷하지만 키가 없을 떄 default값을 자동으로 반환
"""
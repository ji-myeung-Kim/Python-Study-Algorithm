'''
문제 - BFS, DFS
프로그래머스 타겟넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
'''


def solution(numbers, target):
    tree = [0]
    for num in numbers:
        sub_tree = []
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
        tree = sub_tree
    return tree.count(target)


'''
풀이
def solution(numbers, target):
    tree = [0]
        # 트리의 첫번째 층에 0 넣기
    
    for num in numbers:
        sub_tree = []
            # 매개변수로 받은 숫자 목록을 하나씩 꺼냄
        
        for tree_num in tree:
            sub_tree.append(tree_num + num)
            sub_tree.append(tree_num - num)
                # 트리의 노드에 있는 숫자를 더하고 빼서 자식 노드 생성
            
        tree = sub_tree
            # 트리는 이전 수에 대한 계산 결과를 담은 층
            # 서브트리는 현재 숫자에 대한 결과를 담은 자식 노드를 하나씩 추가
        
    return tree.count(target)
'''
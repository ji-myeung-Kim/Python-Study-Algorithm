def solution(priorities, location):
    answer = 0
    pi_list = [(p, i) for (i, p) in enumerate(priorities)]

    while pi_list:
        prior = pi_list.pop(0)

        if pi_list:
            p_list = [priority for priority, idx in pi_list]

        if p_list:
            if prior[0] >= max(p_list):
                if prior[1] == location:
                    return answer + 1
                else:
                    answer += 1
            else:
                pi_list.append(prior)

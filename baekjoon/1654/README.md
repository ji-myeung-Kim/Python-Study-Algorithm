## [백준 1654 - 랜선자르기](https://www.acmicpc.net/problem/1654)

### input()대신 sys.stdin.readline()을 사용하는 이유

- input() 내장 함수는 sys.stdin.readline()과 비교해서 prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느리다.
- 한 두줄 입력받는 문제들과 다르게, 반복문으로 여러줄을 입력 받아야 할 때는 input()으로 입력 받는다면 시간초과가 발생할 수 있습니다.

### 참고
- [Input vs. sys.stdin.readline 차이점](https://buyandpray.tistory.com/7)
- [파이썬 입력 받기(sys.stdin.readline)](https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline)
- [풀이 참고](https://st-lab.tistory.com/269) : 은진님이 찾은 블로그인데 코드는 파이썬 아니지만 설명이 엄청 자세해서 이해하기 쉽습니다.

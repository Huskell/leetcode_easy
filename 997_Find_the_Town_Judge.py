from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:

        vertex = N
        graph = {}
        for i in range(1, vertex + 1):
            graph[i] = []
        for i in trust:
            if graph[i[0]] == []:
                graph[i[0]].append(i[1])
            else:
                graph[i[0]].append(i[1])

        for i in range(1, vertex + 1):
            if graph[i] == []:
                trusted = [False for _ in range(vertex)]
                trusted[i-1] = True
                for j in range(1, vertex + 1):
                    if i in graph[j]:
                        trusted[j-1] = True

                if False not in trusted:
                    return i
        return -1

    def findJudge2(self, N: int, trust: List[List[int]]) -> int:
        in_edges, out_edges = [0] * N, [0] * N

        for t in trust:
            s, d = t[0] - 1, t[1] - 1
            in_edges[d] += 1
            out_edges[s] += 1
        print(in_edges, out_edges)
        for i in range(0, N):
            if (in_edges[i] == N - 1 and out_edges[i] == 0):
                return i + 1
        return -1




if __name__ == '__main__':
    N = 4
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

    # N = 11
    # trust = [[1, 8], [1, 3], [2, 8], [2, 3], [4, 8], [4, 3], [5, 8], [5, 3], [6, 8], [6, 3], [7, 8], [7, 3], [9, 8], [9, 3], [11, 8], [11, 3]]

    sol = Solution().findJudge2(N, trust)
    print(sol)
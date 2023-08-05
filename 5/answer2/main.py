def print_permutations(string):
    visited = [False] * len(string)

    permutations_helper(string, "", visited)


def permutations_helper(str, prefix, visited):
    if len(prefix) == len(str):
        print(prefix)
        return

    for i in range(len(str)):
        if not visited[i]:
            visited[i] = True
            new_prefix = prefix + str[i]
            permutations_helper(str, new_prefix, visited)
            visited[i] = False


if __name__ == '__main__':
    string = input()
    print_permutations(string)

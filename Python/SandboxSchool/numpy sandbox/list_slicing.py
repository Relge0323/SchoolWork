numbers = input().split()

frontAndBack = numbers[:] + numbers[-1::-1]

gettinCrazy = ([numbers[0]] + frontAndBack + [numbers[-1]]) * 2


print(gettinCrazy)
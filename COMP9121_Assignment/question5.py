n = ('c3b588e9483030f2929d405eab0d672e'
     '4aad3cae52aca1bdd607d3fb88b2da85'
     '0d09dd207e374d31dc5078d06438c40e'
     '6013f1e725406076d07b5c99db4ef7db'
     '3be0afd01b59beb5ed1134943a80c6d3'
     '01d7d0272ae8559cc1e5b167c6cb2608'
     '15e507f66043fea953a9a76a515ee129'
     'f0726b88b9db8607925d64a2b04d63b5')

p = ('f1fe23ef77b3f72b205ef20c7883205e'
     '636d46f9935f93b428e309c7a74bc9c0'
     'f69f11da9a5d725d1deed855e14d50b9'
     '88198caf5b841acce74e31df998091bb')

q = ('cf098fc972a33e7a1c853265769da918'
     '84ea9421c3524404ae5cdc41449513f4'
     'd1ce7db3f8e126d2ba6e752c8928627e'
     '592297b81edd32e158c16f08c329114f')

e = '010001'

d = ('2fc30be8b2bf6012b309417e590c6a53'
     'f7d1936f8fa9a5c768867c8b746f01b9'
     '5ad73f6a00a38a6952b528e6e2ae9fda'
     '4a4453d2ef5a68b0566ce4ca7fa52403'
     'a56173144dd7aa8fb20f2d52d14659d4'
     'b23c721732f121840fedea55f9e31747'
     '4eb48b63f9bb096abe5681d2809e03a2'
     '8167e3b00f87ca5cb2235c530aba79f9')

n1 = int(n, 16)
p1 = int(p, 16)
q1 = int(q, 16)
e1 = int(e, 16)
d1 = int(d, 16)
z = (p1 - 1) * (q1 - 1)
if p1 * q1 == n1:
    print('True')
else:
    print('False')

if (e1 * d1) % z == 1:
    print('True')
else:
    print('False')

s = ((e1 * d1) - 1) / z
print(s)

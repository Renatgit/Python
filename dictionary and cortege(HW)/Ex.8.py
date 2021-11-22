archie={
    'kind':'dog',
    'host':'Renat'
    }
gracie={
    'kind':'cat',
    'host':'Andrew'
    }
homik={
    'kind':'hamster',
    'host':'Den'
    }
pets=[archie, gracie, homik]

for n in pets:
    print('-'*30)
    for k, v in n.items():
        kind=f"{n['kind']}"
        host=f"{n['host']}"
    print(f"\tKind of animal: {kind}")
    print(f"\tHost name: {host.title()}")

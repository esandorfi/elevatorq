class TheHobbit:
    def __len__(self):
        return 95022


th = TheHobbit()
print(len(th))


def greet(name: str) -> str:
    return "Hello " + name


def headline(text: str, align: bool = True) -> str:
    if align:
        return f"{text}\n{'-'*len(text)}"
    else:
        return f" {text} ".center(50, "-")


print(headline("By", False))
print(headline("Hello"))
print(headline(2, align=2))


y = greet("Manu")
print(y)

if False:
    x = 1 + "Two"
else:
    x = 1 + 2
print(x)

dict = {"ok0": 1}

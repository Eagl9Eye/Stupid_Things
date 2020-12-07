import json

json_input = '{"quiz": {"sport": {"q1": {"question":"Which one is correct team name in NBA?","options": ["New York Bulls","Los Angeles Kings","Golden State Warriros","Huston Rocket"],"answer":"Huston Rocket"}},"maths": {"q1": {"question":"5 + 7 = ?","options": ["10","11","12","13"],"answer":"12"},"q2": {"question":"12 - 8 = ?","options": ["1","2","3","4"],"answer":"4"}}}}'


def tree_viewer(treeobj, symbols={}):
    symbols = {**{"seperator": "|>", "linebreak": "|\\",
                  "line": "| ", "endline": "|/", "end": "*"}, **symbols}
    print_branch(obj=treeobj, symbols=symbols)
    print(symbols["end"])


def print_branch(obj, symbols, beforehand=""):

    def front(func):
        def inner(*args):
            print(f'{beforehand}', end='')
            return func(*args)
        return inner

    def print_dict(obj):
        for k in obj:
            print_name(k)
            print_newline()
            print_branch(obj[k], symbols,
                         beforehand+symbols["line"])
            if(k == list(obj)[-1]):
                print_endline()
            else:
                print_line()

    @front
    def print_name(name):
        print(f'{name:12}')

    @front
    def print_newline():
        print(symbols["linebreak"])

    @front
    def print_endline():
        print(symbols["endline"])

    @front
    def print_line():
        print(symbols["line"])

    def print_list(obj):
        for o in obj:
            print_item(o)

    @front
    def print_item(item):
        print(f'{symbols["seperator"]}{item}')

    switcher = {
        dict: print_dict,
        list: print_list,
        tuple: print_list,
        set: print_list,
        str: print_item
    }
    switcher.get(type(obj), symbols["endline"])(obj)


json_object = json.loads(json_input)
tree_viewer(json_object)

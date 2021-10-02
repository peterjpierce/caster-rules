from dragonfly import Mimic, Function, MappingRule

from castervoice.lib.actions import Key, Text

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import IntegerRefST
from castervoice.lib.merge.state.short import R

# Added
from castervoice.lib import navigation


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class BaseRule(MappingRule):
#    GIT_ADD_ALL = "g, i, t, space, a, d, d, space, minus, A"
#    GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"

    mapping = {
        "(fit|fight)": Key("1"),
        
        "(placeholder_!)": Key("!"),
        "(placeholder_$)": Key("$"),
        "(placeholder_#)": Key("#"),
        "(placeholder_:)": Key(":"),
        "(ride|horse)": Text(","),
    
        "(placeholder_entrap)": Key("x"),

        "(placeholder_sy)": Key("s-y"),

        "(more health)": Key("f2"),
        "(more manner)": Key("f3"),
        "(mark)": Key("f8"),
        "(patch|bandage)": Key("f9"),
        "(drink)": Key("f11"),
        "(eat|food|full)": Key("f12"),N()

        "(red)": Key("tab"),
        "(green)": Key("c-tab"),

        "(rake)": R(Function(navigation.right_click)),
        "(gnarl|nick)": Key("n"),
        "(Run|stop)": Text("~"),
        "(bait)": Text("/cast Fishing") + R(Key('enter')),
    }
    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}

    def add_key(keypress, phrase_pattern):
        self.mapping[phrase_pattern] = Key(keypress)

    def add_text(keypress, phrase_pattern):
        self.mapping[phrase_pattern] = Text(keypress)

    def add_left_click(phrase_pattern):
        self.mapping[phrase_pattern] =  R(Function(navigation.left_click))

    def add_right_click(phrase_pattern):
        self.mapping[phrase_pattern] =  R(Function(navigation.right_click))


_executables = []


def get_rule(name):
    return BaseRule, RuleDetails(name=name, executable=_executables)


# EXAMPLES
#        "(git|get) add all":
#            R(Key(GIT_ADD_ALL)),
#        "(git|get) commit all":
#            R(Key("%s, ;, space, %s" % (GIT_ADD_ALL, GIT_COMMIT))),
#        "(git|get) status":
#            R(Key("g, i, t, space, s, t, a, t, u, s")),
#        "(git|get) commit":
#            R(Key(GIT_COMMIT)),
#        "(git|get) bug fix commit <n>":
#            R(Mimic("get", "commit") + Text("fixes #%(n)d ") + Key("backspace")),
#        "search recursive count":
#            R(Text("grep -rinH \"PATTERN\" * | wc -l")),
#        "search recursive file type":
#            R(Text("find . -name \"*.java\" -exec grep -rinH \"PATTERN\" {} \\;")),
#        "to file":
#            R(Text(" > FILENAME")),

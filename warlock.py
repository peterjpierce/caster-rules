from dragonfly import Mimic, Function, MappingRule

from castervoice.lib.actions import Key, Text

from castervoice.lib.ctrl.mgr.rule_details import RuleDetails
from castervoice.lib.merge.additions import ShortIntegerRef
from castervoice.lib.merge.state.short import R

# Added
from castervoice.lib import navigation


def _apply(n):
    if n != 0:
        Text("stash@{" + str(int(n)) + "}").execute()


class NoodleRule(MappingRule):
#    GIT_ADD_ALL = "g, i, t, space, a, d, d, space, minus, A"
#    GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"

    mapping = {
        "(shoot)": Key("1"),
        "(bolt|bold)": Key("2"),
        "(corrupt|corruption)": Key("3"),
        "(agony)": Key("4"),
        "(siphon)": Key("5"),
        "(immolate)": Key("6"),
        "(pain)": Key("7"),
        "(placeholder8)": Key("8"),
        "(reckless)": Key("9"),
        "(attack)": Key("10"),
        "(placeholder11)": Key("11"),
        "(placeholder12)": Key("12"),
        
        "(howl|how|terror)": Key("!"),
        "(hill|hell|hell fire)": Key("$"),
        "(rain|rain fire)": Key("#"),
#        "(amplify)": Key(":"),
        "(ride|horse)": Text(","),
    
        "(burn)": Key("d"),
        "(fear)": Key("x"),
        "(drain|life)": Key("f"),
        "(final|funnel)": Key("h"),
        "(tap|tab)": Key("t"),
        "(soul|sold)": Key("r"),
        "(ward|word|award|shadow award)": Key("y"),
        "(fear)": Key("x"),
        "(quail|coil)": Key("a"),
        "(pet|pat)": Key("c"),

        "(stone|health stone)": Key("s-h"),
        "(tongue|ton|tongues)": Key("s-t"),
        "(leach|leach manner)": Key("s-r"),
        "(breath|breathe)": Key("s-u"),
        "(bubble|sacrifice)": Key("s-x"),

        "(more health)": Key("f2"),
        "(more manner)": Key("f3"),
        "(free me)": Key("f3"),
        "(patch|bandage)": Key("f9"),
        "(drink)": Key("f11"),
        "(eat|food|full)": Key("f12"),

        "(red)": Key("tab"),
        "(green)": Key("c-tab"),

        "(rake)": R(Function(navigation.right_click)),
        "(gnarl|nick)": Key("n"),
        "(run|stop)": Text("~"),
    }
    extras = [
        ShortIntegerRef("n", 1, 10000),
    ]
    defaults = {"n": 0}


_executables = []


def get_rule():
    return NoodleRule, RuleDetails(name="noodle", executable=_executables)


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

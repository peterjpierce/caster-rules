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


class DruidRule(MappingRule):
#    GIT_ADD_ALL = "g, i, t, space, a, d, d, space, minus, A"
#    GIT_COMMIT = "g, i, t, space, c, o, m, m, i, t, space, minus, m, space, quote, quote, left"

    mapping = {
        "(fit|fight)": Key("1"),
        "(wrath)": Key("2"),
        "(moon|moon fire)": Key("3"),
        "(placeholder4)": Key("4"),
        "(placeholder5)": Key("5"),
        "(theory|fairy)": Key("6"),
        "(placeholder7)": Key("7"),
        "(placeholder8)": Key("8"),
        "(placeholder9)": Key("9"),
        "(attack|tack)": Key("0"),
        "(placeholder11)": Key("11"),
        "(placeholder12)": Key("12"),
        
        "(placeholder_!)": Key("!"),
        "(placeholder_$)": Key("$"),
        "(placeholder_#)": Key("#"),
#        "(placeholder_:)": Key(":"),
        "(ride|horse)": Text(","),
    
        "(just|rejuvenate)": Key("f"),
        "(grow|growth|regrow|regrowth)": Key("g"),
        "(heal|hill)": Key("d"),
        "(big heal|big hill)": Key("h"),
        "(placeholder_t)": Key("t"),
        "(placeholder_r)": Key("r"),
        "(placeholder_y)": Key("y"),
        "(root|roots)": Key("x"),
        "(strap)": Key("c"),
        "(bear|there)": Key("a"),

        "(placeholder_sh)": Key("s-h"),
        "(placeholder_sx)": Key("s-t"),
        "(stealth|shadow)": Key("s-a"),
        "(placeholder_su)": Key("s-u"),
        "(placeholder_sv)": Key("s-v"),
        "(placeholder_sx)": Key("s-x"),
        "(placeholder_sy)": Key("s-y"),

        "(more health)": Key("f2"),
        "(more manner)": Key("f3"),
        "(placeholder_f3)": Key("f3"),
        "(thorns)": Key("f7"),
        "(mark)": Key("f8"),
        "(patch|bandage)": Key("f9"),
        "(drink)": Key("f11"),
        "(eat|food|full)": Key("f12"),

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


_executables = []


def get_rule():
    return DruidRule, RuleDetails(name="druid", executable=_executables)


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

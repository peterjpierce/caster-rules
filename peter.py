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


class PeterRule(MappingRule):

    mapping = {
        "(rake)": R(Function(navigation.right_click)),
        "(cake)": R(Function(navigation.left_click)),
        "(shake)": R(Key("enter")),
        "(junk)": Key("j"),
        "(nova|nick)": Key("n"),
        '(chad)': R(Key('c, d, space')),
        '(goodbye)': R(Text("exit\n")),
        '(temple|tempo)': R(Key('slash, t, m, p, slash')),
        '(go aws)': R(Key('s, s, h, space, w, k, a, enter')),

        '(use|using what|mutt)': R(Text("mutt\n")),

        '(bush|push dev)': R(Text("push origin dev:")),

        '(get nrtc)': R(Text("cd ~/git/nrtc\n")),
        '(get peter)': R(Text("cd ~/git/peter\n")),
        '(go log|go logs)': R(Text("cd /var/log\n")),
        '(go local)': R(Text("cd /var/local\n")),

        '(go one)': R(Key('g, comma, space, a, a, 1, 0, 1, space')),
        '(go to)': R(Key('g, comma, space, a, a, 2, 0, 1, space')),
        '(go three)': R(Key('g, comma, space, a, a, 3, 0, 1, space')),
        '(go for)': R(Key('g, comma, space, a, a, 4, 0, 1, space')),

        #"(throw left)": Key("win") + Key("shift") + Key("left"),
        #"(fling)": R(Text("windows shift left")),
        #"(fling)": R(Key("windows shift left")),
        '(fling)': R(Key("ws-left")),

        '(army)': R(Text('ppierce@nrtc.coop')),
        '(Army)': R(Text('peter@truenorth.us')),
        '(nordic)': R(Text('nrtc')),
        '(tomato)': R(Key('t, m, a, enter')),
        '(moonshot)': R(Text("morning_check\n")),
        '(hammer)': R(Text('vim ')),
        '(sidebar)': R(Text('comma, d, comma, r')),
        '(goose)': R(Text('git ')),
        '(gas)': R(Text('git/')),
        '(fetch upstream)': R(Text("gfu\n")),
        '(fetch both)': R(Text("gfuo\n")),
        '(make directory|make dear)': R(Text('mkdir ')),
    }

    extras = [
        IntegerRefST("n", 1, 10000),
    ]
    defaults = {"n": 0}


_executables = []


def get_rule():
    return PeterRule, RuleDetails(name="peter", executable=_executables)


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

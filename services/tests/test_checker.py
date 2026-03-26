import re
from services import checker


def test_bullets_and_numbered_lists():
    text = "- Did something important\n1. Led the migration\n2) Improved performance"
    bullets = checker._bullets(text)
    assert len(bullets) >= 3


def test_action_verbs_detection():
    text = "- Developed API endpoints\n- Designed schema\n- Maintained docs"
    r = checker.check_action_verbs(text)
    assert r['total'] == 3
    assert r['strong'] >= 2


def test_spelling_grammar_flags_weak_phrases():
    text = "- Was responsible for deployment\n- Helped with onboarding"
    r = checker.check_spelling_grammar(text)
    assert r['count'] >= 1
    assert any('Weak phrase' in i or 'Responsible for' in i for i in r['issues'])


def test_quantify_impact_flags_missing_numbers():
    text = "- Improved user experience by redesigning the onboarding flow which led to better retention and metrics\n- Reduced errors"
    r = checker.check_quantify_impact(text)
    assert r['count'] >= 1

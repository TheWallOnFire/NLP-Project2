import pytest
from app.nodes.intent_node import IntentNode
from app.core.schemas import Priority

def test_intent_node_initialization():
    node = IntentNode()
    assert node is not None

def test_intent_detection_card_lost():
    node = IntentNode()
    result = node.process("I lost my credit card at the mall")
    assert result.intent == "card_lost"
    assert result.confidence > 0.5

def test_intent_detection_balance_inquiry():
    node = IntentNode()
    result = node.process("What is my account balance?")
    assert result.intent == "balance_inquiry"

"""
NLU model for intent classification and entity extraction
in Hindi/Marathi agricultural contexts.
"""
from typing import Dict, List, Any


AGRICULTURAL_INTENTS = {
    "post_job": ["mujhe mazdoor chahiye", "worker chahiye", "मुझे मजदूर चाहिए", "काम के लिए मजदूर"],
    "find_job": ["kaam chahiye", "mujhe kaam chahiye", "काम चाहिए", "मला काम पाहिजे"],
    "check_wage": ["kitna milega", "kitni mazdoori", "कितना मिलेगा", "मजदूरी कितनी"],
}

ENTITY_PATTERNS = {
    "task_type": {
        "HARVESTING": ["kataai", "harvest", "काटाई", "कापणी"],
        "WEEDING": ["nindai", "weed", "निंदाई", "खुरपाई"],
        "SOWING": ["buaai", "sow", "बुआई", "पेरणी"],
        "IRRIGATION": ["sinchai", "irrigate", "सिंचाई"],
    },
    "crop": {
        "wheat": ["gehu", "गेहूं", "wheat"],
        "rice": ["chawal", "dhan", "चावल", "धान"],
        "cotton": ["kapas", "कपास", "cotton"],
        "sugarcane": ["ganna", "गन्ना", "sugarcane"],
    },
}


def classify_intent(text: str) -> str:
    """Classify the intent of a voice command."""
    text_lower = text.lower()
    for intent, keywords in AGRICULTURAL_INTENTS.items():
        if any(kw in text_lower for kw in keywords):
            return intent
    return "unknown"


def extract_entities(text: str) -> Dict[str, Any]:
    """Extract named entities from agricultural text."""
    entities = {}
    text_lower = text.lower()
    for entity_type, patterns in ENTITY_PATTERNS.items():
        for value, keywords in patterns.items():
            if any(kw in text_lower for kw in keywords):
                entities[entity_type] = value
                break
    return entities

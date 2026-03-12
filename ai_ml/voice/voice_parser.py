"""
Voice job parser: transcribe audio and extract structured job data.
"""
import re
from typing import Dict, Any


class VoiceJobParser:
    """Parse voice input into structured job data using Whisper + NLU."""

    TASK_KEYWORDS = {
        "HARVESTING": ["harvest", "kataai", "काटाई", "कापणी", "कटाई"],
        "WEEDING": ["weed", "nindai", "निंदाई", "खुरपाई", "तणकाढणी"],
        "SOWING": ["sow", "buaai", "बुआई", "पेरणी", "बीज"],
        "TRANSPLANTING": ["transplant", "ropai", "रोपाई", "रोपणी"],
        "IRRIGATION": ["irrigat", "sinchai", "सिंचाई", "पाणी देणे"],
        "SPRAYING": ["spray", "davai", "दवाई", "फवारणी"],
        "HARVESTING": ["harvest", "काटाई", "कापणी"],
        "LOADING": ["load", "bhojan", "लोडिंग"],
    }

    CROP_KEYWORDS = [
        "wheat", "gehu", "गेहूं", "rice", "chawal", "चावल",
        "cotton", "kapas", "कपास", "sugarcane", "ganna", "गन्ना",
        "grape", "angur", "अंगूर", "paddy", "dhan", "धान",
        "onion", "pyaj", "प्याज", "soybean", "soya", "सोयाबीन",
    ]

    def parse(self, audio_path: str, language: str = "hi") -> Dict[str, Any]:
        """Transcribe audio and extract job fields."""
        # Step 1: Transcribe using OpenAI Whisper
        # TODO: Integrate real Whisper model
        # import whisper
        # model = whisper.load_model("small")
        # result = model.transcribe(audio_path, language=language)
        # transcript = result["text"]
        transcript = ""

        # Step 2: Extract entities
        return {
            "task_type": self._extract_task_type(transcript),
            "workers_needed": self._extract_workers(transcript),
            "wage_per_day": self._extract_wage(transcript),
            "crop_type": self._extract_crop(transcript),
            "raw_transcript": transcript,
        }

    def _extract_task_type(self, text: str) -> str:
        text_lower = text.lower()
        for task, keywords in self.TASK_KEYWORDS.items():
            if any(kw in text_lower for kw in keywords):
                return task
        return "OTHER"

    def _extract_workers(self, text: str) -> int:
        """Extract number of workers from transcript."""
        patterns = [
            r"(\d+)\s*(?:worker|mazdoor|मजदूर|कामगार|मजूर)",
            r"(\d+)\s*(?:log|लोग|माणसे)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return int(match.group(1))
        return 1

    def _extract_wage(self, text: str) -> float:
        """Extract daily wage from transcript."""
        patterns = [
            r"(?:rs\.?|₹|rupee|rupay)\s*(\d+)",
            r"(\d+)\s*(?:rupee|rupay|रुपये|रुपया)",
        ]
        for pattern in patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return float(match.group(1))
        return 300.0

    def _extract_crop(self, text: str) -> str:
        """Extract crop name from transcript."""
        text_lower = text.lower()
        for crop in self.CROP_KEYWORDS:
            if crop in text_lower:
                return crop.capitalize()
        return "Other"

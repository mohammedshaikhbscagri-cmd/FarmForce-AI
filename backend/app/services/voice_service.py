import re
from typing import Dict, Any


class VoiceService:
    """Parse voice input into structured job data using Whisper + NLU."""

    def parse_voice_to_job(self, audio_path: str, language: str = "hi") -> Dict[str, Any]:
        """Transcribe audio and extract job fields."""
        # Step 1: Transcribe using OpenAI Whisper
        # TODO: import whisper; model = whisper.load_model("small"); result = model.transcribe(audio_path, language=language)
        # transcript = result["text"]

        # Step 2: Use NLU/regex to extract entities
        # (placeholder response)
        transcript = ""

        task_type = self._extract_task_type(transcript)
        workers_needed = self._extract_workers(transcript)
        wage = self._extract_wage(transcript)
        crop = self._extract_crop(transcript)

        return {
            "task_type": task_type,
            "workers_needed": workers_needed,
            "wage_per_day": wage,
            "crop_type": crop,
            "raw_transcript": transcript,
        }

    def _extract_task_type(self, text: str) -> str:
        """Extract task type from transcript."""
        task_keywords = {
            "HARVESTING": ["harvest", "काटाई", "कापणी"],
            "WEEDING": ["weed", "निंदाई", "खुरपाई"],
            "SOWING": ["sow", "बुआई", "पेरणी"],
            "IRRIGATION": ["irrigat", "सिंचाई", "पाणी"],
        }
        text_lower = text.lower()
        for task, keywords in task_keywords.items():
            if any(kw in text_lower for kw in keywords):
                return task
        return "OTHER"

    def _extract_workers(self, text: str) -> int:
        """Extract number of workers from transcript."""
        match = re.search(r"(\d+)\s*(?:worker|mazdoor|मजदूर|कामगार)", text, re.IGNORECASE)
        return int(match.group(1)) if match else 1

    def _extract_wage(self, text: str) -> float:
        """Extract daily wage from transcript."""
        match = re.search(r"(?:rs\.?|₹|rupee)\s*(\d+)", text, re.IGNORECASE)
        return float(match.group(1)) if match else 300.0

    def _extract_crop(self, text: str) -> str:
        """Extract crop name from transcript."""
        crops = ["wheat", "rice", "cotton", "sugarcane", "grape", "paddy", "गेहूं", "चावल", "कपास"]
        text_lower = text.lower()
        for crop in crops:
            if crop in text_lower:
                return crop.capitalize()
        return "Other"

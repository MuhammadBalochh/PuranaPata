import re

class KeywordScanner:
    @staticmethod
    def scan_content(content, keywords):
        matches = []
        for keyword in keywords:
            pattern = re.compile(rf"\b{re.escape(keyword)}\b", re.IGNORECASE)
            matches.extend([(m.group(), m.start()) for m in pattern.finditer(content)])
        return matches

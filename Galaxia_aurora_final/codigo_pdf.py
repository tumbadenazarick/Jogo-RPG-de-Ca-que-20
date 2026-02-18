class CodeOrganizer:
    def __init__(self, files):
        self.files = files
    def analyze_files(self):
        print("Organizando código para PDF...")

class PDFGenerator:
    def __init__(self, output):
        self.output = output
    def generate(self, organizer):
        print(f"PDF {self.output} gerado.")

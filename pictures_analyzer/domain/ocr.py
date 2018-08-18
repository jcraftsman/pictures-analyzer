from pictures_analyzer.domain.file import File


class OCR(object):
    def image_to_text(self, file: File) -> str:
        raise NotImplementedError()

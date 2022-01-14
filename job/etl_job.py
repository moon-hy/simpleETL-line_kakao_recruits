import extract
import transform
import load


class Pipeline:
    def __init__(self, extractor, transformer, loader):
        self.extractor = extractor
        self.transformer = transformer
        self.loader = loader

    def run(self):
        try:
            self.__execute__pipeline()
            self.loader = None
            return "Success"

        except Exception as e:
            print(e)
            return "Fail"

    def __execute__pipeline(self):
        raw_data = self.extractor.extract()
        trans_data = self.transformer.transform(raw_data)
        self.loader.load_list(trans_data)

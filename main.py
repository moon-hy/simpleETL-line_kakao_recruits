from extract.extractor import LineExtractor
from transform.transformer import LineTransformer
from load.loader import Loader
from job.etl_job import Pipeline

if __name__ == '__main__':

    extractor = LineExtractor()
    transformer = LineTransformer()
    loader = Loader()

    pipeline = Pipeline(extractor, transformer, loader)
    pipeline.run()